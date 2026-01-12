from dash import Dash, html, dcc, callback
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import dash
import sqlite3
from dash_iconify import DashIconify

from dash.exceptions import PreventUpdate

from app import *

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from flask import Flask, request,render_template
from flask_login import logout_user, current_user

from dash_bootstrap_templates import load_figure_template
load_figure_template(["litera"])

from datetime import date, datetime
hora = ""
numero_data = date.today().weekday() #data
dia_da_semana = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")
hoje = date.today()
#print(hoje)
dia = dia_da_semana[numero_data]
#dia = 'Sexta'

# created_at=datetime.utcnow()
# print(created_at)

#INICIA A CONEXÃO COM O DB
# def open_connection():
#     conn = psycopg2.connect(
#         host=host,
#         port=port,
#         dbname=dbname,
#         user=user,
#         password=password
#     )
#     return conn

# #BUSCA NOME COMPLETO
# def userFullname():
#     #if current_user.is_authenticated:
#         #nomeUsuario = request.authorization['username']
#         conn = open_connection()
#         c = conn.cursor()
#         c.execute("SELECT nome FROM users WHERE username = '{u}'".format(u=current_user.username))
#         res = c.fetchall()
#         c.close()
#         conn.close()
#         nomeUser = pd.DataFrame(res, columns = ['agendamento'])
#         var = nomeUser.iloc[0][0]
#         return var

# def primeiro_nome(nomeCompleto):
#     separador = nomeCompleto.split(" ")
#     nome = separador[0]
#     return nome

import requests
import json
import urllib.parse
import itertools

horaAtual = datetime.now().time().strftime('%H:%M:%S')

produtos = pd.DataFrame({
    1:["DARTH VADER","GANDALF, O BRANCO","SPOCK, O SÁBIO","WOOKIE, O AVENTUREIRO"],
    2:["BRIGADEIRO","NINHO","DUO (BRIGADEIRO E NINHO)","DOCE DE LEITE"],
    3:["R$ 5,00", "R$ 5,00", "R$ 5,00", "R$ 5,00"],
    4:["Brownie 6X6 com muuuuito recheio de BRIGADEIRO para fazer a aliança rebelde tremer de medo!",
        "Brownie 6X6 com muuuuito recheio de NINHO para derrotar as forças de Sauron e salvar a terra média!",
        "Brownie 6X6 com muuuuito recheio DUO (BRIGADEIRO E NINHO) para ir onde ninguém jamais esteve!",
        "Brownie 6X6 com muuuuito recheio de DOCE DE LEITE para as suas aventuras em uma galáxia muito, muito distante!"],
    5:["/static/p1.png","/static/p2.png","/static/p3.png","/static/p4.png"],
    6:["/static/br0.jpg","/static/br1.jpg","/static/br2.jpg","/static/br0.jpg"],
    #7:["/static/brigadeiro.png","/static/ninho.png","/static/duo.png"]
})

#carrinho = []

def start():
    info = "Sistema de pedidos da *Choco Nerds!*"
    info += "\n"
    info += "---------------------------\n"
    info += "Pedido iniciado em: \n"
    info += "*{}, {}/{}/{} às {}*\n".format(dia_da_semana[numero_data], hoje.day, hoje.month, hoje.year, horaAtual)
    info += "\n"
    info += "*Dados do pedido:* \n"
    info += "---------------------------\n"
    return info

def monta_pedido(nome, sabor, quantidade):
    texto = f"*{nome}*, qtd: {str(quantidade)}un.\n"
    texto += f"*Sabor:* {sabor}\n"
    texto += f"*Sub-total:* R${6*quantidade:.2f}\n"
    texto += "---------------------------\n"
    texto += "\n"
    carrinho.append(texto)

def dados_cliente(nome, whats, local, pagamento):
    texto = "\n"
    texto += "*Dados do cliente:*\n"
    texto += "---------------------------\n"
    texto += f"*Nome:* {nome}\n"
    texto += f"*Whatsapp:* {whats}\n"
    texto += f"*Entrega:* {local}\n"
    texto += f"*Forma de pagamento:* {pagamento}\n"
    carrinho.append(texto)

def text_format():
    begin = start()
    print(start)
    message = "".join(carrinho)
    print(message)
    text = begin + message
    return text

# def whatsapp():
#     txt = text_format()          
#     response = requests.get(f'http://api.textmebot.com/send.php?recipient=+555384298702&apikey=gFZv7vjaoJUX&text={urllib.parse.quote(txt)}&json=yes')
#     if response.status_code == 200:
#         data = response.json()
#         print(f"success: {data}")

def pedidos_no_carrinho():
    order_elements = []
    for pedido in carrinho:
        detalhes = pedido.split('\n')
        name = detalhes[0].lower().split(',')[0].strip('*')
        quantity = detalhes[0].split(':')[1].strip()
        flavor = detalhes[1].split(': ')[1]
        total = detalhes[2].split(': ')[1]
        order_element = html.Div([
            html.P(f"Nome: {name}, Qtd.: {quantity}, Sabor: {flavor}, Total: {total}",style={"font-family":"Arial, Helvetica, sans-serif"}),
            html.Hr()
        ])
        order_elements.append(order_element)
    return html.Div(order_elements)

