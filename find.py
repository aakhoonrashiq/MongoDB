from config import students

student = students.find_one(
    {"name": "Rashiq"}
)

print(student)