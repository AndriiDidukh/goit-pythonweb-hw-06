from datetime import datetime, timedelta
import random

from faker import Faker

from db import session
from models import Student, Group, Teacher, Subject, Grade


fake = Faker()

START_DATE = datetime(2022, 1, 1)
END_DATE = datetime(2026, 12, 31)


def random_date(start_date, end_date):
    delta = end_date - start_date
    return start_date + timedelta(days=random.randint(0, delta.days))

groups = [
    Group(name=f"Group {i}")
    for i in range(1, 4)
]

session.add_all(groups)
session.commit()

teachers = [
    Teacher(name=fake.name())
    for _ in range(5)
]

session.add_all(teachers)
session.commit()

subjects = []

for i in range(1, 9):
    subject = Subject(
        name=f"Subject {i}",
        teacher=random.choice(teachers),
    )
    subjects.append(subject)

session.add_all(subjects)
session.commit()

students = []

for _ in range(50):
    student = Student(
        name=fake.name(),
        group=random.choice(groups),
    )
    students.append(student)

session.add_all(students)
session.commit()

grades = []

for student in students:
    grades_count = random.randint(1, 20)

    for _ in range(grades_count):
        subject = random.choice(subjects)
        grades.append(
            Grade(
                student=student,
                subject=subject,
                grade=random.randint(60, 100),
                date_received=random_date(
                    START_DATE,
                    END_DATE,
                ),
            )
        )

session.add_all(grades)
session.commit()
session.close()