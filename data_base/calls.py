from model import *
from datetime import timedelta
from datetime import datetime

def __make_session():
    session = sessionmaker(engine)()
    return session


def get_calls_on_date(date,session=None):
    if session is None:
        session=__make_session()

    calls=session.query(Call).filter(Call.call_date==date).all()
    return calls


def add_new_call(date,client=None,phone=None,client_id=None,service_id=None,session = None):
    if session is None:
        session = __make_session()
    if not(client is None):
        phone = client.phone
        client_id = client.id
    call = session.query(Call).filter(Call.call_date==date,Call.client_id==client_id,Call.service_id==service_id).first()
    if not(call is None):
        return None

    call = Call(
        client_id =client_id,
    call_date = date,
    service_id = service_id,
    number_of_calls = 0,
    is_answered =False,
    doesnt_need_to_call=False
        )

    session.add(call)
    session.commit()
    return None


def get_not_answered_calls_from_the_past_in_db(date=None,session=None):
    if date is None:
        date=datetime.now()
    if session is None:
        session=__make_session()
    calls = session.query(Call).filter(Call.call_date<date,Call.number_of_calls==0).all()
    return calls


def get_calls_on_today_from_base(date=None,session=None):
    if date is None:
        date=datetime.now()
    if session is None:
        session=__make_session()
    calls = session.query(Call).filter(Call.call_date==date,).all()
    return calls

def change_call_to_answer_in_db(id):
    session = __make_session()
    call = session.query(Call).filter(Call.id==id).first()
    setattr(call,"is_answered",True)
    session.commit()


def didnt_answer_db(id,delta_days=3):
    session = __make_session()
    now = datetime.now().date()
    call = session.query(Call).filter(Call.id==id).first()
    number_of_calls=call.number_of_calls
    call_date=call.call_date
    if call_date<now:
        new_call_date=now+timedelta(3)
    else:
        new_call_date = call_date+timedelta(days=delta_days)
    setattr(call,"is_answered",False)
    setattr(call,"call_date",new_call_date)
    setattr(call,"number_of_calls",number_of_calls+1)
    session.commit()

def answered_bd(id,):
    session = __make_session()
    call = session.query(Call).filter(Call.id==id).first()
    number_of_calls=call.number_of_calls

    setattr(call,"is_answered",True)
    setattr(call,"number_of_calls",number_of_calls+1)
    session.commit()

def doesnt_need_to_answer_call_bd(id):
    session = __make_session()
    call = session.query(Call).filter(Call.id==id).first()
    number_of_calls=call.number_of_calls

    setattr(call,"doesnt_need_to_call",True)
    session.commit()


    