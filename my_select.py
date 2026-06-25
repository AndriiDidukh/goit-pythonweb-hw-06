from db import session
from sqlalchemy.sql import func
from models import Student, Group, Subject, Grade

def select_1():
    return (
        session.query(Student)
        .join(Grade)
        .group_by(Student.id)
        .order_by(func.avg(Grade.grade).desc())
        .limit(5)
        .all()
    )

def select_2(subject_id: int):
    return (
        session.query(Student)
        .join(Grade)
        .filter(Grade.subject_id == subject_id)
        .group_by(Student.id)
        .order_by(func.avg(Grade.grade).desc())
        .first()
    )

def select_3(subject_id: int):
    return (
        session.query(Group.name, func.avg(Grade.grade))
        .join(Student, Student.group_id == Group.id)
        .join(Grade, Grade.student_id == Student.id)
        .filter(Grade.subject_id == subject_id)
        .group_by(Group.name)
        .all()
    )

def select_4():
    return session.query(func.avg(Grade.grade)).scalar()

def select_5(teacher_id: int):
    return (
        session.query(Subject.name)
        .filter(Subject.teacher_id == teacher_id)
        .all()
    )

def select_6(group_id: int):
    return (
        session.query(Student.name)
        .filter(Student.group_id == group_id)
        .all()
    )

def select_7(group_id: int, subject_id: int):
    return (
        session.query(Student.name, Grade.grade)
        .join(Grade)
        .filter(
            Student.group_id == group_id,
            Grade.subject_id == subject_id,
        )
        .all()
    )

def select_8(teacher_id: int):
    return (
        session.query(func.avg(Grade.grade))
        .join(Subject, Grade.subject_id == Subject.id)
        .filter(Subject.teacher_id == teacher_id)
        .scalar()
    )

def select_9(student_id: int):
    return (
        session.query(Subject)
        .join(Grade)
        .filter(Grade.student_id == student_id)
        .distinct()
        .all()
    )

def select_10(student_id: int, teacher_id: int):
    return (
        session.query(Subject)
        .join(Grade)
        .filter(
            Grade.student_id == student_id,
            Subject.teacher_id == teacher_id,
        )
        .distinct()
        .all()
    )