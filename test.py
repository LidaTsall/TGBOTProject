import json

with open("tovar_dict.json") as file:
    new_list = json.load(file)

search_id = '10335'

if search_id in new_list:
    print('Уже есть')
else:
    print('Что-то новое!!')