#========== LAYOUT
def render_layout():
    template = html.Div(children=[
            dcc.Location(id="agenda-url"),

            html.Div(id="sinc3", style={"margin-bottom":"15px","display":"none", "justify-content":"center"}),
        
            #header
            dbc.Row([
                dmc.Grid(children=[

                    html.A([
                        html.Div([
                            dbc.CardImg(src="/static/logo.png", class_name="logotipo"),
                        ], style={'textAlign': 'center'},className="logo-agenda"),  
                    ]),#,href="https://agendatreino.com"),

                ],justify="center",align="center"),
            ], justify="center", style={"display":"flex", "justify-content":"center"}, class_name="lowbar"),

            dbc.Row([
                html.A([
                    html.Div([
                        dmc.Button("VOLTAR AO INÍCIO", id="back", variant="gradient", leftSection=DashIconify(icon="material-symbols:home"), radius="30px")
                    ],style={"justify-content":"start", "display":"flex"}),
                ],href="/"),
            ], style={"margin-top":"20px", "margin-left":"10px","display":"flex", "justify-content":"start"}),

            html.Div(id="limpa"),

            dbc.Row([
                html.Div([
                    html.H2("Quase lá!", className="saudacao1"),
                ],style={"justify-content":"center", "display":"flex"})
            ], justify="center", style={"margin-top":"20px", "display":"flex", "justify-content":"center"}),

            #DADOS DO CLIENTE
            dbc.Row([
                html.H5("Insira suas informações a seguir:", className="saudacao1", style={"margin-bottom":"15px"}),
                html.Div([
                    dmc.Stack(
                        children=[
                            dmc.TextInput(placeholder="Informe seu nome completo", style={"width": 350, "margin-bottom":"-20px"}, id="nomeCliente"),
                            dmc.NumberInput(placeholder="Seu whatsapp com DDD", style={"width": 350, "margin-bottom":"-20px"}, id="whatsCliente"),
                            dmc.Textarea(placeholder="Seu endereço de entrega",style={"width": 350}, id="localCliente"),
                            dmc.Select(
                                placeholder="Selecione a forma de pagamento",
                                id="fPagamento",
                                value="ng",
                                data=["Dinheiro", "Pix", "Cartão de Crédito/Débito"],
                                style={"width": 350},
                            ),
                            dmc.Text(id="selected-value"),
                        ],
                    )
                ],style={"justify-content":"center", "display":"flex"})
            ], justify="center", style={"margin-top":"20px", "display":"flex", "justify-content":"center"}),

            #FECHAR PEDIDO
            html.Div([
                dmc.Button("SALVAR OS DADOS", id="encerrar", style={"border-radius":"30px"}, variant="gradient", gradient={"from": "orange", "to": "red", "deg": 105}, leftSection=DashIconify(icon="mdi:user-circle")),
            ],className="d-grid gap-2 d-md-flex justify-content-md-center", style={"justify-content":"center", "display":"flex", "margin-top":"0px"}),

            #PÓS PEDIDO
            html.Div([
                html.Div([
                    dbc.Row(html.P("Dados salvos com sucesso.", className="subtexto6")),
                    dbc.Row(
                        dmc.Button("ENVIAR O PEDIDO", id="enviaPedido", style={"border-radius":"30px","justify-content":"center", "display":"flex"}, variant="gradient", gradient={"from": "lime", "to": "green", "deg": 105}, leftSection=DashIconify(icon="material-symbols:send-rounded")),
                    )
                ],id="finalizou",style={"justify-content":"center", "display":"none", "margin-top":"10px"}),
            ],style={"justify-content":"center", "display":"flex","margin-top":"30px"}),

            html.Div(id="zipzop", style={"justify-content":"center", "display":"flex"}),

            html.Div(style={"margin-top":"20px", "margin-bottom":"30px"}),

            
        ], className="content"),
    return template

#=========================
#====== CALLBACKS ========

#ENVIA PARA O WHATSAPP
@callback(Output("zipzop","children"),
        Input("enviaPedido","n_clicks"),    
)
def envia(n_clicks):
    if n_clicks is not None:
        txt = text_format()          
        response = requests.get(f'http://api.textmebot.com/send.php?recipient=+555384298702&apikey=gFZv7vjaoJUX&text={urllib.parse.quote(txt)}&json=yes')
        if response.status_code == 200:
            data = response.json()
            print(f"success: {data}")
            return html.P("Pedido enviado! Entraremos em contato em breve.", style={"margin-top":"10px","font-family":"Arial"})

#PEDIDO FINALIZADO
@callback(Output(component_id='finalizou', component_property='style'),
          [State("nomeCliente", "value"),
          State("whatsCliente", "value"),
          State("localCliente", "value"),
          State("fPagamento", "value")],
          Input("encerrar", "n_clicks"),
)
def fim(nome, whats, local, pagamento, n_clicks):
    if nome is not None and whats is not None and local is not None and pagamento is not None and n_clicks is not None:
        return dict()
    else:
        return dict(display='none')


#INFORMAÇÕES DO CLIENTE
@callback(Output("selected-value", "children"), 
          [Input("nomeCliente", "value"),
          Input("whatsCliente", "value"),
          Input("localCliente", "value"),
          Input("fPagamento", "value"),
          Input("encerrar", "n_clicks")]          
)
def select_value(nome, whats, local, pagamento, n_clicks):
    if nome is not None and whats is not None and local is not None and pagamento is not None and n_clicks is not None:
        return dados_cliente(nome, whats, local, pagamento)

#sucesso
@app.callback(Output('sinc3', 'children'),
          [Input('sucesso','n_clicks')],
)
def fecha_pedido(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    if n_clicks is not None:
        carrinho.clear()
        print("ENCERRAMENTO")
        print(carrinho)