from sqlalchemy import create_engine, Column, Integer, String, Enum
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv
from User.Domain.Entities.UserType import UserType

Base = declarative_base()

class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone = Column(String(20), nullable=False, unique=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    user_uuid = Column(String(36), unique=True)
    type = Column(Enum(UserType))
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'last_name': self.last_name,
            'phone': self.phone,
            'email': self.email,
            'password': self.password,
            'user_uuid': self.user_uuid
        }

class SurveyModel(Base):
    __tablename__ = 'surveys'

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    survey_uuid = Column(String(36), unique=True)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'survey_uuid': self.survey_uuid
        }
    
class AskModel(Base):
    __tablename__ = 'asks'

    id = Column(Integer, primary_key=True)
    ask = Column(String(50), nullable=False)
    ask_uuid = Column(String(36), unique=True)

    def to_dict(self):
        return {
            'id': self.id,
            'ask': self.ask,
            'ask_uuid': self.ask_uuid
        }

class AwardModel(Base):
    __tablename__ = 'awards'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=False)
    award_uuid = Column(String(36), unique=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'award_uuid': self.award_uuid
        }



class DBConnection:
    def __init__(self):
        load_dotenv()

        host = os.getenv('DB.HOST_MYSQL')
        port = os.getenv('DB.PORT_MYSQL')
        user = os.getenv('DB.USER_MYSQL')
        password = os.getenv('DB.PASSWORD_MYSQL')
        database = os.getenv('DB.DATABASE_MYSQL')

        try:
            self.engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')
            Base.metadata.create_all(self.engine)
            self.Session = sessionmaker(bind=self.engine)
            print("Conexión exitosa a la base de datos con MySQL LISTA!")
        except Exception as e:
            print(f"Error al conectar a la base de datos: {str(e)}")