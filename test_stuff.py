from controller import *
from model import *
jenuary = set()
february = set()
same = ()
from sqlalchemy import extract  
session = sessionmaker(engine)()

def getDataMonth(staff_id, month_number):
    month = set()
    
    filter = list()
    filter.append(Appointment.staff_id == staff_id)
    filter.append(extract('month', Appointment.datetime_of_appointment) == month_number)

    appoints = session.query(Appointment).filter(*filter).all()
    for appoint in appoints:
        month.add(appoint.client_id)

    return month

#staff
staffs = session.query(Staff).all()
for person in staffs:
    jenuary = getDataMonth(person.id, 1)
    february = getDataMonth(person.id, 2)
    same = jenuary & february


    print(len(same))



