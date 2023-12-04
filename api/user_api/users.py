from fastapi import APIRouter
from database.test_service import get_leaders_db
from database.user_service import register_user_db, increment_user_points_db


user_router = APIRouter(prefix='/users', tags=['User'])

# Register user
@user_router.post('/register')
async def register_user(name, phone):
    registration = register_user_db(name, phone)
    if registration:
        return {'status': 'success', 'message': registration}
    else:
        return 'Cant register user'

#Users list
@user_router.get('/leaders')
async def get_leaders():
    leaders = get_leaders_db()
    if leaders:
        return {'list': leaders}
    else:
        return 'Error'

# Post result of every user
@user_router.post('/done')
async def test_finished(user_id, correct_answers):
    finished = increment_user_points_db(user_id, correct_answers)
