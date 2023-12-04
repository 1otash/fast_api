from .models import User, Question, UserAnswer, Leader
from database import get_db
from datetime import datetime

# Create user registration
def register_user_db(name, phone):
    db = next(get_db())
    # Check if user in database
    checker = db.query(User).filter_by(phone=phone).first()
    if checker:
        #user_id
        return checker.id
    else:
        #If is not in base then register
        new_user = User(name=name, phone=phone)
        db.add(new_user)
        db.commit()
        return new_user.id

#Entry of every answer
def set_user_answer_db(user_id, question_id, user_answer):
    #Create connection to db
    db = next(get_db())
    #Find current answer in db
    exact_question = db.query(Question).filter_by(id=question_id).first()
    #If there is question in db with current id specifically with exact_question
    if exact_question:
        #Comparing user answer with answer in db
        if exact_question.correct_answer == user_answer:
            correctness = True
        else:
            correctness = False

        #Create object for db
        new_user = UserAnswer(user_id=user_id, question_id=question_id, user_answer=user_answer, correctness=correctness)

        db.add(new_user)
        db.commit()

        return True if correctness else False

    return 'Question is not found'

#Increasing marks of users
def increment_user_points_db(user_id, correct_answers):
    db = next(get_db())

    checker = db.query(Leader).filter_by(user_id=user_id).first()

    if checker:
        checker.correct_answers += correct_answers

    else:
        new_leader_data = Leader(user_id=user_id, correct_answers=correct_answers)

        db.add(new_leader_data)
        db.commit()

    # get position in list
    all_leaders = db.query(Leader.user_id).order_by(Leader.correct_answers.desc())

    return all_leaders.index((user_id,)) + 1
