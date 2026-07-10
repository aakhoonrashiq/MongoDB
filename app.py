from pymongo import MongoClient

client = MongoClient()
db = client["college"]
students = db["students"]
student = {
    "name": "Ali",
    "age": 20,
    "city": "Delhi"
}

result = students.insert_one(student)

print(result.inserted_id)
