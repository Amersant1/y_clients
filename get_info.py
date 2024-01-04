from data_base import *
from utils import *
# dicti = dict()
# # for i in SERVICES_DICT_WITH_DATA.keys():
#     # service = SERVICES_DICT_WITH_DATA[i]
#     # # print(service)
#     # dicti[service["name"]] = 7
#     # print(service["name"],"\n")

# print(dicti)
# print(get_phone_calls())
# make_phone_calls_on_today()
print(*[ call.as_dict() for call in get_phone_calls()])
