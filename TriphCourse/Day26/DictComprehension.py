import random

notes = ['Hello', 'there', 'how', 'are', 'you']
student_results = {student: random.randint(20, 100) for student in notes}

passed = {student: score for (student, score) in student_results.items() if score >= 60}
print(passed)

print(student_results)

for (key, value) in student_results.items():
    print(value)

