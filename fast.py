from fastapi import FastAPI
from database import Base, engine

# создать таблицы для базы данных
Base.metadata.create_all(bind=engine)

# обьект для FastApi
app = FastAPI()

from buisness import buisnessapi
from card_mamnagment_stansfer import cardapi
from user_aunthenfication import userapi

#  Запук проета FastApi
#  uvicorn fast:app --reload