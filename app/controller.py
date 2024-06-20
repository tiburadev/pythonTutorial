from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app import responses

# Define the engine and session
engine = create_engine('mysql+mysqlconnector://root:Tibura2018!@localhost/classicmodels')
Session = sessionmaker(bind=engine)
session = Session()

# Define the base
Base = declarative_base()

# Define the User model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
    # def __init__(self, data):
    #     self.name = data.get('name')
    #     self.email = data.get('email')
    @staticmethod
    def get_all_users():
        
        # Create tables
       # Base.metadata.create_all(engine)

    

    # Query users
        users = session.query(User).all()
        user_list = [(user.name, user.email) for user in users]
        print(user_list)
        return user_list
    @staticmethod
    def add_user(data):
     try:
        # Add a new user
        
        # Create tables
        print(data,'kkkkkk')
        Base.metadata.create_all(engine)
        new_user = User(data)
        session.add(new_user)
        session.commit()
        return  responses.get(200,"Sucess","user added ",True)
     except Exception as e:
        session.rollback()
        print(f"Error occured :{e}")
        return  responses.get(404,"Error",f"{e}",True)
