import json

with open('employees.json', 'r') as json_file:
    data = json.load(json_file)
    # print(data)
    employees = data["employees"]
    print(employees)
    print(employees[0])


    # for employee in employees:
    #     print(employee['lastName'])

