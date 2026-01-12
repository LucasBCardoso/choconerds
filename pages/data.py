#======================================================================
#ATUALIZAÇÕES PARA FAZER:
#Atualizar callback ADM [x]
#Notificação de vencimento [x]
#Remover quem cancelou e finalizou o treino da lista do dia [x]
#Ordenar resultados na página de gerencia [x]
#Contadores no sistema [x]
#Acesso de senha por usuário [x]
#Número de treinos do aluno [x]
#Como o aluno se sente geralmente pós treino[x]
#Gráfico com histórico de treinos [x]
#Função lista de espera para até 3 vagas []
#Avaliação física []
#Alunos experimentais []
#Possibilidade de alterar os horários de cada dia (segunda a sábado) []
#Alterar logotipo, dados da empresa, imagens de aviso etc []
#======================================================================

from dash import html, dcc, callback
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

# from flask_login import logout_user, current_user

from dash_bootstrap_templates import load_figure_template
load_figure_template(["litera"])

import requests
import json
import logging

import urllib.parse
#The urllib.parse.quote() function is used to URL-encode the text string, so that any special characters are properly encoded and won't cause issues with the API call

# url = 'http://127.0.0.1:8050/'
# response = requests.get(url)

# import sys
# sys.setrecursionlimit(2000)

from datetime import date, datetime, timedelta, time
hora = datetime.now()
numero_data = date.today().weekday() #data
dia_da_semana = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")
hoje = date.today()
dia = dia_da_semana[numero_data]
#dia = "Quarta"
numero_data2 = (date.today()+timedelta(1)).weekday()
dia2 = dia_da_semana[numero_data2]
amanha = date.today()+timedelta(1)
horaAtual = datetime.now().time().strftime('%H:%M:%S')
#print(horaAtual)

def data_atual():
    return html.P("Hoje é {}, {}/{}/{}".format(dia_da_semana[numero_data], hoje.day, hoje.month, hoje.year), className="subtexto3", style={"font-family":"Arial", "display":"flex", "justify-content":"center"})
# currentTime = datetime.now().time()
# endTime = datetime.time(17,40,0)

def data_atual2():
    return html.P("Selecione o seu treino para: {}, {}/{}/{}".format(dia_da_semana[numero_data], hoje.day, hoje.month, hoje.year), className="subtexto5", style={"font-family":"Arial", "display":"flex", "justify-content":"center"})


import datetime as dt  
def isNowInTimePeriod(startTime, endTime, nowTime): 
    if startTime < endTime: 
        return nowTime >= startTime and nowTime <= endTime 
    else: 
        #Over midnight: 
        return nowTime >= startTime or nowTime <= endTime 

#db horário de treinos
horarios = pd.DataFrame({

    "Segunda":[" ","08:30"," ","19:00","20:00"],
    #"Segunda":[" "," "," ","19:00","20:00"],
    #"Terça":["Não há treinos hoje."," "," "," "," "],
    "Terça":[" "," "," ","19:00","20:00"],
    "Quarta":[" ","08:30"," ","19:00","20:00"],
    #"Quarta":[" "," "," ","19:00","20:00"],
    "Quinta":[" ","08:30"," ","19:00"," "],
    "Sexta":[" ","08:30"," ","19:00","20:00"],
    "Sábado":["Não há treinos hoje."," "," "," "," "],
    "Domingo":["Não há treinos hoje."," "," "," "," "]
    #"Domingo":["15:00"," "," "," "," "]

})

options = []
for i in range(horarios.shape[0]):
    for j in range(horarios.shape[1]):
        if horarios.iloc[i, j] != " " and horarios.columns[j] == dia:
            #options.append({"label": horarios.columns[j] + " - " + horarios.iloc[i, j], "value": horarios.columns[j] + " - " + horarios.iloc[i, j]})
            options.append({"label": horarios.iloc[i, j], "value": horarios.iloc[i, j]})

escolha = []
agenda = []
agendados = []

nomeUsuario = ""
nomeCompleto = ""

#ontem = datetime.now()-timedelta(1)
#amanha = datetime.now()+timedelta(1)

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

# Set up logging
logging.basicConfig(filename='app.log', level=logging.ERROR)

