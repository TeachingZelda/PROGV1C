import json
with open('employees.json', 'r') as json_file:
    data = json.load(json_file)
    employees = data["employees"]

    for employee in employees:
        print(employee['lastName'])

