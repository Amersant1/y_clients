from data_base import *
from datetime import datetime, timedelta
from data_base import SERVICES_DICT_WITH_DATA
from dateutil.relativedelta import relativedelta
import pandas as pd
import numpy as np
def make_phone_calls_on_today():
    
    appointments = get_clients_from_bd()
    now = datetime.now()
    for appointment in appointments:
        days=100
        final_service=None
        #тут надо добавить перебор всех сервисов 
        for service in appointment.services:
            try:
                if SERVICES_DICT_WITH_DATA[service.service_id]["call_after_time"]<days:
                    days=SERVICES_DICT_WITH_DATA[service.service_id]["call_after_time"]
                    final_service =service
            except Exception as err:
                print(f"couldn't find service with id {service.service_id} and name:{service.service.name}\n\n\nor err: {err}")
        date = appointment.datetime_of_appointment.date()
        delta = now.date() - date
        if delta.days == days:
            user = appointment.client
            add_new_call(date=now,client=user,service_id=final_service.service_id)
    return  None


def get_clients_from_bd(days=60):
    now = datetime.now()
    day = now - timedelta(days=days)
    appointments = get_appointments_with_filters(start_datetime_of_appointment=day)

    return appointments


# def transport_calls_from_the_past():
    

def get_calls_today():
    session = make_session()
    calls=get_calls_on_today_from_base(session=session)
    calls.extend(get_not_answered_calls_from_the_past_in_db(session=session))
    
    return calls


def get_phone_calls():
    now = datetime.now()
    calls = get_calls_on_date(now.date())
    return calls


def change_call_to_answer(id):
    try:
        change_call_to_answer_in_db(id)
    except Exception as err:
        print(err)



def transform_calls_to_dict(calls):
    for call in calls:
        call = call.as_dict()



def night_time_transfer():
    pass


def didnt_answer_change(id):

    didnt_answer_db(id,delta_days=3)


def answered_call(id):
    answered_bd(id)


def doesnt_need_to_answer(id):
    doesnt_need_to_answer_call_bd(id)



def make_getting_back_info(start:datetime,end:datetime,period_days=None,period_months=None):
    start=start.date()
    end=end.date()

    if not(period_days is None):
        delta=timedelta(days=period_days)
    elif not(period_months is None):
        delta = relativedelta(months=period_months)
    else:
        return None

    full_dictionary = dict()
    appointments_dict = dict()
    current_date = start
    list_of_periods = list()
    i=0
    while True:
        full_dictionary[i] = dict()
        new_end = current_date+delta
        if new_end>end:
            break
        list_of_periods.append(f"{current_date.strftime(DATE_FORMAT)} : {new_end.strftime(DATE_FORMAT)}")
        appointments=get_appointments_with_filters(start_datetime_of_appointment=current_date,end_datetime_of_appointment=new_end)
        
        for appointment in appointments:
            if not(appointment.client.y_clients_id in appointments_dict):
                appointments_dict[appointment.y_clients_id]=i
            else:
                full_dictionary[appointments_dict[appointment.y_clients_id]][i]+=1

        current_date=current_date+delta
        i+=1
    for index in full_dictionary.keys():
        for new_index in full_dictionary[index]:
            full_dictionary[index][list_of_periods[new_index]] = full_dictionary[index][new_index]
            del(full_dictionary[index][new_index])
        full_dictionary[list_of_periods[new_index]] = full_dictionary[index]
        del (full_dictionary[index])
    return full_dictionary
    


def get_dataframe_of_info_of_get_back(start:datetime,end:datetime,period_days=None,period_months=None):
    dicti = make_getting_back_info(start,end,period_days,period_months) 
    df = pd.DataFrame(dicti)
    return df


def convert_df_to_excel(df:pd.DataFrame):
    path="STATISTICS.xlsx"
    excel = df.to_excel(path,sheet_name='information')
    return path