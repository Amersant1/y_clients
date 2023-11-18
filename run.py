# from controller import *
# from model import *
# import json
# from data_base import *
# from datetime import datetime
# # from bd_preparation.make_client import *
# # clients = json.loads(open("clients.json","r").read())

#     # print(json.dumps(clients),file=file)
# file = open("appointment.json","r")
# visits = json.loads(file.read())
# # file = open("appointment_but_only_one.json","w")
# # print(json.dumps(clients[0:100]),file=file)
# # file.close()
# # visits = api.get_visits_for_client(clients[0])
# session = sessionmaker(engine)()
# i=0
# for visit in visits:
#     i+=1
#     if i%1000==0:
#         print(i)
#         session.commit()
#         session =sessionmaker(engine)()
#     # req = api.get_visits_for_client(clients[0])
#     # visits = req["services"]
#     id = visit["id"] 
#     # name = visit["name"]
#     staff = visit["staff"]
#     staff_id = staff["id"]
#     staff_name = staff["name"]
#     staff_specialization = staff["specialization"]
#     client = visit["client"]
#     if client == None:
#         continue
#     services = visit["services"]
#     if len(services)==0:
#         continue
#     if "id" in client:
#         client_id = client["id"]
#     else:
#         client_id = None
#     datetime_of_visit=visit["date"]
#     datetime_of_visit=datetime.strptime(datetime_of_visit,"%Y-%m-%d %H:%M:%S")

#     staff_id=make_staff_member(specialization=staff_specialization,y_clients_id=staff_id,name=staff_name,session=session)

    
#     new_services = list()
#     price = int()
#     for service in services:
        
#         dicti = dict()
#         dicti["y_clients_id"] = service["id"]
#         dicti["name"] = service["title"]
#         dicti["price"] = service["cost"]
#         price+=dicti["price"]
#         dicti["discount"] = service["discount"]

#         for j in range(service["amount"]):
#             new_services.append(dicti)

#         service_id = add_service(name= dicti["name"],y_clients_id=dicti["y_clients_id"],now_day_price=dicti["price"],session=session)
#     appointment=make_appointment(
#                     y_clients_id=id,
#                     client_id=client_id,
#                     staff_id=staff_id,
#                     services=new_services,
#                     price=price,
#                     datetime_of_appointment=datetime_of_visit,
#                     session=session)
    
# session.commit()