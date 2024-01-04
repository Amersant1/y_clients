from model import *

CLIENTS = dict()


def __make_session():
    session = sessionmaker(engine)()
    return session


def make_client(
    y_clientys_id,
    name,
    surname,
    patronymic,
    display_name,
    phone,
    email,
    birth_date: str("%d.%m.%Y"),
    sex_id,
    last_change_date: str("2020-08-07T14:04:25+0400"),
):
    pass


def get_client(id=None, y_clients_id=None, session=None):
    if session is None:
        session = __make_session()
    filter = list()
    if not (id is None):
        filter.append(Client.id == id)
    else:
        filter.append(Client.user_id_in_yclients == y_clients_id)

    client = session.query(Client).filter(*filter).first()
    return client


def get_clients():
    global CLIENTS
    session = __make_session()
    filter = list()

    clients = session.query(Client).all()
    for client in clients:
        CLIENTS[client.user_id_in_yclients] = client.id
