import requests
from controller import *


def test():
    js = {"login": "79031250586", "password": "Anna24070509%%"}
    # req=requests.get(f"https://api.yclients.com/api/v1/records/{company_id}",headers=HEADERS)
    # req=requests.post('https://api.yclients.com/api/v1/auth',headers=HEADERS,json=js)
    # req=requests.get(f'https://api.yclients.com/api/v1/company/{company_id}/users/roles',headers=HEADERS)
    req = requests.post(f"https://x/api/v1/records/{company_id}", headers=HEADERS)
    print(
        req.content.decode("utf-8"),
    )


# test()

# if __name__=="__main__":
# req=requests.post(f'https://x/api/v2/records/{company_id}',headers=HEADERS)
# print(req.content.decode("utf-8"),)
