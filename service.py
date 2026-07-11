# Thực hiện vấn đề
from sqlalchemy.orm import Session
from model import WorldCup
from schema import TeamCreate, BaseTeam


def get_item(db: Session):
    get_list = db.query(WorldCup).all()
    return get_list


def get_item_id(db: Session, item_id: int):
    get_list_id = db.query(WorldCup).filter(
        WorldCup.id == item_id).first()
    return get_list_id

# phải nhập theo tên để cật nhập


def add_new_item(db: Session, item_data: TeamCreate):
    new_player = WorldCup(**item_data.model_dump())
    db.add(new_player)
    db.commit()
    db.refresh(new_player)
    return new_player

# cật nhập đội tuyển


def update_item(db: Session, item_id: int, item_data: BaseTeam):
    item = db.query(WorldCup).filter(WorldCup.id == item_id).first()
    if item:
        for key, value in item_data.model_dump(exclude_unset=True).items():
            setattr(item, key, value)
            db.commit()
            db.refresh(item)
    return item

# xoá


def delete_item(db: Session, item_id: int):
    item = db.query(WorldCup).filter(WorldCup.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
        return item
    return None

# tìm kiếm


def search_group_name(db: Session, group_name: str):
    search = db.query(WorldCup).filter(
        WorldCup.group_name.ilike(f"%{group_name}%")).all()
    return search
