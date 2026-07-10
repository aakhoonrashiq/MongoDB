from config import students

student = {
    "name": "Rashiq",
    "age": 20,
    "major": "Computer Science",
    "city": "Srinagar"
}

result = students.insert_one(student)

print("Inserted ID:", result.inserted_id)