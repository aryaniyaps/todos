from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import (
    declarative_base, 
    scoped_session, 
    sessionmaker
)

from app.config import DEBUG, DATABASE_URL

metadata = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    },
)

Base = declarative_base(metadata=metadata)

engine = create_engine(url=DATABASE_URL, future=True, echo=DEBUG)

db_session = scoped_session(sessionmaker(bind=engine))
