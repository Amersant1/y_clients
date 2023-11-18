from aiogram import *
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import *
from y_clients_lib import YClientsAPI


# database = 'horoscope'

Base = declarative_base()

connection_string = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
    user, password, host, port, database
)


engine = create_engine(url=connection_string)

Session = sessionmaker(engine)()


api = YClientsAPI(
    partner_token=PARTNER_TOKEN,
    user_token=USER_TOKEN,
    company_id=int(company_id),
    form_id=int(PARTNER_ID),
)
