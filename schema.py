# schema là giới hạn cho người dùng nhập kiểu dữ liệu đúng sai
from pydantic import BaseModel, Field

# Schema dùng để nhận dữ liệu khi Tạo mới (POST)


class TeamCreate(BaseModel):
    country_name: str = Field(..., max_length=50, min_length=1)


class NameTeam(BaseModel):
    group_name: str = Field(..., max_length=100, min_length=1)


class BaseTeam(BaseModel):
    country_name: str = Field(..., max_length=50, min_length=1)
    coach_name: str = Field(..., max_length=100, min_length=1)
    group_name: str = Field(..., max_length=100, min_length=1)
    point: int = Field(..., ge=0)  # ge=0 đảm bảo điểm không âm

# Schema dùng để trả về dữ liệu (Response) - Nên có id


class TeamResponse(BaseTeam):
    id: int

    class Config:
        from_attributes = True  # Quan trọng: để FastAPI hiểu dữ liệu từ SQLAlchemy
