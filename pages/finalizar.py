from dash import Dash, html, dcc, callback, callback_context
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import dash
import sqlite3
from dash_iconify import DashIconify

from dash.exceptions import PreventUpdate
from werkzeug.security import generate_password_hash

from app import *
import numpy as np
import pandas as pd
from IPython.display import display
import plotly.express as px
import plotly.graph_objects as go

#from flask_login import logout_user, current_user

from dash_bootstrap_templates import load_figure_template
load_figure_template(["litera"])

from datetime import date
hora = ""
numero_data = date.today().weekday() #data
dia_da_semana = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")
hoje = date.today()
dia = dia_da_semana[numero_data]
#dia = 'Sexta'

#INICIA A CONEXÃO COM O DB
def open_connection():
    conn = psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password
    )
    return conn

#BUSCA NOME COMPLETO
def userFullname():
    #if current_user.is_authenticated:
        #nomeUsuario = request.authorization['username']
        conn = open_connection()
        c = conn.cursor()
        c.execute("SELECT nome FROM users WHERE username = '{u}'".format(u=current_user.username))
        res = c.fetchall()
        c.close()
        conn.close()
        nomeUser = pd.DataFrame(res, columns = ['agendamento'])
        var = nomeUser.iloc[0][0]
        return var

def primeiro_nome(nomeCompleto):
    separador = nomeCompleto.split(" ")
    nome = separador[0]
    return nome

dados = [["","Treino Leve","green"], ["","Leve-moderado","blue"], ["","Moderado-intenso","yellow"], ["","Muito intenso","orange"], ["","Exaustivo","red"]]

# def PreAgenda(aluno):
#     sql_query = pd.read_sql("SELECT agendamento FROM users WHERE username = '{u}'".format(u=aluno), conn)
#     agendaUser = pd.DataFrame(sql_query, columns = ['agendamento'])
#     var = agendaUser.iloc[0][0]
#     #print(var)
#     if var == 'True':
#         return dict(display='none')
#     elif var is None or var == 'None' or var == 'Cancel':
#         return dict()

