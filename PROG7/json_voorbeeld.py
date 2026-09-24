import json
employees = [ {"name" : "William", "lastName" : "Jones"},
              {"name" : "Anna", "lastName" : "Ford"},
              {"name" : "Peter", "lastName" : "Obama"}
            ]
print(type(employees))
employees = json.dumps(employees)
print(type(employees))
