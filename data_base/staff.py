from model import *

STAFF = dict()


def __make_session():
    session = sessionmaker(engine)()
    return session


def make_staff_member(
    y_clients_id,
    name,
    specialization,
    session=None,
):
    bola = True
    if session is None:
        session = __make_session()
        bola = False
    if y_clients_id in STAFF:
        return STAFF[y_clients_id]
    staff = session.query(Staff).filter(Staff.y_clients_id == y_clients_id).first()
    if staff is None:
        staff = Staff(
            y_clients_id=y_clients_id,
            name=name,
            profit=0,
            type_of_service=specialization,
        )

        session.add(staff)
        session.flush()
        session.refresh(staff)
        return staff.id
    else:
        return staff.id
    if bola == False:
        session.commit()
        session.close()
    return None


def get_staff_global():
    global STAFF
    session = __make_session()

    staff = session.query(Staff).all()
    for staff_1 in staff:
        STAFF[staff_1.y_clients_id] = staff_1.id


get_staff_global()
