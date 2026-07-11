from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, Field

# Liên kết bảng model
from model import Base

# liên kết bảng service
from service import get_item, get_item_id, add_new_item, update_item, delete_item, search_group_name
from sqlalchemy.orm import Session
from database import get_db, engine
from schema import BaseTeam, NameTeam

app = FastAPI()


# siêu quan trọng
Base.metadata.create_all(bind=engine)

# tìm kiếm


@app.get('/teams/search')
def search_player(group_name: str, db: Session = Depends(get_db)):
    search = search_group_name(db, group_name)
    if not search:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Không thấy'
        )
    return search


# lấy chi tiết đội tuyển


@app.get('/teams/{team_id}')
def list_data_id(item_id: int, db: Session = Depends(get_db)):
    list_id = get_item_id(db, item_id)
    if not list_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Không thấy'
        )
    return list_id

# thêm đội tuyển mới


@app.post('/teams')
def add_new_player(item_data: BaseTeam, db: Session = Depends(get_db)):
    add_new = add_new_item(db, item_data)
    status_code = status.HTTP_201_CREATED
    return {
        'message': "Them thanh cong",
        'status_code': status_code,
        'data': add_new
    }

# cật nhập đội tuyển


@app.put('/team/{team_id}')
def update_player(item_id: int, item_data: BaseTeam, db: Session = Depends(get_db)):
    update = update_item(db, item_id, item_data)
    if not update:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Không thấy'
        )
    return {
        'message': 'cật nhập thành công',
        'data': update
    }

# xoá


@app.delete('/teams/{team_id}')
def delete_player(item_id: int, db: Session = Depends(get_db)):
    delete = delete_item(db, item_id)
    if not delete:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Không thấy'
        )
    return {
        'message': 'thành công xoá',
        'data': delete
    }

# lấy danh sách đội tuyển


@app.get('/get/teams')
def list_data(db: Session = Depends(get_db)):
    list = get_item(db)
    if not list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Không thấy'
        )
    return list
