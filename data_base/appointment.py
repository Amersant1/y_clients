from model import *
from data_base import *

APPOINTMENTS = dict()
get_clients()


def __make_session():
    session = sessionmaker(engine)()
    return session


def make_appointment(
    client_id,
    y_clients_id,
    staff_id,
    services,
    price,
    
    datetime_of_appointment,
    is_paid =True,

    description=None,
    session = None
):
    if session is None:
        session = __make_session()
    try:
        appointment_id =APPOINTMENTS[y_clients_id]
    except:
        appointment = session.query(Appointment).filter(Appointment.y_clients_id==y_clients_id).first()

        if not(client_id in CLIENTS):
            client = get_client(y_clients_id=client_id,session=session)
            try:
                CLIENTS[client_id] = client.id
            except:
                return None
            client_id = client.id
            CLIENTS[client_id] = client.id
        else:
            client_id = CLIENTS[client_id]

        if appointment is None:
            appointment = Appointment(
                y_clients_id=y_clients_id,
                client_id=client_id,
                staff_id=staff_id,
                price=price,
                is_paid = is_paid,
                datetime_of_appointment=datetime_of_appointment,
                description=description,
            )
            session.add(appointment)
            session.flush()
            session.refresh(appointment)
        appointment_id = appointment.id


    for service in services:
        if not(service["y_clients_id"] in SERVICES):

            new_service = session.query(Service).filter(Service.y_clients_id==service["y_clients_id"]).first()
            SERVICES[new_service.y_clients_id] = new_service.id
        # appointment_service =session.query(Appointment_Service).filter(Appointment_Service.y_clients_id == service["y_clients_id"]).first()
        # if appointment_service is None:
        #     new_appointment_service = Appointment_Service(service_id=new_service.id,appointment_id=appointment.id,discount = service["discount"],y_clients_id = service["y_clients_id"])
        #     session.add(new_appointment_service)
        # else:
        new_appointment_service = Appointment_Service(service_id=SERVICES[service["y_clients_id"]],appointment_id=appointment_id,discount = service["discount"],y_clients_id = service["y_clients_id"])
        session.add(new_appointment_service)

        
def get_appointments():
    global APPOINTMENTS
    session=__make_session()
    
    appointments= session.query(Appointment).all()
    for appointment in appointments:
        APPOINTMENTS[appointment.y_clients_id] = appointment.id


get_appointments()