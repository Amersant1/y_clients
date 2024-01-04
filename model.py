from controller import *

# from sqlalchemy import relation
from sqlalchemy.orm import relationship


class Staff(Base):
    """ПЕРСОНАЛ"""

    __tablename__ = "staff"
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    y_clients_id = Column(Integer)
    name = Column(String(200))

    # clients = relationship("Client", back_populates="staff", lazy="subquery")
    appointments = relationship("Appointment", back_populates="staff", lazy="subquery")
    profit = Column(Integer)
    type_of_service = Column(String(1000))


class Client(Base):
    """КЛИЕНТЫ"""

    __tablename__ = "clients"
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    # favorite_staff =
    user_id_in_yclients = Column(Integer)
    name = Column(String(200))
    surname = Column(String(200))
    patronymic = Column(String(200))
    display_name = Column(String(400))
    appointments = relationship("Appointment", back_populates="client", lazy="subquery")
    hash_id = Column(String(30))
    phone = Column(String(20))
    paid = Column(Integer)
    birth_date = Column(Date)
    last_change_date = Column(DateTime)
    sex = Column(SMALLINT)  # 0 - неизвестно, 1 - мужчина, 2 - женщина
    category_id = Column(Integer, ForeignKey("clients_categories.id"), nullable=True)
    category = relationship("ClientCategory", back_populates="clients", lazy="subquery")


class Appointment(Base):
    """ВИЗИТЫ КЛИЕНТОВ"""

    __tablename__ = "appointments"

    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    y_clients_id = Column(Integer)
    client_id = Column(Integer, ForeignKey("clients.id"))
    client = relationship("Client", back_populates="appointments", lazy="subquery")

    staff_id = Column(Integer, ForeignKey("staff.id"))
    staff = relationship("Staff", back_populates="appointments", lazy="subquery")

    services = relationship(
        "Appointment_Service", back_populates="appointment", lazy="subquery"
    )

    price = Column(Integer)
    is_paid = Column(Boolean)
    description = Column(String(300))
    datetime_of_appointment = Column(DateTime)

    def as_dict(self):
        dicti = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        services = list()
        for service in self.services:
            service_2 = service.service.as_dict()
            services.append(service_2)
        dicti["services"] = services
        return dicti


class Appointment_Service(Base):
    """УСЛУГИ, ОКАЗАННЫЕ ПРИ ВИЗИТЕ"""

    __tablename__ = "appointment_services"
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    service_id = Column(
        Integer,
        ForeignKey("services.id"),
        nullable=True,
    )
    service = relationship("Service", lazy="subquery")
    appointment_id = Column(
        Integer,
        ForeignKey("appointments.id"),
        nullable=True,
    )
    appointment = relationship(
        "Appointment", back_populates="services", lazy="subquery"
    )
    y_clients_id = Column(Integer)
    discount = Column(Integer)


# class PhoneCalls(Base):


class Service(Base):
    """ВСЕ УСЛУГИ"""

    __tablename__ = "services"
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    y_clients_id = Column(Integer)

    name = Column(String(400))

    description = Column(String(500))
    now_day_price = Column(Integer)
    now_day_profit = Column(Integer)
    marginality = Column(Float)
    category_id = Column(Integer, ForeignKey("service_categories.id"))
    category = relationship(
        "ServiceCategory", back_populates="services", lazy="subquery"
    )

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class ServiceCategory(Base):
    """КАТЕГОРИИ УСЛУГ"""

    __tablename__ = "service_categories"
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(30))
    description = Column(String(200))
    services = relationship("Service", back_populates="category", lazy="subquery")


class ClientCategory(Base):
    """КАТЕГОРИИ КЛИЕНТОВ"""

    __tablename__ = "clients_categories"
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(30))
    description = Column(String(200))
    clients = relationship("Client", back_populates="category", lazy="subquery")


class Call(Base):
    __tablename__="calls"
    id = Column(Integer, nullable=False, unique=True, primary_key=True)

    client_id = Column(Integer, ForeignKey("clients.id"))
    client = relationship("Client", lazy="subquery")
    call_date = Column(Date)
    service_id = Column(Integer, ForeignKey("services.id"))
    service = relationship("Service", lazy="subquery")
    number_of_calls = Column(Integer)
    is_answered = Column(Boolean)
    doesnt_need_to_call = Column(Boolean)
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
# Service.__table__.drop(engine)

Call.__table__.drop(engine)

# Appointment_Service.__table__.drop(engine)
# Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
