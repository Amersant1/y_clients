from controller import *
from model import *


session = sessionmaker(engine)()


appoints = session.query(Appointment).filter(Appointment.price>500).all()
for appoint in appoints:
    print(appoint.price,appoint.client_id)




