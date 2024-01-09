### How to install
- Run : pip install -r requirement.txt
- Setup postgre database in .env
- Edit file alembic.ini, change code : sqlalchemy.url = postgresql://{databaseUsername}:{databasePassword}@{databaseHost}:{databasePort}/{databaseName}
- Run : yarn migrate , in order to migrate table and seed data

### How to run
- Run : python index.py
- API can be accesed through http://localhost:5000 

### User example

Email     : root@gmail.com
Password  : 12345678  

Email     : admin@gmail.com
Password  : 12345678  

Email     : master@gmail.com
Password  : 12345678  

### Packages

PyJWT==2.8.0
flask
selenium
flask_sqlalchemy
flask-cors
alembic
psycopg2
bcrypt
aoiklivereload
python-dotenv
sanic_cors
uvicorn
datetime
requests
google-auth

### Environment configuraion
Edit .env in order to adjust some configuration. For database configuration, adjust it with your postgre server and database.

- DB_NAME : database name
- DB_USER : database username
- DB_PASSWORD : database password
- DB_HOST : database host
- DB_PORT : database port
- SELENIUM_ENVIRONMENT : If development, selenium will run visually in Windows. If production, selenium will run headless. (value = production / development)
- GOOGLE_CLIENT_ID : Google Client ID