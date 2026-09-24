import json

result = 9.0
names = [ 'John', 'Frank' ]
results = [
    {
        'name' : 'John',
        'result' : 4.0
    },
    {
        'name' : 'Frank',
        'result' : 7.0
    }
]
with open('result.json', 'w') as json_file:
    json.dump(result, json_file)

with open('names.json', 'w') as json_file:
    json.dump(names, json_file)

with open('results.json', 'w') as json_file:
    json.dump(results, json_file, indent=4)

