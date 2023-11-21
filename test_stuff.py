from controller import *
from model import *
from sqlalchemy import extract  
session = sessionmaker(engine)()

def getDataMonth(staff_id, month_number):
    clients = set()
    filter = list()
    filter.append(Appointment.staff_id == staff_id)
    filter.append(extract('month', Appointment.datetime_of_appointment) == month_number + 1)

    appoints = session.query(Appointment).filter(*filter).all()
    for appoint in appoints:
        clients.add(appoint.client_id)

    return clients

#staff
staffs = session.query(Staff).all()
each_staff = []
for person in staffs:

    appointmentsChange = dict()
    months = []
    for i in range(12):
        months.append(getDataMonth(person.id, i))

    for i in range(12):
        monthData = []
        for j in range(i):
            monthData.append(len(months[i] & months[j]))
        appointmentsChange[i+1] = monthData

    each_staff.append(appointmentsChange)




