from flask import Flask

app = Flask(__name__)
app.secret_key = "namjunghyun117"

DATABASE = "books_db"