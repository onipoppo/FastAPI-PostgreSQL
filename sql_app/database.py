# SQLAlchemyを使ってデータベースのエンジンを作成する。Postgresqlとの接続を試す。
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

db_user = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')
db_database = os.getenv('DB_DATABASE')

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://{db_user}:{db_password}@PostgreSQL:5432/{db_database}'.format(db_user=db_user, db_password=db_password, db_database=db_database)
# SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://user_fastapi:password_fastapi@PostgreSQL:5432/sample"

# sqlite3限定：connect_args={"check_same_thread": False}
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
