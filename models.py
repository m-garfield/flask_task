from sqlalchemy import create_engine, Column, Integer, String, DateTime, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from atexit import register

PG_USER = 'app'
PG_PASSWORD = '0000'
PG_HOST = '127.0.0.1'
PG_PORT = 5431
PG_DB = 'app'
PG_DSN = f'postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}'

engine = create_engine(PG_DSN)
register(lambda: engine.dispose())
Session = sessionmaker(bind=engine)
Base = declarative_base(bind=engine)


class Message(Base):
    __tablename__ = 'app_message'
    id = Column(Integer, primary_key=True)
    message_user = Column(String, nullable=False)
    message_headers = Column(String, nullable=False)
    message_text = Column(String, nullable=False)
    message_time_create = Column(DateTime, server_default=func.now())

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


Base.metadata.create_all(bind=engine)
