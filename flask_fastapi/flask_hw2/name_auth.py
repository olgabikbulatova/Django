# ++Создать страницу, на которой будет форма для ввода имени и электронной почты
# ++При отправке которой будет создан cookie файл с данными пользователя
# ++Также будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя.
# ++На странице приветствия должна быть кнопка "Выйти"
# ++При нажатии на кнопку будет удален cookie файл с данными пользователя и произведено перенаправление на страницу
# ввода имени и электронной почты.

from flask import Flask, request, redirect, url_for, render_template, make_response

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        response = make_response(redirect(url_for('hello', name=name)))
        response.set_cookie('username', name)
        response.set_cookie('useremail', email)
        return response
    return render_template('index.html')


@app.route('/hello/<string:name>', methods=['GET', 'POST'])
def hello(name):
    if request.method == 'POST':
        response = make_response(redirect(url_for('login')))
        response.delete_cookie('username')
        response.delete_cookie('useremail')
        return response
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)

