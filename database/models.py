from sqlalchemy import String, Integer, Column, DateTime, Boolean, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

#Create table of users
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False, unique=True)

#Create questions table
class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    question_text = Column(String, nullable=False)
    level = Column(String, nullable=False)
    v1 = Column(String, nullable=False)
    v2 = Column(String, nullable=False)
    v3 = Column(String, nullable=False)
    v4 = Column(String, nullable=False)
    correct_answer = Column(Integer, nullable=False)

#Create answers table of user
class UserAnswer(Base):
    __tablename__ = "answers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    question_id = Column(Integer, ForeignKey('questions.id'))
    user_answer = Column(Integer, nullable=False)
    correctness = Column(Boolean, default=False)
    answer_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')
    user_fk = relationship(Question, lazy='subquery')

#Create leaders table
class Leader(Base):
    __tablename__ = 'leaders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    correct_answers = Column(Integer, default=0)
    user_fk = relationship(User, lazy='subquery')


