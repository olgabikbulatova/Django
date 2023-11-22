# Создать страницу, на которой будет кнопка "Нажми меня", при
# нажатии на которую будет переход на другую страницу с
# приветствием пользователя по имени.
from pathlib import PurePath, Path

# на которой будет изображение и ссылка на другую страницу,
# на которой будет отображаться форма
# для загрузки изображений.

from flask import Flask, render_template, request, flash, redirect, url_for, abort
from werkzeug.utils import secure_filename
import secrets


app = Flask(__name__)
app.secret_key = 'c8db7e4d1c3d4c2fd943b99d32fb690dea5497c4a2088364697741b41185ac72'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello/')
def hello():
    return 'привет!'


@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads',file_name))
        return f"Файл {file_name} загружен на сервер"
    return render_template('upload.html')


# Создать страницу, на которой будет форма для ввода логина и пароля
# При нажатии на кнопку "Отправить" будет произведена проверка соответствия логина и пароля и переход на
# страницу приветствия пользователя или страницу с ошибкой
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        if login == 'olga' and password == '123':
            return f'hello {login}'
        return """
        <h1> wrong name or password, try again </h1>
        <p> 
            <a href="/login/"> ссылка на страницу login </a>
        </p>
        <p> 
            <a href="/"> ссылка на index </a>
        </p>
        """
    return render_template('reg.html')

# Создать страницу, на которой будет форма для ввода текста и
# кнопка "Отправить"
# При нажатии кнопки будет произведен подсчет количества слов
# в тексте и переход на страницу с результатом.


@app.route('/text/', methods=['GET', 'POST'])
def text():
    if request.method == 'POST':
        text = request.form.get('text')
        return f'text lenght = {len(text)}'
    return render_template('text.html')


# Создать страницу, на которой будет форма для ввода двух
# чисел и выбор операции (сложение, вычитание, умножение
# или деление) и кнопка "Вычислить"
# При нажатии на кнопку будет произведено вычисление
# результата выбранной операции и переход на страницу с
# результатом.
@app.route('/calc/', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        num1 = int(request.form.get('num1'))
        num2 = int(request.form.get('num2'))
        action = request.form.get('action')
        if action == '+':
            return f'{num1} + {num2} = {num2+num1}'
        elif action == '*':
            return f'{num1} * {num2} = {num2*num1}'
        if action == '-':
            return f'{num1} - {num2} = {num2-num1}'
        else:
            return f'{num1} / {num2} = {num2 / num1}'
    return render_template('calc.html')


# Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка
# возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.
@app.errorhandler(403)
def age_error(e):
    return 'no ENTRY, your are too young', 403


@app.route('/age/', methods=['GET', 'POST'])
def age():
    if request.method == 'POST':
        name = request.form.get('name')
        age = int(request.form.get('age'))
        if age >= 18:
            return f'welcome to site'
        abort(403)
    return render_template('age.html')

# Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.


@app.route('/qwadro/', methods=['GET', 'POST'])
def qwadro():
    if request.method == 'POST':
        num1 = int(request.form.get('num1'))
        return redirect(url_for('result', number=num1 ** 2))
    return render_template('qwadro.html')


@app.route('/result/<int:number>/')
def result(number):
    return f"sdfsafasdf {number}"


# Создать страницу, на которой будет форма для ввода имени
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!".

@app.route('/name/', methods=['GET', 'POST'])
def name():
    if request.method == 'POST':
        name = request.form.get('name')
        flash(f'hello, {name}', 'success')
        return redirect(url_for('name'))
    return render_template('name.html')


if __name__ == '__main__':
    app.run(debug=True)

