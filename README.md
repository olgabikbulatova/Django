# учебные проекты GeekBrains
## Django: 
* реализован сайт с основными блоками: игры, статьи, интернет магазин с БД. 
## Flask:
* Создать страницу, на которой будет форма для ввода имени и электронной почты При отправке которой будет создан cookie файл с данными пользователя Также будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя.На странице приветствия должна быть кнопка "Выйти"При нажатии на кнопку будет удален cookie файл с данными пользователя и произведено перенаправление на страницуввода имени и электронной почты.
* базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал), и дочерние шаблоны для страниц категорий товаров и отдельных товаров. Например, создать страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон.
* базу данных для интернет-магазина. База данных должна состоять из трёх таблиц: товары, заказы и пользователи.Создайте модели pydantic для получения новых данных и возврата существующих в БД для каждой из трёх таблиц. Реализуйте CRUD операции для каждой из таблиц через создание маршрутов, REST API.
* Необходимо создать API для управления списком пользователей.Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа.Для этого использовать библиотеку Pydantic.Создайте HTML шаблон для отображения списка пользователей.Шаблон должен содержать заголовок страницы, таблицу со списком пользователей и кнопку для добавления нового пользователя.
## Pytest: 
* для проекта по работе с пользователями (имя, id, уровень) тесты pytest с использованием фикстур 