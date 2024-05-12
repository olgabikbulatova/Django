# Создать базу данных для хранения информации о студентах университета.
# База данных должна содержать две таблицы: "Студенты" и "Факультеты".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия,
# возраст, пол, группа и id факультета.
# В таблице "Факультеты" должны быть следующие поля: id и название
# факультета.
# Необходимо создать связь между таблицами "Студенты" и "Факультеты".
# Написать функцию-обработчик, которая будет выводить список всех
# студентов с указанием их факультета.

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fac_name = db.Column(db.String(120), unique=True, nullable=False)
    students = db.Relationship('Student', backref='faculty.id', lazy=True)

    def __repr__(self):
        return f'Faculty ({self.faculty_name})'


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    surname = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Enum('male', 'female'), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    faculty = db.Column(db.ForeignKey('faculty.id'))

    def __repr__(self):
        return f'Student (name {self.name}, surname {self.surname}, age {self.age}, faculty {self.faculty})'


