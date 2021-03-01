from sqlalchemy import Column, Integer, String
from dao.engine import engine, Base
from dataclasses import dataclass

@dataclass
class User(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    phone = Column(String(50))
    email = Column(String(50))

    def __repr__(self):
        return "<User(name='%s', phone='%s', email='%s')>" % (self.name, self.phone, self.email)

Base.metadata.create_all(engine)