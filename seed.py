from db import session
from models import (
    Student,
    Group,
    Teacher,
    Subject,
    Grade,
)

from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)


start_date = datetime(2022, 1, 1)
end_date = datetime(2026, 12, 31)

students = [Student(name=fake.name()) for _ in range(50)]
session.add_all(students)
session.commit()

groups = [Group(name=f"Group {i+1}") for i in range(3)]
session.add_all(groups)
session.commit()

teachers = [Teacher(name=fake.name()) for _ in range(5)]
session.add_all(teachers)
session.commit()

subjects = [Subject(name=f"Subject {i+1}") for i in range(8)]
session.add_all(subjects)
session.commit()

for student in students:
    student_groups = random.sample(groups, random.randint(1, 3))
    for group in student_groups:
        if len(group.students) < 25:
            student.groups.append(group)
session.commit()

for teacher in teachers:
    teacher_subjects = random.sample(subjects, random.randint(1, 2))
    for subject in teacher_subjects:
        if len(subject.teachers) < 5:
            subject.teachers.append(teacher)
session.commit()

for student in students:
    for subject in subjects:
        for _ in range(random.randint(1, 20)):
            grade = Grade(
                student=student,
                subject=subject,
                grade=random.randint(60, 100),
                date_received=random_date(start_date, end_date),
            )
            session.add(grade)

session.commit()
session.close()