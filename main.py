from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, Field

# Liên kết bảng model
from model import Base

# liên kết bảng service
from service import get_item, get_item_id, add_new_item, update_item, delete_item, search_group_name
from sqlalchemy.orm import Session
from database import get_db, engine
from schema import TeamCreate, BaseTeam, NameTeam

app = FastAPI()


# siêu quan trọng
Base.metadata.create_all(bind=engine)


# lấy danh sách đội tuyển


@app.get('/get/teams')
def list_data(db: Session = Depends(get_db)):
    list = get_item(db)
    if list == '':
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Không thấy'
        )
    return list

# lấy chi tiết đội tuyển


@app.get('/teams/{team_id}')
def list_data(item_id: int, db: Session = Depends(get_db)):
    list_id = get_item_id(db, item_id)
    if not list_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Không thấy'
        )
    return list_id

# thêm đội tuyển mới


@app.post('/teams')
def add_new_player(item_data: TeamCreate, db: Session = Depends(get_db)):
    add_new = add_new_item(db, item_data)
    return {
        'message': "Them thanh cong",
        'data': add_new
    }

# cật nhập đội tuyển


@app.put('/team/{team_id}')
def update_player(item_id: int, item_data: BaseTeam, db: Session = Depends(get_db)):
    update = update_item(db, item_id, item_data)
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

# tìm kiếm


@app.get('/teams/search')
def search_player(item_group_name=str, db: Session = Depends(get_db)):
    search = search_group_name(db, item_group_name)
    if not search:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Không thấy'
        )
    return search