#========== LAYOUT
def render_layout():
    template = html.Div(children=[

            dcc.Location(id="finalizar-url"),
            html.Div(id="encerramento"),
        
            #header
            dbc.Row([
                dmc.Grid(children=[

                    html.A([
                        html.Div([
                            dbc.CardImg(src="/static/agendalogo-white.png", class_name="logotipo"),
                        ], style={'textAlign': 'center'},className="logo-agenda"),  
                    ],href="https://agendatreino.com"),

                    html.A([
                        html.Div([
                            #dmc.Button("PERFIL", variant="light", leftSection=DashIconify(icon="gg:profile"), radius="30px")
                            html.A([html.Div([dmc.Button("GERENCIAR", variant="light", leftSection=DashIconify(icon="fluent:settings-32-regular"), radius="30px")], id="escondeAdm", style={'display':'none'},className="botoes-inicio2")],href="/gerencia"),
                        ], style={'align-self': 'end', "margin-right":"10px", "justify-content":"end"}),
                    ],href="/perfil"),

                ],justify="center",align="center"),
            ], justify="center", style={"display":"flex", "justify-content":"center"}, class_name="lowbar"),

            dbc.Row([
                html.Div([
                    html.Div([
                        dbc.CardImg(src="/static/logogn.png", class_name="logotipo3"),
                    ], style={'textAlign': 'center'})
                ],className="topBar"),
            ], justify="center", style={"display":"flex", "justify-content":"center"}),

            #BOTAO VOLTAR
            dbc.Row([
                html.A([
                    html.Div([
                        dmc.Button("VOLTAR AO INÍCIO", variant="gradient", leftSection=DashIconify(icon="material-symbols:home"), radius="30px")
                    ],style={"justify-content":"start", "display":"flex"}),
                ],href="/"),
            ], style={"margin-top":"20px", "margin-left":"10px","display":"flex", "justify-content":"start"}),

            #BOAS VINDAS
            dbc.Row([
                html.Div([
                    html.P("Olá,", style={"margin-right":"5px"}, className="saudacao0"),
                    html.P("{}.".format(primeiro_nome(userFullname())), className="saudacao2"),
                ],style={"justify-content":"center", "display":"flex"})
            ], justify="center", style={"margin-top":"20px", "display":"flex", "justify-content":"center"}),
            # dbc.Row([
            #     html.Div([
            #         html.P("vamos finalizar o seu treino.", style={"margin-right":"5px"}, className="saudacao1"),
            #     ],style={"justify-content":"center", "display":"flex"})
            # ], justify="center", style={"margin-bottom":"5px", "display":"flex", "justify-content":"center"}),

            # html.Div([html.H4("Não vai poder treinar?", style={"font-family":"Arial"})], style={"justify-content":"center", "display":"flex"}),
            # html.Div([
            #     html.A([dbc.Button("CANCELAR TREINO", className="bt-treinos", id="cancel")], href="/data"),
            # ], style={"justify-content":"center", "display":"flex"}, id="botaoCancelar"),

            dbc.Row([
                dbc.Col([
                    dbc.Card([ 
                        #dbc.CardImg(src="/static/treino1.jpeg", top=True),
                        dbc.CardBody([
                            html.Div([html.H4("Não vai poder treinar?", style={"font-family":"Arial"})], style={"margin-top":"15px", "margin-bottom":"5px", "justify-content":"center", "display":"flex"}),
                            
                            # html.Div([
                            #     html.A([dbc.Button("CANCELAR TREINO", className="bt-treinos", id="cancelarTreino")], href="/"),
                            # ], style={"justify-content":"center", "display":"flex"}, id="botaoCancelar"),
                            html.Div([
                                dbc.Button("CANCELAR TREINO", href="/", id="cancelarTreino", outline=True, color="danger", className="me-1", style={"border-radius":"30px", "font-weight":"bold"}),
                            ],className="d-grid gap-2 d-md-flex justify-content-md-center", style={"justify-content":"center", "display":"flex"}, id="botaoCancelar"),

                        ], className="cartao")
                    ],color="dark", inverse=True, 
                    class_name="opUsuario"
                    #style={"width": "25rem", "border-radius":"20px"}
                    )
                ], style={"display":"flex", "justify-content":"center", "align-items":"center"})
            ], justify="center", style={"margin-top":"10px", "display":"flex", "justify-content":"center"}), 

            #html.Hr(), #SEPARADOR

            # html.P("Se você treinou e deseja finalizar o treino", style={"margin-top":"30px","font-family":"Arial", "justify-content":"center", "display":"flex"}),
            # html.H5("responda a seguir:", style={"margin-top":"30px","font-family":"Arial", "justify-content":"center", "display":"flex"}),
            dbc.Row([
                dbc.Col([
                    dbc.Card([   
                        #dbc.CardImg(src="/assets/treino1.jpeg", top=True),
                        dbc.CardBody([
                            html.H5("Treinou? Finalize seu treino:", style={"margin-top":"10px", "margin-bottom":"10px", "display":"flex", "justify-content":"center"}, className="subtexto6"),
                            html.H5("O que você achou do treino?", style={"margin-top":"10px", "margin-bottom":"10px", "display":"flex", "justify-content":"center", "font-size":"20px"}),
                            html.P("Selecione uma das opções abaixo:", className="subtexto3", style={"font-family":"Arial", "display":"flex", "justify-content":"center"}),

                             html.Div([
                                html.Div([
                                    dmc.ChipGroup(
                                        [
                                            dmc.Chip(
                                                x,
                                                value=x,
                                                variant="outline",
                                            )
                                            for x in ["Treino Leve", "Leve-moderado", "Moderado-intenso", "Muito intenso", "Exaustivo"]
                                        ],
                                        position="center",
                                        align="center",
                                        id="sentimentos",
                                        multiple=False,
                                    ),
                                    html.Div(id="sense"),
                                ], style={"display":"flex", "justify-content":"center", "align-items":"center"}),
                            
                                # html.Div([
                                #     dbc.Button("SALVAR E FINALIZAR", href="/fim", className="bt-treinos2", id="finalizarTreino")
                                # ], style={"margin-top":"30px", "display":"flex", "justify-content":"center"}),
                                html.Div([
                                    dbc.Button("SALVAR E FINALIZAR", href="/fim", id="finalizarTreino", color="danger", className="me-1", style={"border-radius":"30px", "font-weight":"bold"}),
                                ],className="d-grid gap-2 d-md-flex justify-content-md-center", style={"justify-content":"center", "display":"flex", "margin-top":"20px"}),
                                html.Div(id="ntSense")
                            ]),


                        ], className="cartao")
                    ],color="light", inverse=False,
                    class_name="opUsuario" 
                    #style={"width": "25rem", "border-radius":"20px"}
                    )
                ], style={"display":"flex", "justify-content":"center", "align-items":"center"})
            ], justify="center", style={"margin-top":"10px", "display":"flex", "justify-content":"center"}), 

            # html.Div([
            #         dbc.Button("SALVAR E FINALIZAR TREINO", className="bt-treinos2", id="finalizarTreino", href="/data"),
            # ], id="escondeBtfim", style={"justify-content":"center", "display":"none"}),

            html.Div([],style={"padding":"50px"}),

        html.Div([],style={"padding":"20px"}),

        #footer
        dbc.Row([
            html.A([
                html.Div([ #ri:logout-box-line
                    dbc.CardImg(src="/static/minilc.png", class_name="logotipo2"),
                ], style={'textAlign': 'center'}),
            ],href="https://lucapps.studio"),
        ], justify="center", style={"display":"flex", "justify-content":"center"}, class_name="lowbar2"),

        ], className="content"),
    return template

