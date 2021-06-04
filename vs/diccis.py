import json

users = [
    {"user": "juan", "active": True, "quota": None},
    {"user": "ana", "active": False, "quota": 300},
]
print(json.dumps(users, indent=2))

nik = {
    "age": 32,
    "gender": "male",
    "employed": True,
}

print(nik.get("location"))

for d in users:
    print(d.get("user"))
