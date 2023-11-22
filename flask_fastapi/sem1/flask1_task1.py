# Напишите простое веб-приложение на Flask, которое будет
# выводить на экран текст "Hello, World!".

from flask import Flask

app = Flask(__name__)

# Написать функцию, которая будет выводить на экран HTML
# страницу с заголовком "Моя первая HTML страница" и
# абзацем "Привет, мир!".

html = """
    <h1> Моя первая HTML страница </h1>
    <p> Привет, мир!</p>
    """

@app.route('/')
def hello_world():
    return html


@app.route('/about/')
def about():
    return 'About'


@app.route('/contact/')
def Contact():
    return 'Contact'


# Написать функцию, которая будет принимать на вход два числа и выводить на экран их сумму.
@app.route('/number/<int:a><int:b>/')
def set_number(a,b):
    return f'Передано числа {a} и {b}, их сумма равна {a+b} '


# Написать функцию, которая будет принимать на вход строку и выводить на экран ее длину.
@app.route('/str/<string:word>/')
def len_text(word):
    return f'длина текста {len(word)}'

if __name__ == '__main__':
    app.run(debug=True)


