from datetime import date
from sqlalchemy import String, Integer, Date, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship, mapped_column, Mapped


class Base(DeclarativeBase):
    pass


class Group(Base):
    __tablename__ = "groups"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    students: Mapped[list["Student"]] = relationship(
        "Student",
        back_populates="group",
        cascade="all, delete-orphan",
    )

class Student(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    group_id: Mapped[int] = mapped_column(
        ForeignKey("groups.id", ondelete="CASCADE"),
        nullable=False,
    )
    group: Mapped["Group"] = relationship(
        "Group",
        back_populates="students",
    )
    grades: Mapped[list["Grade"]] = relationship(
        "Grade",
        back_populates="student",
        cascade="all, delete-orphan",
    )


class Teacher(Base):
    __tablename__ = "teachers"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    subjects: Mapped[list["Subject"]] = relationship(
        "Subject",
        back_populates="teacher",
        cascade="all, delete-orphan",
    )


class Subject(Base):
    __tablename__ = "subjects"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    teacher_id: Mapped[int] = mapped_column(
        ForeignKey("teachers.id", ondelete="CASCADE"),
        nullable=False,
    )
    teacher: Mapped["Teacher"] = relationship(
        "Teacher",
        back_populates="subjects",
    )
    grades: Mapped[list["Grade"]] = relationship(
        "Grade",
        back_populates="subject",
        cascade="all, delete-orphan",
    )


class Grade(Base):
    __tablename__ = "grades"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    student_id: Mapped[int] = mapped_column(
        ForeignKey("students.id"),
        nullable=False,
    )
    subject_id: Mapped[int] = mapped_column(
        ForeignKey("subjects.id"),
        nullable=False,
    )
    grade: Mapped[int] = mapped_column(Integer, nullable=False)
    date_received: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )
    student: Mapped["Student"] = relationship(
        "Student",
        back_populates="grades",
    )
    subject: Mapped["Subject"] = relationship(
        "Subject",
        back_populates="grades",
    )