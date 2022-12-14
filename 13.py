import json

f = open('C:/Users/dvvvn/Desktop/labs/data.json')
data = json.load(f)
needed_category = 'datepicker'

clients_and_count = {}
for i in data['events_data']:
    if i['category'] == needed_category:
        if i['client_id'] in clients_and_count.keys():
            clients_and_count[i['client_id']] += 1
else:
    clients_and_count[i['client_id']] = 1

print(max(clients_and_count, key=clients_and_count.get))