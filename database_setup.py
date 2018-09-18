import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))
    password_hash = Column(String(64))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {'name': self.name, 'email': self.email, 'id': self.id}


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {'name': self.name, 'id': self.id, 'user_id': self.user_id}


class CategoryItem(Base):
    __tablename__ = 'category_item'
    name = Column(String(80), nullable=False)
    description = Column(String(250))
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'category_id': self.category_id,
            'category': self.category,
            'user_id': self.user_id
        }


engine = create_engine('sqlite:///Catalog.db')
Base.metadata.create_all(engine)
