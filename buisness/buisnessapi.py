from fast import app
from database.businessservice import register_business_category_db, register_business_db, \
    get_business_categories_db, get_exact_business_db, \
    pay_for_service_db, delete_business_db, delete_business_category_db

# Регистрация категории бизнеса
@app.post('/register-business-category')
async def register_business_category_api(name: str):
    result = register_business_category_db(name=name)

    return {"status": 1, "message": result}

# Регистрация бизнеса
@app.post('/register-business')
async def register_business_api(category_id: int, name: str, card_number: int):
    result = register_business_db(category_id=category_id,
                                  name=name,
                                  card_number=card_number)

    return {"status": 1, "message": result}

# Вывод всех категорий
@app.get('/get-all-categories')
async def get_business_categories_api(exact_category_id: int = 0):
    categories = get_business_categories_db(exact_category_id=exact_category_id)

    return {"status": 1, "categories": categories}

# Вывод услуг
@app.get('/get-business')
async def get_exact_business_api(business_id: int, category_id: int):
    business = get_exact_business_db(business_id=business_id,
                                     category_id=category_id)

    return {"status": 1, "business": business}

# Оплата услуги
@app.post('/pay-service')
async def pay_for_service_api(business_id: int, from_card: int, amount: float):
    result = pay_for_service_db(business_id=business_id,
                                from_card=from_card,
                                amount=amount)

    return {"status": 1, "message": result}

# Удалить бизнес
@app.delete('/delete-business')
async def delete_business_api(business_id: int):
    result = delete_business_db(business_id=business_id)

    return {"status": 1, "message": result}

@app.delete('/delete-business-category')
async def delete_business_category_api(category_id):
    result = delete_business_category_db(category_id=category_id)

    return {"status": 1, "message": result}