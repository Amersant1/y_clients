from model import *

SERVICES = dict()
SERVICES_DICT_WITH_DATA = dict()


def __make_session():
    session = sessionmaker(engine)()
    return session


def add_service(
    name,
    y_clients_id,
    now_day_price,
    session=None,
    description=str(),
    end_session=False,
) -> int:
    if session is None:
        session = __make_session()

    if y_clients_id in SERVICES:
        return None
    service = (
        session.query(Service).filter(Service.y_clients_id == y_clients_id).first()
    )
    if not (service is None):
        service_price = service.now_day_price
        if service != now_day_price:
            setattr(service, "now_day_price", now_day_price)
        id = service.id
    else:
        new_service = Service(
            y_clients_id=y_clients_id,
            name=name,
            description=description,
            now_day_price=now_day_price,
        )
        session.add(new_service)
        session.flush()
        session.refresh(new_service)
        id = new_service.id
    if end_session:
        session.commit()
    return id


def get_services():
    global SERVICES
    global SERVICES_DICT_WITH_DATA
    session = __make_session()
    filter = list()

    services = session.query(Service).all()
    for service in services:
        SERVICES[service.y_clients_id] = service.id
        SERVICES_DICT_WITH_DATA[service.id] = service.as_dict()
        if service.name in GLOBAL_CALL_TIME:
            SERVICES_DICT_WITH_DATA[service.id]["call_after_time"] = GLOBAL_CALL_TIME[service.name]
        else:
            

            SERVICES_DICT_WITH_DATA[service.id]["call_after_time"] = 30

get_services()
