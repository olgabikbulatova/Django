# Написать функцию, которая будет выводить на экран HTML
# страницу с блоками новостей.
# Каждый блок должен содержать заголовок новости,
# краткое описание и дату публикации.
# Данные о новостях должны быть переданы в шаблон через
# контекст.

from flask import Flask, render_template


app = Flask(__name__)

news = [
    {'head': 'dfskfsf', 'shortcut': 'sdfsds sdfsfsdf sdfsdfsfd', 'publish_date': '18-10-2023'},
    {'head': 'dfskfsf', 'shortcut': 'sdfsds sdfsfsdf sdfsdfsfd', 'publish_date': '19-10-2023'},
    {'head': 'dfskfsf', 'shortcut': 'sdfsds sdfsfsdf sdfsdfsfd', 'publish_date': '20-10-2023'},
    {'head': 'dfskfsf', 'shortcut': 'sdfsds sdfsfsdf sdfsdfsfd', 'publish_date': '21-10-2023'}
]


@app.route('/news/')
def get_news():
    return render_template('news.html', news=news)


if __name__ == '__main__':
    app.run(debug=True)