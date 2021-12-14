friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}
friend_ages["Bob"] = 20

print(friend_ages["Adam"])
friend = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30}
]
print(friend[0])

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")