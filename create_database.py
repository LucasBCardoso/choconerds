'''
from sqlalchemy import Table, create_engine
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os

from app import *

engine = create_engine(os.environ.get('DATABASE_URL', 'sqlite:///local.db'))

# Create a connection to the database
conn = engine.connect()


#========= USUÁRIOS
class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nomeCompleto = db.Column(db.String(100))
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120))
    password = db.Column(db.String(300))
    telefone = db.Column(db.Integer)
    vencimento = db.Column(db.Integer)
    status = db.Column(db.String(50))
    ativo = db.Column(db.String(30))
    agendamento = db.Column(db.String(40))
    sentimento = db.Column(db.String(60))

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self): 
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

Users_tbl = Table('users', Users.metadata, extend_existing=True)

def create_users_table():
    Users.metadata.create_all(engine)
create_users_table()

#========= TREINOS DO DIA
class treinos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date)
    selection = db.Column(db.String(25))
    username = db.Column(db.String(30))

treino_tbl = Table('treinos', treinos.metadata, extend_existing=True)

def create_treinos_table():
    treinos.metadata.create_all(engine)
create_treinos_table()

#========= HISTÓRICO DE TREINOS
class historico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date)
    selection = db.Column(db.String(25))
    sentimento = db.Column(db.String(40))
    username = db.Column(db.String(30))


historico_tbl = Table('historico', historico.metadata, extend_existing=True)

def create_historico_table():
    historico.metadata.create_all(engine)
create_historico_table()

#========= TREINOS AGENDADOS
class agendados(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date)
    selection = db.Column(db.String(25))
    username = db.Column(db.String(30), unique=True, nullable=False)

agendados_tbl = Table('agendados', agendados.metadata, extend_existing=True)

def create_agendados_table():
    agendados.metadata.create_all(engine)
create_agendados_table()

#========= LEITURA DE DBs

#USUÁRIOS
import pandas as pd
c = conn.cursor()
df = pd.read_sql('select * from users', conn)
df

#TREINOS CANCELADOS
import pandas as pd
c = conn.cursor()
df = pd.read_sql('select * from treinos', conn)
df

#HISTÓRICO GERAL
import pandas as pd
c = conn.cursor()
df = pd.read_sql('select * from historico', conn)
df

#SISTEMA DE AGENDAMENTOS
import pandas as pd
c = conn.cursor()
df = pd.read_sql('select * from agendados', conn)
df
'''