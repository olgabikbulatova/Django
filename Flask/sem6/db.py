from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy import create_engine
import databases
from settings import settings

DATABASE_URL = settings.DATABASE_URL
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(2)),
    sqlalchemy.Column("surname", sqlalchemy.String(32)),
    sqlalchemy.Column("b_day", sqlalchemy.Date),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
    sqlalchemy.Column("address", sqlalchemy.String(128)),
    sqlalchemy.Column("password", sqlalchemy.String(128)),
)
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)
