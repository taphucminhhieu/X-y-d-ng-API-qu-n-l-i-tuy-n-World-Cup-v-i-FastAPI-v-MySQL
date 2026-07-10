from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

database_url = "mysql+pymysql://root:23112007@localhost:3306/worldcup_db"

engine = create_engine(database_url)

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