#=========================
#====== CALLBACKS ========

# #VISIBILIDADE BT FINALIZAR
# @app.callback(
#     Output(component_id='escondeBtfim', component_property='style'),
#     [Input("sentimentos", "value")],
# )
# def btFim(sense):
#     if sense is not None:
#         return dict()
#     else:
#         return dict(display='none')


#ENCERRA O TREINO E VOLTA A AGENDA
@app.callback(
    Output("encerramento", "children"),
    [Input("cancelarTreino", "n_clicks")],
    [Input("finalizarTreino", "n_clicks")],
    [Input("sentimentos", "value")],
    #prevent_initial_call=True,
)
def escondeAgenda(n1, n2, sense):
    print("DADOS DO AGENDAMENTO")
    nomeCompleto = userFullname()
    conn = open_connection()
    c = conn.cursor()
    c.execute("SELECT data, selection FROM agendados WHERE username = '{u}'".format(u=nomeCompleto))
    sql_query = c.fetchall()
    c.close()
    conn.close()
    dadosAgendados = pd.DataFrame(sql_query, columns = ['data', 'selection'])
    var1 = dadosAgendados.iloc[0][0]
    print("var 1: {}".format(var1))
    var2 = dadosAgendados.iloc[0][1]
    print("var 2: {}".format(var2))

    ctx = dash.callback_context
    if ctx.triggered:
        trigg_id = ctx.triggered[0]['prop_id'].split('.')[0]

        if trigg_id == 'cancelarTreino':
            #if current_user.is_authenticated:
                #username = request.authorization['username']
                nome_usuario = userFullname()
                print("CANCELA TREINO")
                conn = open_connection()
                c = conn.cursor()
                c.execute("INSERT INTO historico (data, selection, sentimento, username) VALUES ('{d}', '{s}', '{v}', '{u}')".format(d=hoje, s=var2, v='CANCELADO', u=nome_usuario))
                c.execute(
                    "UPDATE users SET agendamento = %s WHERE username = %s;"
                    "UPDATE agendados SET selection = %s WHERE username = %s",
                    ('False', current_user.username, 'CANCELADO', nome_usuario)
                )
                conn.commit()
                c.close()
                conn.close()


        if trigg_id == 'finalizarTreino':
            #if current_user.is_authenticated:
                #username = request.authorization['username']
                nome_usuario = userFullname()
                print("FINALIZA TREINO")
                conn = open_connection()
                c = conn.cursor()
                c.execute("INSERT INTO historico (data, selection, sentimento, username) VALUES ('{d}', '{s}', '{v}', '{u}')".format(d=hoje, s=var2, v=sense, u=nome_usuario))
                c.execute(
                    "UPDATE users SET agendamento = %s , sentimento = %s WHERE username = %s",
                    ('False', sense, current_user.username)
                    )
                conn.commit()
                c.close()
                conn.close()

                # c = conn.cursor()
                # c.execute("UPDATE users SET agendamento = %s , sentimento = %s WHERE email = %s", ('False', sense, username))
                # print("FOI 2")
                # conn.commit()
                # conn.close()
                # c.close()


