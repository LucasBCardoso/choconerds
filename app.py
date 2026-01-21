#IMPORTS
import dash
from dash import html, dcc, callback
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash.exceptions import PreventUpdate

from flask import Flask, render_template, url_for, redirect, request, make_response

import os
import pandas as pd
import requests
import json

global carrinho
carrinho = []

#INICIO DO APP
app = dash.Dash(__name__, 
    external_stylesheets=[dbc.themes.LITERA] + dmc.styles.ALL,
    assets_folder='assets',
    suppress_callback_exceptions=True
)
server = app.server

# Configurar Flask para servir arquivos estáticos da pasta 'static'
from flask import send_from_directory

@server.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

server.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', os.urandom(12))

#TITULO DO APLICATIVO
app.title = 'Choco Nerds!'
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

