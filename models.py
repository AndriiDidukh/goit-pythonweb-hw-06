from datetime import date
from sqlalchemy import (
    String,
    Integer,
    Date,
    ForeignKey,
    Column,
    Table,
    PrimaryKeyConstraint,
)
from sqlalchemy.orm import DeclarativeBase, relationship, mapped_column, Mapped


class Base(DeclarativeBase):
    pass


association_student_group_table = Table(
    "association_student_group",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id", ondelete="CASCADE")),
    Column("group_id", Integer, ForeignKey("groups.id", ondelete="CASCADE")),
    PrimaryKeyConstraint("student_id", "group_id"),
)

association_teacher_subject_table = Table(
    "association_teacher_subject",
    Base.metadata,
    Column("teacher_id", Integer, ForeignKey("teachers.id", ondelete="CASCADE")),
    Column("subject_id", Integer, ForeignKey("subjects.id", ondelete="CASCADE")),
    PrimaryKeyConstraint("teacher_id", "subject_id"),
)


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    groups: Mapped[list["Group"]] = relationship(
        "Group",
        secondary=association_student_group_table,
        back_populates="students",
    )
    grades: Mapped[list["Grade"]] = relationship("Grade", back_populates="student")


class Group(Base):
    __tablename__ = "groups"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    students: Mapped[list["Student"]] = relationship(
        "Student",
        secondary=association_student_group_table,
        back_populates="groups",
    )


class Teacher(Base):
    __tablename__ = "teachers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    subjects: Mapped[list["Subject"]] = relationship(
        "Subject",
        secondary=association_teacher_subject_table,
        back_populates="teachers",
    )


class Subject(Base):
    __tablename__ = "subjects"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    teachers: Mapped[list["Teacher"]] = relationship(
        "Teacher",
        secondary=association_teacher_subject_table,
        back_populates="subjects",
    )
    grades: Mapped[list["Grade"]] = relationship("Grade", back_populates="subject")


class Grade(Base):
    __tablename__ = "grades"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"), nullable=False)
    subject_id: Mapped[int] = mapped_column(ForeignKey("subjects.id"), nullable=False)
    grade: Mapped[int] = mapped_column(Integer, nullable=False)
    date_received: Mapped[date] = mapped_column(Date, nullable=False)
    student: Mapped["Student"] = relationship("Student", back_populates="grades")
    subject: Mapped["Subject"] = relationship("Subject", back_populates="grades")
