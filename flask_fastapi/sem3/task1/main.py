import random

from flask import Flask, render_template
from task1.models import db, Faculty, Student
from random import randint


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("fill-db")
def fill_tables():
    count = 10
    for student in range(1, count + 1):
        new_student = Student(
            name=f'name{student}',
            surname=f'surname{student}',
            age=randint(18, 25),
            gender=random.choice(['male', 'female']),
            group=randint(2003, 2025),
            faculty=randint(1, 3)
        )
        db.session.add(new_student)
    db.session.commit()
    for faculty in range(1, 4):
        new_faculty = Faculty(fac_name=f'faculty{faculty}')
        db.session.add(new_faculty)
    db.session.commit()
    print('OK')


@app.route('/')
def hi():
    return 'Hello'


@app.route('/students/')
def students_info():
    students = Student.query.all()
    return render_template('students.html', students=students)


if __name__ == '__main__':
    app.run(debug=True)

