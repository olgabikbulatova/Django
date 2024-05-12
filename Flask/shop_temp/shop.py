# Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
# Например, создать страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон.

from flask import Flask, render_template

app = Flask(__name__)
text = 'привет это мой первый интернет-магазин'
clothes = [
    {'name': 'пальто', 'text': 'блаблабла', 'price': '1280', 'img': 'https://st34.stblizko.ru/images/news/001/357/686_original.jpg'},
    {'name': 'куртка', 'text': 'блаблабла', 'price': '5000', 'img': 'http://images.prom.ua/1935217212_w640_h640_kurtka-muzhskaya-osennyaya.jpg'},
    {'name': 'джинсы', 'text': 'блаблабла', 'price': '3000', 'img': 'https://almode.ru/uploads/posts/2021-03/1616576976_8-p-stilnie-dzhinsi-boifrendi-8.jpg'},
    {'name': 'футболка', 'text': 'блаблабла', 'price': '1500', 'img': 'https://avatars.mds.yandex.net/get-mpic/4291905/img_id6457370401666591128.jpeg/orig'}]
shoes = [
    {'name': 'туфли', 'text': 'блаблабла', 'price': '1280', 'img': 'https://a.1stdibscdn.com/archivesE/upload/1121189/v_33955331508743310735/3395533_master.jpg?width=768'},
    {'name': 'сапоги', 'text': 'блаблабла', 'price': '5000', 'img': 'https://www.huntinggeardeals.com/wp-content/uploads/2019/03/Guide-Gear-Mens-Ankle-Fit-Insulated-Rubber-Boots-2400-gram-768x768.jpg'},
    {'name': 'кроссовки', 'text': 'блаблабла', 'price': '3000', 'img': 'https://www.modnyi-shop.ru/wp-content/uploads/2021/09/premiata-chernye-kombinirovannye-muzhskie-krossovki-bolshie-razmery-52-768x768.jpg'},
]


@app.route('/')
def get_main():
    return render_template('main.html')


@app.route('/clothes/')
def get_clothes():
    return render_template('clothes.html', clothes=clothes)


@app.route('/clothes/jeans1/')
def get_jeans():
    return render_template('jeans1.html', clothes=clothes)


@app.route('/shoes/')
def get_shoes():
    return render_template('shoes.html', shoes=shoes)


if __name__ == '__main__':
    app.run(debug=True)