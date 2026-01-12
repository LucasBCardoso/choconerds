#IMPORTS
import dash
from dash import html, dcc, callback
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash.exceptions import PreventUpdate

from flask import Flask, render_template, url_for, redirect, request, make_response
#from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session

import psycopg2
from psycopg2 import connect

import os
import pandas as pd
from werkzeug.security import generate_password_hash, check_password_hash

global carrinho
carrinho = []

#INICIO DO APP
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LITERA] + dmc.styles.ALL)
server = app.server
server.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///local.db')

#SESSÃO DE USUARIO
server.config['SESSION_TYPE'] = 'filesystem'
server.config['SESSION_FILE_DIR'] = '/tmp/flask_session'
server.config['SESSION_COOKIE_NAME'] = 'my-session'
server.config['PERMANENT_SESSION_LIFETIME'] = 365 * 24 * 60 * 60 * 10  # 10 years

server.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', os.urandom(12))
app.config.suppress_callback_exceptions = True #True
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

session = Session(server)
db = SQLAlchemy(server)

#TITULO DO APLICATIVO
app.title = 'Choco Nerds!'

#CONEXÃO COM A BASE DE DADOS
# conn = psycopg2.connect(
#     host=host,
#     port=port,
#     dbname=dbname,
#     user=user,
#     password=password
# )
# c = conn.cursor()

# #========= CADASTRO DE USUÁRIOS
# class Users(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     nome = db.Column(db.String(200))
#     username = db.Column(db.String(100), unique=True, nullable=False)
#     email = db.Column(db.String(250))
#     password = db.Column(db.String(350))
#     telefone = db.Column(db.Integer)
#     cpf = db.Column(db.Integer)
#     endereco = db.Column(db.String(500))
#     vencimento = db.Column(db.Integer)
#     status = db.Column(db.String(100))
#     ativo = db.Column(db.String(100))
#     agendamento = db.Column(db.String(100))
#     sentimento = db.Column(db.String(100))
#     datacadastro = db.Column(db.Date)
#     atividade = db.Column(db.String(100))

# #========= HISTÓRICO GERAL DE TREINOS
# class historico(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     data = db.Column(db.Date)
#     selection = db.Column(db.String(50))
#     sentimento = db.Column(db.String(50))
#     username = db.Column(db.String(300))

# #========= TREINOS DO DIA E PRÉ AGENDADOS
# class agendados(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     data = db.Column(db.Date)
#     selection = db.Column(db.String(50))
#     username = db.Column(db.String(300), unique=True, nullable=False)

# #========= HORÁRIOS E TREINOS
# class treinos(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     atividade = db.Column(db.String(100))
#     diadasemana = db.Column(db.String(50))
#     horario = db.Column(db.String(50))
#     ativo = db.Column(db.String(50))

# #========= DADOS DA EMPRESA
# class empresa(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nome = db.Column(db.String(150))
#     email = db.Column(db.String(200))
#     password = db.Column(db.String(350))
#     telefone = db.Column(db.Integer)
#     cpf = db.Column(db.Integer, unique=True, nullable=False)
#     empresa = db.Column(db.String(300), unique=True, nullable=False)
#     cnpj = db.Column(db.Integer)
#     endereco = db.Column(db.String(500))
#     vencimento = db.Column(db.Integer)
#     ativo = db.Column(db.String(100))

