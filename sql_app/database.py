from sqlalchemy import create_engine
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

postgres_password = os.environ.get("POSTGRES_PASSWORD")
postgres_port = os.environ.get("POSTGRES_PORT")
postgres_user = os.environ.get("POSTGRES_USER")
postgres_host = os.environ.get("POSTGRES_HOST")
postgres_db = os.environ.get("POSTGRES_DB")

#SQLALCHEMY_DATABASE_URL = "sqlite:///./ecommerce_fastapi.db"
SQLALCHEMY_DATABASE_URL = f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL#, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

print(Base.metadata.create_all)
