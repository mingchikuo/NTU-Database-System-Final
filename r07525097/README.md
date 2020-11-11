# Flask REST demo

# 開發環境win10

# 進 MySQL Shell 

CREATE DATABASE `demo`;

drop database demo;

# CMD CD進r07525097資料夾，以下依序執行後，即可跑POSTMAN

set FLASK_APP=restdemo:create_app()

flask db init

flask db migrate

flask db upgrade

flask run

需求：
alembic==1.0.8
aniso8601==6.0.0
Click==7.0
Flask==1.0.2
Flask-JWT==0.3.2
Flask-Migrate==2.4.0
Flask-RESTful==0.3.7
Flask-SQLAlchemy==2.3.2
itsdangerous==1.1.0
Jinja2==2.10
Mako==1.0.8
MarkupSafe==1.1.1
PyJWT==1.4.2
PyMySQL==0.9.3
python-dateutil==2.8.0
python-editor==1.0.4
pytz==2018.9
six==1.12.0
SQLAlchemy==1.3.1
Werkzeug==0.15.1