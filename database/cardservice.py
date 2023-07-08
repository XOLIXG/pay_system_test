from database.models import Card, User, Payment
from database import get_db

# Добавить карту в базу
def add_user_card_db(**kwargs):
    db = next(get_db())
    card_number = kwargs.get('card_number')

    # Проверка была ли добавлена карта
    checker = db.query(Card).filter_by(card_number=card_number).first()

    if checker:
        return "Карта естьв базе"

    new_card = Card(**kwargs)
    db.add(new_card)
    db.coomit()

    return "Карта успешно добавлена"

# Удалить карту из сервиса
def delete_user_card_db(card_id, user_id):
    db = next(get_db())
    card = db.query(Card).filter_by(id=card_id, user_id=user_id).first()

    if card:
        db.delete(card)
        db.commit()
        return "Карта успешно удалена"
    else:
        return "Карта не найдена"

# Получить все карты по номеру телефона
def get_user_cards_by_phone_number_db(phone_number):
    db = next(get_db())

    #вместо filter join
    #checker = db.query(Card).join(User.phone_number == phone_number).first()
    checker = db.query(Card).filter(User.phone_number == phone_number).first()

    return checker
    # user = db.query(User).filter_by(phone_number=phone_number).first()
    #
    # if user:
    #     cards = db.query(Card).filter_by(user_id=user.id).all()
    #     return cards
    # else:
    #     return "Пользователь не найден"


# Получить определенную карту
def get_exact_user_card_db(user_id, card_id):
    db = next(get_db())
    # card = db.query(Card).filter_by(id=card_id, user_id=user_id).first()
    #
    # if card:
    #     return card
    # else:
    #     return "Карта не найдена"
    db = next(get_db())
    if card_id == 0:
        card_data = db.query(Card).filter_by(user_id=user_id).all()

    else:
        card_data = db.query(Card).filter_by(user_id=user_id, card_id=card_id).first()

    return card_data

# Получить все транзакции по определенной карте или по всем
def get_all_cards_for_exact_transactions(user_id, card_id: int = 0):
    db = next(get_db())
    if card_id == 0:
        card_monitor = db.query(Payment).filter_by(user_id=user_id).all()

    else:
        card_monitor = db.query(Payment). filter_by(user_id=user_id, card_id=card_id).all()

    return card_monitor