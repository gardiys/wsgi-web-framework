# WSGI web-framework
Простой WSGI Web-фреймворк на базе uWSGI с использованием nginx.

## Установка
> Примечание: uWSGI работает только под дистрибутивами Linux.
```bash
sudo apt-get update
sudo apt-get install python-dev python-pip nginx
sudo pip install virtualenv
```
#### Создание виртуального окружения
Перейдите в каталог с приложением, затем выполните следующий код
```bash
virtualenv venv
source venv/bin/activate
```
#### Установка uWSGI и сторонней библиотеки Webob для формирования запросов и ответов
```bash
pip3 install uwsgi
pip3 install webob
```
## Запуск сервера
```bash
uwsgi --socket 0.0.0.0:8080 --protocol=http -w app
```
## Пример использования
В файле *app.py* реализован основной функционал приложения.
Весь программный код должени быть реализован внутри функции *application* (так работает *uwgi*).
```python
def application(environ, start_response):
    app = WebFramework()

    @app.route("/")
    def main_page(request, response):
        with open(r"views/index.html", "r") as f:
            response.text = f.read()

    @app.route("/info")
    def info_page(request, response):
        with open(r"views/info.html", "r") as f:
             response.text = f.read()

    return app(environ, start_response)
```
Функция *application* обязательно должна возвращать итератор, для корректной работы сервера.
## License
[MIT](https://choosealicense.com/licenses/mit/)
