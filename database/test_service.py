from .models import Leader, Question
from database import get_db

#Function for displaying leaders
def get_leaders_db():
    db = next(get_db())

    leaders = db.query(Leader.user_id).order_by(Leader.correct_answers.desc())

    return leaders[:5]

#Adding questions to db
def add_questions_db(question_text, correct_answer, level, v1, v2, v3, v4):
    db = next(get_db())
    new_question = Question(question_text=question_text, correct_answer=correct_answer, level=level, v1=v1, v2=v2, v3=v3, v4=v4)
    db.add(new_question)
    db.commit()
    return 'Question successfully added'

#Displaying 20 questions from db
def get_question_db():
    db = next(get_db())
    question = db.query(Question).all()
    return question[:20]