# Создайте форму регистрации пользователя с использованием Flask-WTF. Форма должна
# содержать следующие поля:
# ○ Имя пользователя (обязательное поле)
# ○ Электронная почта (обязательное поле, с валидацией на корректность ввода email)
# ○ Пароль (обязательное поле, с валидацией на минимальную длину пароля)
# ○ Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
# После отправки формы данные должны сохраняться в базе данных (можно использовать SQLite)
# и выводиться сообщение об успешной регистрации. Если какое-то из обязательных полей не
# заполнено или данные не прошли валидацию, то должно выводиться соответствующее
# сообщение об ошибке.
# Дополнительно: добавьте проверку на уникальность имени пользователя и электронной почты в
# базе данных. Если такой пользователь уже зарегистрирован, то должно выводиться сообщение
# об ошибке.


from flask import Flask, render_template, request, redirect, url_for

from Flask.sem3.task4.models import db, Users
from forms import RegForm
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)
app.config['SECRET_KEY'] = 'mysecret'
csrf = CSRFProtect(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.route('/')
def hi():
    return f'Hello'


@app.route('/reg/', methods=['GET', 'POST'])
def reg():
    form = RegForm()
    if request.method == 'POST' and form.validate():
        name = form.username.data
        surname = form.surname.data
        email = form.email.data
        password = form.password.data
        hash = generate_password_hash(password)

        user = Users(name=f'{name} {surname}', email=email, password=hash)
        db.session.add(user)
        db.session.commit()
        return 'Регистрация прошла успешно'
    return render_template('reg.html', form=form)





if __name__ == '__main__':
    app.run(debug=True)
