from controller import *
from model import *
import json
# from data_explorer import *
# print(clients[0],"\n\n\n\n")
from datetime import datetime
# if __name__=="__main__":
# file = open("clients.json","w")
# clients=api.get_clients_data(clients_per_page=200,)

# print(json.dumps(clients),file=file)
file = open("clients.json","r")

clients = json.loads(file.read())
for client in clients:
    birth_day = client["birth_date"]
    if birth_day!=str():
        birth_day = datetime.strptime(birth_day,"%Y-%m-%d")
    else:
        birth_day = datetime(year=1970,month=1,day=1)
    try: 
        last_change_date =datetime.strptime(client["last_change_date"],"%Y-%m-%dT%H:%M:%S%z")
    except:
        pass
    bd_client = Client(
        user_id_in_yclients=client["id"],
        name=client["name"],
        surname=client["surname"],
        patronymic = client["patronymic"],
        display_name = client["display_name"],
        phone = client["phone"],
        paid = 0,
        birth_date = birth_day,
        last_change_date=last_change_date,
        sex=int(client["sex_id"])
        )
    Session.add(bd_client)
Session.commit()

# print(api.get_visits_data_for_clients_list(clients[0:5]))


