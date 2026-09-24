import json
with open('stations.json', 'r') as json_file:
    data = json.load(json_file)
print(data["payload"])

for item in data["payload"]:
    print(f'{item["namen"]["lang"]:<25}{item["code"]:<10}{item["stationType"]:<10}')

