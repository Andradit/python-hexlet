"""В этом упражнении вы создадите простое веб-приложение, которое передает
текстовое сообщение. Это поможет познакомиться с Flask.

Чтобы посмотреть результаты работы приложения, используйте кнопку
«Web-доступ» в правой панели.

Реализуйте обработчик, который по адресу / отдает строчку Welcome to Hexlet!."""

from flask import Flask

app = Flask(__name__)


# BEGIN (write your solution here)
@app.route('/')
def hello_hexlet():
    return 'Welcome to Hexlet!'
# END