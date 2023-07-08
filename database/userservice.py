from database.models import User, Password
from database import get_db

def register_user_db(**kwargs):
    db = next(get_db())

    phone_number = kwargs.get('phone_number')

    checker = db.query(User).filter_by(phone_number=phone_number).first()

    if checker:
        return "Пользователь с таким номером уже существует в базе"
    new_user = User(**kwargs)
    db.add(new_user)
    db.commit()

    new_user_password = Password(user_id=new_user.user_id, **kwargs)
    db.add(new_user_password)
    db.commit()

    return "Пользователь успешно добавлен в базу"

def check_password_db(phone_number,  password):
    db = next(get_db())

    checker = db.query(Password).filter_by(phone_number=phone_number).first

    if checker and checker.password == password:
        return checker.user_id
    elif not checker:
        return 'Ошибка данных'
    elif checker.password != password:
        return "Неверный пароль"

def get_user_cabinet_db(user_id):
    db = next(get_db())

    checker = db.query(User).filter_by(user_id=user_id).first

    if checker:
        return checker
    return "Ошибка в данных"
