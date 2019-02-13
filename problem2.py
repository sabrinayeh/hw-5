Ron_Swanson = {
	"name": "Ron Swanson",
    "age": 55,
    "department": "Management",
    "phone": "555-1234",
    "salary": "$87,000"
    }

Leslie_Knope = {
	"name": "Leslie Knope",
    "age": 44,
    "department": "Middle Management",
    "phone": "555-4321",
    "salary": "$76,000"
	}

Andy_Dwyer = {
	"name": "Andy Dwyer",
    "age": 33,
    "department": "Shoe Shining",
    "phone": "555-1122",
    "salary": "$65,000"
	}

April_Ludgate = {
	"name": "April Ludgate",
    "age": 22,
    "department": "Administration",
    "phone": "555-3345",
    "salary": "$54,000"
	}


employees = [Ron_Swanson, Leslie_Knope, Andy_Dwyer, April_Ludgate]

for index in range(len(employees)):
		print(employees[index]["name"], "in", employees[index]["department"], "can be reached at", employees[index]["phone"] + ".")

"""

Ron Swanson in Management can be reached at 555-1234.
Leslie Knope in Middle Management can be reached at 555-4321.
Andy Dwyer in Shoe Shining can be reached at 555-1122.
April Ludgate in Administration can be reached at 555-3345.

"""