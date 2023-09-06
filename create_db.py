import os
from sqlalchemy import Table, create_engine
from sqlalchemy.sql import select
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

cwd = os.path.dirname(os.path.realpath(__file__))
os.chdir(cwd)

conn = sqlite3.connect('data.sqlite') # se conecta ao banco de dados
engine = create_engine('sqlite:///data.sqlite') # mantem a conexão ativa
db = SQLAlchemy() # cria uma instância do DB

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable = False)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(88))

Users_tbl = Table('users', Users.metadata)

#fuction to create table using Users class
def create_users_table():
    Users.metadata.create_all(engine)
create_users_table()



# ========== TEST ========== #
# import sqlite3
# import pandas as pd
# conn = sqlite3.connect('data.sqlite')
# c = conn.cursor()
# df = pd.read_sql('SELECT * FROM users', conn)
# df