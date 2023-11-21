from controller import *
from model import *
from sqlalchemy import extract  
session = sessionmaker(engine)()


def getDataMonth(month_number):
    clients = set()
    filter = list()
    filter.append(extract('month', Appointment.datetime_of_appointment) == month_number + 1)

    appoints = session.query(Appointment).filter(*filter).all()
    for appoint in appoints:
        clients.add(appoint.client_id)

    return clients

months = []
for i in range(12):
    months.append(getDataMonth(i))


appointmentsChange = dict()

for i in range(12):
    monthData = []
    for j in range(i):
        monthData.append(len(months[i] & months[j]))
    appointmentsChange[i+1] = monthData
print(appointmentsChange)