# @app.callback(
#     Output("ntSense", "children"),
#     Input("save", "n_clicks"),
#     prevent_initial_call=True,
# )
# def update_db(n_clicks):
#     sql_query = pd.read_sql("SELECT selection FROM agendados WHERE username = '{u}'".format(u=current_user.nomeCompleto), conn)
#     selecionado = pd.DataFrame(sql_query, columns = ['selection'])
#     print(selecionado)
#     var = selecionado.iloc[0][0]
#     if n_clicks is not None:
#         ins = treino_tbl.insert().values(data=hoje,selection=var,username=current_user.username)
#         # conn = engine.connect()
#         #conn.execute(ins)
#         conn.commit(ins)
#         print("call 1")


# #ANTIGO SISTEMA DE ENCERRAMENTO
# @app.callback (
#     Output("sense", "children"),
#     Input("sentimentos", "value"),
#     Input("save","n_clicks"))
# def sentimento(value, n_clicks):
#     nomeCompleto = userFullname()
#     c = conn.cursor()
#     c.execute("SELECT selection FROM agendados WHERE username = '{u}'".format(u=nomeCompleto), conn)
#     sql_query = c.fetchall()
#     selecionado = pd.DataFrame(sql_query, columns = ['selection'])
#     var = selecionado.iloc[0][0]
#     if n_clicks is not None:
#         if auth.is_authorized():
#             nomeUsuario = request.authorization['username']
#             c = conn.cursor()
#             c.execute("INSERT INTO historico(data, selection, sentimento, username) VALUES ('{d}', '{s}', '{v}', '{u}')".format(d=hoje, s=var, v=value, u=nomeCompleto))
#             c.execute("UPDATE users SET agendamento = '{a}', sentimento = '{s}' WHERE username = '{u}'".format(a='False', s=value, u=nomeUsuario))
#             c.execute(
#                 "UPDATE users SET agendamento = %s , sentimento = %s WHERE username = %s",
#                 ('False', value, nomeUsuario)
#             )
#             conn.commit()
#             #PreAgenda(nomeUsuario)
#             conn.close()
#             c.close()

#=========================
#====== MUDANÇAS NO DB ========



#=========================
#====== LOGOUT DO SISTEMA ========

#LOGOUT
# @app.callback(
#     Output('finalizar-url', 'pathname'),
#     Input('logout_button', 'n_clicks'))
# def successful(n_clicks):
#     if n_clicks == None:
#         raise PreventUpdate
    
#     if current_user.is_authenticated:
#         logout_user()
#         return '/login'
#     else:
#         return '/login'

