# Написать функцию, которая будет выводить на экран HTML
# страницу с таблицей, содержащей информацию о студентах.
# Таблица должна содержать следующие поля: "Имя",
# "Фамилия", "Возраст", "Средний балл".
# Данные о студентах должны быть переданы в шаблон через
# контекст.

from flask import Flask, render_template


app = Flask(__name__)

students = [
    {'name': 'Mike', 'second_name': 'Morrison', 'age': 18, 'av_score': 4.5},
    {'name': 'Olga', 'second_name': 'Morrison', 'age': 22, 'av_score': 3.2},
    {'name': 'Olga3', 'second_name': 'Morrison', 'age': 22, 'av_score': 3.2}
]


@app.route('/students/')
def get_stud():
    return render_template('students.html', students=students)


if __name__ == '__main__':
    app.run(debug=True)

