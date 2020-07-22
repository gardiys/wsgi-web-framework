# WSGI web-framework
Простой WSGI Web-фреймворк на базе uWSGI с использованием nginx.

## Установка
'''bash
sudo apt-get update
sudo apt-get install python-dev python-pip nginx
sudo pip install virtualenv
'''
#### Создание виртуального окружения
Перейдите в каталог с приложением, затем выполните следующий код
'''bash
virtualenv venv
source myappenv/bin/activate
'''
#### Установка uWSGI
'''bash
pip install uwsgi
'''
## Запуск сервера
'''bash
uwsgi --socket 0.0.0.0:8080 --protocol=http -w app
'''
