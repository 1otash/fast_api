from fastapi import APIRouter
from database.test_service import get_question_db, add_questions_db
from database.user_service import set_user_answer_db

test_router = APIRouter(prefix='/test', tags=['Test walkthrough'])

# Get 20 questions
@test_router.get('/get-questions')
async def get_question():
    # Connect to db for access 20 questions
    questions_list = get_question_db()
    if questions_list:
        return {'timer': 12, 'questions': questions_list}
    else:
        return 'No questions!'

#Check every answer of users
@test_router.post('/check_answer')
async def check_answer(user_id: int, question_id: int, user_answer: int):
    # Connect to db for answers
    result = set_user_answer_db(user_id, question_id, user_answer)
    if result:
        return {'status': result}
    else:
        return 'No answers'


#Add questions(tests)
@test_router.post('/add-questions')
async def add_question(question_text: str, correct_answer: int, level: str, v1: str, v2: str, v3: str, v4: str):
    result = add_questions_db(question_text, correct_answer, level, v1, v2, v3, v4)
    if result:
        return {'status': 'success', 'message':result }
    else:
        return "Can't add question"