produtos = pd.DataFrame({
    1:["DARTH VADER","GANDALF, O BRANCO","SPOCK, O SÁBIO","WOOKIE, O AVENTUREIRO", "SAURON, O SOMBRIO"],
    2:["BRIGADEIRO","NINHO","DUO (BRIGADEIRO E NINHO)","DOCE DE LEITE", "NUTELLA"],
    3:["R$ 6,00", "R$ 6,00", "R$ 6,00", "R$ 6,00", "R$ 6,00"],
    4:["Brownie 6X6 com muuuuito recheio de BRIGADEIRO para fazer a aliança rebelde tremer de medo!",
        "Brownie 6X6 com muuuuito recheio de NINHO para derrotar as forças de Sauron e salvar a terra média!",
        "Brownie 6X6 com muuuuito recheio DUO (BRIGADEIRO E NINHO) para ir onde ninguém jamais esteve!",
        "Brownie 6X6 com muuuuito recheio de DOCE DE LEITE para as suas aventuras em uma galáxia muito, muito distante!",
        "Brownie 6X6 com muuuuito recheio de NUTELLA para a todos os brownies comandar!"],
    5:["/static/p1.png","/static/p2.png","/static/p3.png","/static/p4.png","/static/p5.png"],
    6:["/static/br0.jpg","/static/br1.jpg","/static/br2.jpg","/static/br0.jpg","/static/br0.jpg"],
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
    texto += f"Sabor: {sabor}\n"
    texto += f"Total: R${6*quantidade:.2f}\n"
    texto += "---------------------------\n"
    carrinho.append(texto)

def text_format():
    begin = start()
    print(start)
    message = "".join(carrinho)
    print(message)
    text = begin + message
    return text

def whatsapp():
    texto = text_format()
    phone_number = "+5553984298702"
    url = f"https://wa.me/{phone_number}/?text={urllib.parse.quote(texto)}"
    return url

def pedidos_no_carrinho():
    order_elements = []
    
    if not carrinho:
        return html.Div([
            html.P("Seu carrinho está vazio.", style={"fontFamily": "Arial", "textAlign": "center", "color": "#666", "padding": "20px"})
        ])
    
    for pedido in carrinho:
        try:
            detalhes = pedido.split('\n')
            name = detalhes[0].lower().split(',')[0].strip('*')
            quantity = detalhes[0].split(':')[1].strip() if ':' in detalhes[0] else "1"
            flavor = detalhes[1].split(': ')[1] if len(detalhes) > 1 and ': ' in detalhes[1] else ""
            total = detalhes[2].split(': ')[1] if len(detalhes) > 2 and ': ' in detalhes[2] else ""

            if name == "darth vader":
                imagem = produtos.iloc[0][5]
            
            elif name == "gandalf":
                imagem = produtos.iloc[1][5]

            elif name == "spock":
                imagem = produtos.iloc[2][5]

            elif name == "wookie":
                imagem = produtos.iloc[3][5]

            elif name == "sauron":
                imagem = produtos.iloc[4][5]
            else:
                imagem = produtos.iloc[0][5]

            order_element = html.Div(
                id=f"item-{carrinho.index(pedido)}",
                children=[
                    dbc.Card(
                        [
                            dbc.Row(
                                [
                                    dbc.Col(
                                        dbc.CardImg(
                                            src=f"{imagem}",
                                            className="img-fluid rounded-start",
                                        ),
                                        className="col-md-4",
                                    ),
                                    dbc.Col(
                                        dbc.CardBody(
                                            [
                                                html.H6(f"{name}", style={"margin-bottom":"10px"}),
                                                html.P([
                                                        f"Quantidade: {quantity}",
                                                    ],
                                                    style={"font-family":"Arial, Helvetica, sans-serif", "font-size":"13px", "margin-bottom":"-5px"}
                                                ),
                                                html.P([
                                                        f"Sabor: {flavor}",
                                                    ],
                                                    style={"font-family":"Arial, Helvetica, sans-serif", "font-size":"13px", "margin-bottom":"-5px"}
                                                ),
                                                html.P([
                                                        f"Total: {total}",
                                                    ],
                                                    style={"font-family":"Arial, Helvetica, sans-serif", "font-size":"18px", "margin-top":"10px"}
                                                ),
                                            ]
                                        ),
                                        className="col-md-8",
                                    ),
                                ],
                                className="g-0 d-flex align-items-center"
                            )
                        ],
                        className="mb-3"
                    )
                ]
            )
            order_elements.append(order_element)
        except Exception as e:
            logging.error(f"Erro ao processar pedido: {e}")
            continue
    
    return html.Div(order_elements)


# def pedidos_no_carrinho():
#     order_elements = []
#     for pedido in carrinho:
#         detalhes = pedido.split('\n')
#         name = detalhes[0].lower().split(',')[0].strip('*')
#         quantity = detalhes[0].split(':')[1].strip()
#         flavor = detalhes[1].split(': ')[1]
#         total = detalhes[2].split(': ')[1]

#         if name == "darth vader":
#             imagem = produtos.iloc[0][5]
        
#         elif name == "gandalf":
#             imagem = produtos.iloc[1][5]

#         elif name == "spock":
#             imagem = produtos.iloc[2][5]

#         elif name == "wookie":
#             imagem = produtos.iloc[3][5]

#         elif name == "sauron":
#             imagem = produtos.iloc[4][5]

#         order_element = html.Div([
#             dbc.Card([
#                 dbc.Row([
#                         dbc.Col(
#                             dbc.CardImg(
#                                 src=f"{imagem}",#, style={"width":"150px"},
#                                 className="img-fluid rounded-start",
#                             ),
#                             className="col-md-4",
#                         ),
#                         dbc.Col(
#                             dbc.CardBody(
#                                 [
#                                     html.H6(f"Nome: {name}", style={"margin-bottom":"10px"}),
#                                     html.P([
#                                             f"Qtd.: {quantity}",
#                                         ],
#                                         style={"font-family":"Arial, Helvetica, sans-serif", "font-size":"15px", "margin-bottom":"-5px"}
#                                     ),
#                                     html.P([
#                                             f"Sabor: {flavor}",
#                                         ],
#                                         style={"font-family":"Arial, Helvetica, sans-serif", "font-size":"15px", "margin-bottom":"-5px"}
#                                     ),
#                                     html.P([
#                                             f"Total: {total}",
#                                         ],
#                                         style={"font-family":"Arial, Helvetica, sans-serif", "font-size":"25px", "margin-top":"10px"}
#                                     ),
#                                     html.A([
#                                         dmc.Button("Remover", id="remove", style={"border-radius":"30px"}, variant="gradient", gradient={"from": "purple", "to": "red", "deg": 105}, leftSection=DashIconify(icon="ic:round-remove-shopping-cart"))
#                                     ], href=f"{carrinho.remove(pedido)}")

#                                 ]
#                             ),
#                             className="col-md-8",
#                         ),
#                     ],className="g-0 d-flex align-items-center")
#                 ],
#                 className="mb-3",
#             ),
#         ])
#         order_elements.append(order_element)
#     return html.Div(order_elements)



# def pedidos_no_carrinho():
#     for pedido in carrinho:
        # # detalhes = pedido.split('\n')
        # # detalhes = pedido[0].split(', qtd')[0]  # split at the ", qtd" substring and get the first part
        # # nome = detalhes.split('*')[1]  # split at the "*" character and get the second part
        # # qtd = detalhes[0].split(': ')[1]
        # # sabor = detalhes[1].split(': ')[1]
        # # total = detalhes[2].split(': ')[1]
        # detalhes = pedido.split('\n')
        # nome = detalhes[0].lower().split(',')[0].strip('*')
        # qtd = detalhes[0].split(':')[1].strip()
        # sabor = detalhes[1].lower().split(': ')[1]
        # total = detalhes[2].split(': ')[1]
        # #return(f"Nome: {nome}, Qtd: {qtd}, Sabor: {sabor}, Total: {total}")
        # # return html.Div([
        # #     html.P(f"Nome: {nome}\n"),
        # #     html.P(f"Qtd: {qtd}\n"),
        # #     html.P(f"Sabor: {sabor}\n"),
        # #     html.P(f"Total: {total}\n"),
        # # ])

# def api():
#     url = 'http://lucapps.pythonanywhere.com/'

#     # create a dictionary containing the message and sender
#     data = {
#         "from": "+14155238886",
#         "message": "Hello world!"
#     }

#     # convert the dictionary to JSON
#     json_data = json.dumps(data)

#     # send a POST request to the URL of your Flask app with the JSON data
#     response = requests.post(url, data=json_data)

#     # print the response
#     print(response.text)


#========== LAYOUT
def render_layout(): #(username)
    template = html.Div(children=[
                dcc.Location(id='url', refresh=False),

        html.Div([
            
            #header
            dbc.Row([
                dmc.Grid(children=[

                    html.Div([
                        dbc.CardImg(src="/static/logo.png", class_name="logotipo"),
                    ], style={'textAlign': 'center'},className="logo-agenda"),  

                ],justify="center",align="center"),
            ], justify="center", style={"display":"flex", "justify-content":"center"}, class_name="lowbar"),

            #FECHAR PEDIDO
            # html.Div([
            #     html.A(
            #         html.Button(
            #             "CARRINHO",
            #             id="encerrar",
            #             n_clicks=0,
            #             className="btn btn-gradient",
            #             style={"border-radius": "30px", "width": "100%", "border-color":"black"},
            #         ),
            #         href=whatsapp(),
            #         target="_blank",
            #     ),
            # ],className="d-grid gap-2 d-md-flex justify-content-md-center", style={"justify-content":"center", "display":"flex", "margin-top":"30px"}),

            #MENU LATERAL
            html.Div(
                [
                    dmc.Button("ACESSAR O CARRINHO", id="cart", style={"border-radius":"30px"}, variant="gradient", leftSection=DashIconify(icon="material-symbols:shopping-cart")),
                    dmc.Drawer(
                        html.Div([
                            pedidos_no_carrinho(), 
                            html.A(
                                html.Div([
                                    dmc.Button("FECHAR O PEDIDO", id="cart", style={"border-radius":"30px"}, variant="gradient", gradient={"from": "purple", "to": "red", "deg": 105}, leftSection=DashIconify(icon="material-symbols:shopping-cart")),
                                ], style={"margin-top":"10px","display":"flex", "justify-content":"center"}),
                                href="/sucesso",
                                target="_blank",
                            ),       
                        ],style={"overflow": "scroll", "height": "1000px"}),
                        title="Seu pedido",
                        style={"font-weight":"bold"},
                        id="drawer-simple",
                        padding="md",
                        zIndex=10000,
                        size=550
                    ),
                ],className="d-grid gap-2 d-md-flex justify-content-md-center", style={"justify-content":"center", "display":"flex", "margin-top":"30px"}),

            dbc.Col([

                #ALERTA DE VENCIMENTO
                html.Div(id="ntVencimento"),

                #BOTAO DE ATIVAÇÃO DOS CALLBACKS
                html.Div([dbc.Button(id="config1")], style={"display":"none"}),

                #SINCRONIZAÇÃO
                dbc.Row([
                    html.Div([
                        dbc.Button("SINCRONIZAR DADOS", id="sincronizar", className="botaoSair"),
                    ],style={"justify-content":"center", "display":"none"}),
                ], justify="center", style={"margin-bottom":"15px","display":"flex", "justify-content":"center"}),

                html.Div(id="sinc", style={"margin-bottom":"15px","display":"none", "justify-content":"center"}),
                html.Div(id="sinc2", style={"margin-bottom":"15px","display":"none", "justify-content":"center"}),

                html.Div(id='selected-images'),

                #BRIGADEIRO
                dbc.Row([
                    dmc.Card(
                        children=[
                            dmc.CardSection(
                                html.Div([
                                    dbc.Carousel(
                                    items=[
                                        {
                                            "key": "1",
                                            "src": "/static/p1.png",
                                        },
                                        {
                                            "key": "2",
                                            "src": "/static/br0.jpg",
                                        },
                                    ], style={"font-family":"Arial", "border-radius":"20px"}, variant="dark", className="carousel-fade", interval=3000, ride="carousel"),
                                ], style={"display":"flex", "justify-content":"center", "border-radius":"20px"}),
                            ),
                            dmc.Group(
                                [
                                    dmc.Text("DARTH VADER", fw=500, style={"fontFamily": "Arial"}),
                                ],
                                justify="space-between",
                                mt="md",
                                mb="xs",
                                style={"margin-left":"10px"}
                            ),
                            dmc.Group([
                                dmc.Badge("BRIGADEIRO", variant="gradient", gradient={"from": "purple", "to": "red", "deg": 105}, style={"font-size":"14px","padding":"12px"}),
                                dmc.Badge("R$ 6,00", color="green", variant="gradient", gradient={"from": "teal", "to": "lime", "deg": 105}, style={"font-size":"14px","padding":"12px"}),
                            ], gap="xs", style={"margin-left":"10px"}),
                            dmc.Text(
                                "Brownie 6X6 com muuuuito recheio de BRIGADEIRO para fazer a aliança rebelde tremer de medo!",
                                fz="sm",
                                c="dimmed",
                                style={"margin-left":"10px", "margin-top":"10px", "fontFamily": "Arial"}
                            ),
                            html.Div([
                                html.P("Quantas unidades?",className="subtexto6", style={"fontFamily": "Arial"}),
                            ], style={"display":"flex", "justify-content":"center", "margin-top":"10px", "margin-bottom":"-5px"}),
                            html.Div([
                                dmc.NumberInput(
                                    value=1,
                                    min=1,
                                    step=1,
                                    style={"width": 250},
                                    id="unidades"
                                ),
                            ], style={"display":"flex", "justify-content":"center", "margin-bottom":"-20px"}),
                            
                            html.A([
                                dmc.Button(
                                    "ADICIONAR AO CARRINHO",
                                    variant="gradient",
                                    gradient={"from": "orange", "to": "red"},
                                    fullWidth=True,
                                    mt="md",
                                    radius="30px",
                                    id="brownie-select1",
                                    leftSection=DashIconify(icon="material-symbols:shopping-cart"),
                                ),
                            ],href="/"),

                        ],
                        withBorder=True,
                        shadow="sm",
                        radius="md",
                        style={"width": 330, "margin-bottom":"15px"},
                        id="produto"
                    ),

                    #NINHO
                    dmc.Card(
                        children=[
                            dmc.CardSection(
                                html.Div([
                                    dbc.Carousel(
                                    items=[
                                        {
                                            "key": "1",
                                            "src": "/static/p2.png",
                                        },
                                        {
                                            "key": "2",
                                            "src": "/static/br1.jpg",
                                        },
                                    ], style={"font-family":"Arial", "border-radius":"20px"}, variant="dark", className="carousel-fade", interval=3000, ride="carousel"),
                                ], style={"display":"flex", "justify-content":"center", "border-radius":"20px"}),
                            ),
                            dmc.Group(
                                [
                                    dmc.Text("GANDALF, O BRANCO", fw=500, style={"fontFamily": "Arial"}),
                                ],
                                justify="space-between",
                                mt="md",
                                mb="xs",
                                style={"margin-left":"10px"}
                            ),
                            dmc.Group([
                                dmc.Badge("NINHO", variant="gradient", gradient={"from": "purple", "to": "red", "deg": 105}, style={"font-size":"14px","padding":"12px"}),
                                dmc.Badge("R$ 6,00", color="green", variant="gradient", gradient={"from": "teal", "to": "lime", "deg": 105}, style={"font-size":"14px","padding":"12px"}),
                            ], gap="xs", style={"margin-left":"10px"}),
                            dmc.Text(
                                "Brownie 6X6 com muuuuito recheio de NINHO para derrotar as forças de Sauron e salvar a terra média!",
                                fz="sm",
                                c="dimmed",
                                style={"margin-left":"10px", "margin-top":"10px", "fontFamily": "Arial"}
                            ),
                            html.Div([
                                html.P("Quantas unidades?",className="subtexto6", style={"fontFamily": "Arial"}),
                            ], style={"display":"flex", "justify-content":"center", "margin-top":"10px", "margin-bottom":"-5px"}),
                            html.Div([
                                dmc.NumberInput(
                                    value=1,
                                    min=1,
                                    step=1,
                                    style={"width": 250},
                                    id="unidades2"
                                ),
                            ], style={"display":"flex", "justify-content":"center", "margin-bottom":"-20px"}),
                            html.A([
                                dmc.Button(
                                    "ADICIONAR AO CARRINHO",
                                    variant="gradient",
                                    gradient={"from": "orange", "to": "red"},
                                    fullWidth=True,
                                    mt="md",
                                    radius="30px",
                                    id="brownie-select2",
                                    leftSection=DashIconify(icon="material-symbols:shopping-cart"),
                                ),
                            ],href="/"),
                        ],
                        withBorder=True,
                        shadow="sm",
                        radius="md",
                        style={"width": 330, "margin-bottom":"15px"},
                        id="produto"
                    ),

                    #DUO
                    dmc.Card(
                        children=[
                            dmc.CardSection(
                                html.Div([
                                    dbc.Carousel(
                                    items=[
                                        {
                                            "key": "1",
                                            "src": "/static/p3.png",
                                        },
                                        {
                                            "key": "2",
                                            "src": "/static/br2.jpg",
                                        },

                                    ], style={"font-family":"Arial", "border-radius":"20px"}, variant="dark", className="carousel-fade", interval=3000, ride="carousel"),
                                ], style={"display":"flex", "justify-content":"center", "border-radius":"20px"}),
                            ),
                            dmc.Group(
                                [
                                    dmc.Text("SPOCK, O SÁBIO", fw=500, style={"fontFamily": "Arial"}),
                                ],
                                justify="space-between",
                                mt="md",
                                mb="xs",
                                style={"margin-left":"10px"}
                            ),
                            dmc.Group([
                                dmc.Badge("DUO", variant="gradient", gradient={"from": "purple", "to": "red", "deg": 105}, style={"font-size":"14px","padding":"12px"}),
                                dmc.Badge("R$ 6,00", color="green", variant="gradient", gradient={"from": "teal", "to": "lime", "deg": 105}, style={"font-size":"14px","padding":"12px"}),
                            ], gap="xs", style={"margin-left":"10px"}),
                            dmc.Text(
                                "Brownie 6X6 com muuuuito recheio DUO (BRIGADEIRO E NINHO) para ir onde ninguém jamais esteve!",
                                fz="sm",
                                c="dimmed",
                                style={"margin-left":"10px", "margin-top":"10px", "fontFamily": "Arial"}
                            ),
                            html.Div([
                                html.P("Quantas unidades?",className="subtexto6", style={"fontFamily": "Arial"}),
                            ], style={"display":"flex", "justify-content":"center", "margin-top":"10px", "margin-bottom":"-5px"}),
                            html.Div([
                                dmc.NumberInput(
                                    value=1,
                                    min=1,
                                    step=1,
                                    style={"width": 250},
                                    id="unidades3"
                                ),
                            ], style={"display":"flex", "justify-content":"center", "margin-bottom":"-20px"}),
                            html.A([
                                dmc.Button(
                                    "ADICIONAR AO CARRINHO",
                                    variant="gradient",
                                    gradient={"from": "orange", "to": "red"},
                                    fullWidth=True,
                                    mt="md",
                                    radius="30px",
                                    id="brownie-select3",
                                    leftSection=DashIconify(icon="material-symbols:shopping-cart"),
                                ),
                            ],href="/"),
                        ],
                        withBorder=True,
                        shadow="sm",
                        radius="md",
                        style={"width": 330, "margin-bottom":"15px"},
                        id="produto"
                    ),

                    #DOCE DE LEITE
                    dmc.Card(
                        children=[
                            dmc.CardSection(
                                html.Div([
                                    dbc.Carousel(
                                    items=[
                                        {
                                            "key": "1",
                                            "src": "/static/p4.png",
                                        },
                                        {
                                            "key": "2",
                                            "src": "/static/br2.jpg",
                                        },

                                    ], style={"font-family":"Arial", "border-radius":"20px"}, variant="dark", className="carousel-fade", interval=3000, ride="carousel"),
                                ], style={"display":"flex", "justify-content":"center", "border-radius":"20px"}),
                            ),
                            dmc.Group(
                                [
                                    dmc.Text("WOOKIE, O AVENTUREIRO", fw=500, style={"fontFamily": "Arial"}),
                                ],
                                justify="space-between",
                                mt="md",
                                mb="xs",
                                style={"margin-left":"10px"}
                            ),
                            dmc.Group([
                                dmc.Badge("DOCE DE LEITE", variant="gradient", gradient={"from": "purple", "to": "red", "deg": 105}, style={"font-size":"14px","padding":"12px"}),
                                dmc.Badge("R$ 6,00", color="green", variant="gradient", gradient={"from": "teal", "to": "lime", "deg": 105}, style={"font-size":"14px","padding":"12px"}),
                            ], gap="xs", style={"margin-left":"10px"}),
                            dmc.Text(
                                "Brownie 6X6 com muuuuito recheio de DOCE DE LEITE para as suas aventuras em uma galáxia muito, muito distante!",
                                fz="sm",
                                c="dimmed",
                                style={"margin-left":"10px", "margin-top":"10px", "fontFamily": "Arial"}
                            ),
                            html.Div([
                                html.P("Quantas unidades?",className="subtexto6", style={"fontFamily": "Arial"}),
                            ], style={"display":"flex", "justify-content":"center", "margin-top":"10px", "margin-bottom":"-5px"}),
                            html.Div([
                                dmc.NumberInput(
                                    value=1,
                                    min=1,
                                    step=1,
                                    style={"width": 250},
                                    id="unidades4"
                                ),
                            ], style={"display":"flex", "justify-content":"center", "margin-bottom":"-20px"}),
                            html.A([
                                dmc.Button(
                                    "ADICIONAR AO CARRINHO",
                                    variant="gradient",
                                    gradient={"from": "orange", "to": "red"},
                                    fullWidth=True,
                                    mt="md",
                                    radius="30px",
                                    id="brownie-select4",
                                    leftSection=DashIconify(icon="material-symbols:shopping-cart"),
                                ),
                            ],href="/"),
                        ],
                        withBorder=True,
                        shadow="sm",
                        radius="md",
                        style={"width": 330, "margin-bottom":"15px"},
                        id="produto"
                    ),

                    #NUTELLA
                    dmc.Card(
                        children=[
                            dmc.CardSection(
                                html.Div([
                                    dbc.Carousel(
                                    items=[
                                        {
                                            "key": "1",
                                            "src": "/static/p5.png",
                                        },
                                        {
                                            "key": "2",
                                            "src": "/static/br0.jpg",
                                        },

                                    ], style={"font-family":"Arial", "border-radius":"20px"}, variant="dark", className="carousel-fade", interval=3000, ride="carousel"),
                                ], style={"display":"flex", "justify-content":"center", "border-radius":"20px"}),
                            ),
                            dmc.Group(
                                [
                                    dmc.Text("SAURON, O SOMBRIO", fw=500, style={"fontFamily": "Arial"}),
                                ],
                                justify="space-between",
                                mt="md",
                                mb="xs",
                                style={"margin-left":"10px"}
                            ),
                            dmc.Group([
                                dmc.Badge("NUTELLA", variant="gradient", gradient={"from": "purple", "to": "red", "deg": 105}, style={"font-size":"14px","padding":"12px"}),
                                dmc.Badge("R$ 6,00", color="green", variant="gradient", gradient={"from": "teal", "to": "lime", "deg": 105}, style={"font-size":"14px","padding":"12px"}),
                            ], gap="xs", style={"margin-left":"10px"}),
                            dmc.Text(
                                "Brownie 6X6 com muuuuito recheio de NUTELLA para a todos os brownies comandar!",
                                fz="sm",
                                c="dimmed",
                                style={"margin-left":"10px", "margin-top":"10px", "fontFamily": "Arial"}
                            ),
                            html.Div([
                                html.P("Quantas unidades?",className="subtexto6", style={"fontFamily": "Arial"}),
                            ], style={"display":"flex", "justify-content":"center", "margin-top":"10px", "margin-bottom":"-5px"}),
                            html.Div([
                                dmc.NumberInput(
                                    value=1,
                                    min=1,
                                    step=1,
                                    style={"width": 250},
                                    id="unidades5"
                                ),
                            ], style={"display":"flex", "justify-content":"center", "margin-bottom":"-20px"}),
                            html.A([
                                dmc.Button(
                                    "ADICIONAR AO CARRINHO",
                                    variant="gradient",
                                    gradient={"from": "orange", "to": "red"},
                                    fullWidth=True,
                                    mt="md",
                                    radius="30px",
                                    id="brownie-select5",
                                    leftSection=DashIconify(icon="material-symbols:shopping-cart"),
                                ),
                            ],href="/"),
                        ],
                        withBorder=True,
                        shadow="sm",
                        radius="md",
                        style={"width": 330, "margin-bottom":"15px"},
                        id="produto"
                    ),


                ], justify="center", style={"margin-top":"30px", "display":"flex", "justify-content":"center", "gap":"15px"}),

                
                # #FECHAR PEDIDO
                # html.Div([
                #     html.A(
                #         html.Button(
                #             "FECHAR PEDIDO",
                #             id="encerrar",
                #             n_clicks=0,
                #             className="btn btn-gradient",
                #             style={"border-radius": "30px", "width": "100%", "border-color":"black"},
                #         ),
                #         href=whatsapp(),
                #         target="_blank",
                #     ),
                # ],className="d-grid gap-2 d-md-flex justify-content-md-center", style={"justify-content":"center", "display":"flex", "margin-top":"30px"}),


                #ESPAÇO EM BRANCO
                html.Div([],style={"padding":"20px"}),

                #SAIR DO SISTEMA
                # html.Div([
                #     dbc.Button("SAIR DO SISTEMA", id="logout_button", outline=True, color="danger", className="me-1", style={"border-radius":"30px", "font-weight":"bold"}),
                # ],className="d-grid gap-2 d-md-flex justify-content-md-center", style={"justify-content":"center", "display":"flex"}),

                #dmc.NotificationsProvider(html.Div(id="ntPreAgenda")),

                html.Div([
                    html.P("2026 v2.0 | Choco Nerds!",style={"font-size":"10px"},className="escolhas2"),
                ],className="d-grid gap-2 d-md-flex justify-content-md-center", style={"justify-content":"center", "display":"flex"}),
            
            ],className="content"),

            #ESPAÇO EM BRANCO
                html.Div([],style={"padding":"20px"}),

        ], style={"display":"block"}, id="acessoTotal"),
        html.Div(id="bloqueado"),
        
        # Footer
        html.Div([
            html.A(
                "Criado por Lucas Cardoso",
                href="https://www.lucasbcardoso.com.br",
                target="_blank",
                style={"fontFamily": "Arial", "fontSize": "12px", "color": "#666", "textDecoration": "none"}
            ),
        ], style={"display":"flex", "justify-content":"center", "padding":"20px"}),
    ])
    return template

#=========================
#====== CALLBACKS ========

# #REMOVER ITEM DO CARRINHO
# @app.callback(
#     Output("carrinho-container", "children"),
#     Input("remove", "n_clicks"),
#     State("carrinho-container", "children"),
#     prevent_initial_call=True
# )
# def remove_item_from_cart(n, children):
#     if n:
#         item_index = dash.callback_context.triggered[0]["prop_id"].split(".")[0].split("-")[-1]
#         carrinho.pop(int(item_index))
#         return pedidos_no_carrinho()
#     else:
#         raise PreventUpdate


# #CARRINHO
# @callback(
#     Output("drawer-simple", "opened"),
#     Input("cart", "n_clicks"),
#     prevent_initial_call=True,
# )
# def pedidos_no_carrinho():
#     for pedido in carrinho:
#         detalhes = pedido.split('\n')
#         nome = detalhes[0].split(': ')[1]
#         sabor = detalhes[1].split(': ')[1]
#         total = detalhes[2].split(': ')[1]
#         return(f"Nome: {nome}, Sabor: {sabor}, Total: {total}")
#         #return html.P(f"{carrinho}"),

#MENU LATERAL
@callback(
    Output("drawer-simple", "opened"),
    Input("cart", "n_clicks"),
    prevent_initial_call=True,
)
def drawer_demo(n_clicks):
    return True

#MONTA PEDIDO
@app.callback(Output('sinc', 'children'),
          [Input('brownie-select1','n_clicks'),
          Input('brownie-select2','n_clicks'),
          Input('brownie-select3','n_clicks'),
          Input('brownie-select4','n_clicks'),
          Input('brownie-select5','n_clicks')],
          [State('unidades','value')],
          [State('unidades2','value')],
          [State('unidades3','value')],
          [State('unidades4','value')],
          [State('unidades5','value')],
)
def current_pedido(b1, b2, b3, b4, b5, v1, v2, v3, v4, v5):
    ctx = dash.callback_context
    if ctx.triggered:
        trigg_id = ctx.triggered[0]['prop_id'].split('.')[0]
        print("Valor atual do trigg_id: {}".format(trigg_id))

        if trigg_id == "brownie-select1":
            monta_pedido(produtos.iloc[0][1], produtos.iloc[0][2], v1)

        elif trigg_id == "brownie-select2":
            monta_pedido(produtos.iloc[1][1], produtos.iloc[1][2], v2)

        elif trigg_id == "brownie-select3":
            monta_pedido(produtos.iloc[2][1], produtos.iloc[2][2], v3)

        elif trigg_id == "brownie-select4":
            monta_pedido(produtos.iloc[3][1], produtos.iloc[3][2], v4)

        elif trigg_id == "brownie-select5":
            monta_pedido(produtos.iloc[4][1], produtos.iloc[4][2], v5)
        
        # elif trigg_id == "encerrar":
        #     carrinho.clear()
        #     print("ENCERRAMENTO")
        #     print(carrinho)


#FECHA PEDIDO
# @app.callback(Output('sinc2', 'children'),
#           [Input('encerrar','n_clicks')],
# )
# def fecha_pedido(n_clicks):
#     if n_clicks is None:
#         raise PreventUpdate
#     if n_clicks is not None:
#         return whatsapp()


# @app.callback(Output('url', 'pathname'),
#               [Input('encerrar', 'n_clicks')])
# def update_url(n_clicks):
#     if n_clicks is not None:
#         print("CHEGOU NO SUCESSO")
#         return '/sucesso'

# @app.callback(Output('page-content', 'children'),
#               [Input('url', 'pathname')])
# def render_page_content(pathname):
#     if pathname == '/sucesso':
#         return sucesso.render_layout()