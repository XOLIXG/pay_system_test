from database.models import Payment, ServiceCategory, Service
from database import get_db


# Регистрация категории бизнеса
def register_business_category_db(name: str):
    db = next(get_db())
    new_category = ServiceCategory(category_name=name)
    db.add(new_category)
    db.commit()

    return "Категория бизнеса успешно зарегистрирована"

# Регистрация бизнеса
def register_business_db(category_id: int, name: str, card_number: int):
    db = next(get_db())
    new_business = Service(service_category=category_id,
                           servoce_name=name,
                           service_check=card_number)
    db.add(new_business)
    db.commit()

    return "Бизнес успешно зарегистрирован"

# Вывод всех категорий
def get_business_categories_db(exact_category_id: int = 0):
    db = next(get_db())
    if exact_category_id == 0:
        categories = db.query(ServiceCategory).all()
    else:
        categories = db.query(ServiceCategory).filter_by(category_id=exact_category_id).all()

    return categories

# Вывод услуг
def get_exact_business_db(business_id: int, category_id: int):
    db = next(get_db())
    business = db.query(Service).filter_by(service_id=business_id,
                                           category_id=category_id).first()

    if business:
        return business
    else:
        return "Бизнес не найден"

# Оплата услуги
def pay_for_service_db(business_id: int, from_card: int, amount: float):
    db = next(get_db())
    transaction = Payment(business_id=business_id,
                              card_id=from_card,
                              amount=amount)
    db.add(transaction)
    db.commit()

    return "Услуга успешно оплачена"

# Удалить бизнес
def delete_business_db(business_id: int):
    db = next(get_db())
    business = db.query(Service).filter_by(service_id=business_id).first()

    if business:
        db.delete(business)
        db.commit()
        return "Бизнес успешно удален"
    else:
        return "Бизнес не найден"

def delete_business_category_db(category_id: int):
    db = next(get_db())
    business_category = db.query(ServiceCategory).filter_by(category_id=category_id).first()

    if business_category:
        db.delete(business_category)
        db.commit()
        return "Категория успешно удален"
    else:
        return "Категория не найдена"