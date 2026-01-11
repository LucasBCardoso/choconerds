# from dash import Dash, html, dcc, callback
# from dash.dependencies import Input, Output, State
# import dash_bootstrap_components as dbc
# import dash_mantine_components as dmc

# import sqlite3
# from dash_iconify import DashIconify

# from dash.exceptions import PreventUpdate
# from werkzeug.security import generate_password_hash

# from app import *
# import numpy as np
# import pandas as pd
# from IPython.display import display
# import plotly.express as px
# import plotly.graph_objects as go

# from flask_login import logout_user, current_user

# from dash_bootstrap_templates import load_figure_template
# load_figure_template(["litera"])

# from datetime import date
# hora = ""
# numero_data = date.today().weekday() #data
# dia_da_semana = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")
# hoje = date.today()
# dia = dia_da_semana[numero_data]
# #dia = 'Sexta'

# #INICIA A CONEXÃO COM O DB
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
    
# #========== LAYOUT
# def render_layout():
#     template = html.Div(children=[

#             dcc.Location(id="profile-url"),
        
#             #header
#             dbc.Row([
#                 dmc.Grid(children=[

#                     html.A([
#                         html.Div([
#                             dbc.CardImg(src="/static/logo.png", class_name="logotipo"),
#                         ], style={'textAlign': 'center'},className="logo-agenda"),  
#                     ]),#,href="https://agendatreino.com"),

#                     html.A([
#                         html.Div([
#                             #dmc.Button("PERFIL", variant="light", leftSection=DashIconify(icon="gg:profile"), radius="30px")
#                             html.A([html.Div([dmc.Button("GERENCIAR", variant="light", leftSection=DashIconify(icon="fluent:settings-32-regular"), radius="30px")], id="escondeAdm", style={'display':'none'},className="botoes-inicio2")],href="/gerencia"),
#                         ], style={'align-self': 'end', "margin-right":"10px", "justify-content":"end"}),
#                     ],href="/perfil"),

#                 ],justify="center",align="center"),
#             ], justify="center", style={"display":"flex", "justify-content":"center"}, class_name="lowbar"),

#             #BOTAO VOLTAR
#             dbc.Row([
#                 html.A([
#                     html.Div([
#                         dmc.Button("VOLTAR AO INÍCIO", variant="gradient", leftSection=DashIconify(icon="material-symbols:home"), radius="30px")
#                     ],style={"justify-content":"start", "display":"flex"}),
#                 ],href="/"),
#             ], style={"margin-top":"20px", "margin-left":"10px","display":"flex", "justify-content":"start"}),

#             #BOAS VINDAS
#             dbc.Row([
#                 html.Div([
#                     html.P("Olá,", style={"margin-right":"5px"}, className="saudacao0"),
#                     #html.P("{}.".format(primeiro_nome(userFullname())), className="saudacao2"),
#                 ],style={"justify-content":"center", "display":"flex"})
#             ], justify="center", style={"margin-bottom":"-20px", "display":"flex", "justify-content":"center"}),
#             dbc.Row([
#                 html.Div([
#                     html.P("bem-vindo(a) às opções de perfil", style={"margin-right":"5px"}, className="saudacao0"),
#                 ],style={"justify-content":"center", "display":"flex"})
#             ], justify="center", style={"margin-bottom":"-15px", "display":"flex", "justify-content":"center"}),

#             #PESQUISA DE TREINOS
#             dbc.Row([
#                 #AGENDAR TREINO
#                 dbc.Col([
#                     dbc.Card(
#                     [   
#                         #dbc.CardImg(src="/assets/treino1.jpeg", top=True),
#                         dbc.CardBody(
#                             [
#                                 html.H4("Opções de usuário", style={"margin-bottom":"10px", "margin-top":"20px"}),
#                                 html.P("Acesse e altere suas informações:", style={"font-family":"Arial"}, className="opcoesUser"),
#                                 #html.P("Treino agendado para hoje às {}."),
#                                 html.Div([],id="emailAtualX", className="subtexto"),
                                
#                                 # #NOTIFICAÇÃO TELEFONE
#                                 # dmc.NotificationsProvider(
#                                 #     html.Div([
#                                 #         #ALTERAÇÃO DE TELEFONE
#                                 #         html.P("Informe o seu telefone:", style={"font-family":"Arial"}, className="opcoesUser"),
#                                 #         html.Div([current_telefone()],id="telefoneAtualX", className="subtexto"),
#                                 #         html.Div([

#                                 #             dmc.TextInput(
#                                 #                 #label="Your Email",
#                                 #                 style={"width": 350},
#                                 #                 #placeholder="Your Email",
#                                 #                 icon=[DashIconify(icon="material-symbols:phone-enabled")],
#                                 #                 id="foneX"
#                                 #             ),
#                                 #             html.Div(id="telX"),
#                                 #         ], style={"display":"flex", "justify-content":"center"}),

#                                 #         html.Div([
#                                 #             dbc.Button("SALVAR/ALTERAR TELEFONE", id="addTelefoneX", className="botaoSair")
#                                 #         ], style={"display":"flex", "justify-content":"center", "margin-bottom":"20px"}),

#                                 #         html.Div(id="ntFone"),
#                                 #     ])
#                                 # ),
#                                 # html.Hr(), #SEPARADOR

#                                 #NOTIFICAÇÃO E-MAIL
#                                 dmc.NotificationsProvider(
#                                     html.Div([
#                                         #ALTERAÇÃO DE E-MAIL
#                                         html.P("Informe o e-mail desejado:", style={"font-family":"Arial"}, className="opcoesUser"),
#                                         #html.Div([current_email()],id="emailAtualX", className="subtexto"),
#                                         html.Div([

#                                             dmc.TextInput(
#                                                 #label="Your Email",
#                                                 style={"width": 350},
#                                                 #placeholder="Your Email",
#                                                 icon=[DashIconify(icon="material-symbols:mail-rounded")],
#                                                 id="inputMail"
#                                             ),
#                                             html.Div(id="email"),
#                                         ], style={"display":"flex", "justify-content":"center"}),

#                                         html.Div([
#                                             dbc.Button("SALVAR/ALTERAR E-MAIL", id="addEmailX", outline=False, color="primary", className="me-1", style={"border-radius":"30px", "font-weight":"bold"})
#                                         ], style={"display":"flex", "justify-content":"center", "margin-bottom":"20px"}),

#                                         html.Div(id="ntEmail"),
#                                     ])
#                                 ),
#                                 html.Hr(), #SEPARADOR

#                                 #NOTIFICAÇÃO SENHA
#                                 dmc.NotificationsProvider(
#                                     html.Div([
#                                         #ALTERAÇÃO DE SENHA
#                                         html.P("Informe a senha desejada:", style={"font-family":"Arial"}, className="opcoesUser"),
#                                         html.Div([

#                                             dmc.TextInput(
#                                                 #label="Your Email",
#                                                 style={"width": 350},
#                                                 #placeholder="Your Email",
#                                                 icon=[DashIconify(icon="material-symbols:vpn-key-rounded")],
#                                                 id="inputPass"
#                                             ),
#                                             html.Div(id="senha"),
#                                         ], style={"display":"flex", "justify-content":"center"}),

#                                         html.Div([
#                                             dbc.Button("SALVAR/ALTERAR SENHA", id="addSenhaX", outline=False, color="primary", className="me-1", style={"border-radius":"30px", "font-weight":"bold"})
#                                         ], style={"display":"flex", "justify-content":"center", "margin-bottom":"20px"}),

#                                         html.Div(id="ntSenha"),
#                                     ])
#                                 ),
#                                 html.Hr(), #SEPARADOR

#                                 #html.Div([current_vencimento()],id="vencimentoAtualX", className="subtexto"),


#                             ], className="pesquisa"
#                         ),

#                         # #AVISO DE TREINO AGENDADO
#                         html.Div([], style={"display":"flex", "justify-content":"center"}, id="meioCaminho3"),

#                     ],
#                         color="#ff7f1a", inverse=True,
#                         #style={"width": "27rem", "border-radius":"50px", "display":"flex", "justify-content":"center"}
#                         class_name="opUsuario"
#                     ),

#                 ], style={"display":"flex", "justify-content":"center"}),
#             ], justify="center", style={"margin-top":"10px", "display":"flex", "justify-content":"center"}),

#             html.Div([],style={"padding":"20px"}),

#             # html.Div([
#             #     dbc.Button("SAIR DO SISTEMA", id="logout_button", className="botaoSair"),
#             # ],className="d-grid gap-2 d-md-flex justify-content-md-center", style={"justify-content":"center", "display":"flex"}),

#             html.Div([

#                 ],style={"padding":"20px"}),
            
#             dcc.Interval(
#                 id='interval-component',
#                 interval=1*1000, # in milliseconds
#                 n_intervals=0
#             ),

#             #footer
#             dbc.Row([
#                 html.A([
#                     html.Div([ #ri:logout-box-line
#                         dbc.CardImg(src="/static/minilc.png", class_name="logotipo2"),
#                     ], style={'textAlign': 'center'}),
#                 ],href="https://lucapps.studio"),
#             ], justify="center", style={"display":"flex", "justify-content":"center"}, class_name="lowbar2"),

#         ], className="content"),
#     return template

# #=========================
# #====== CALLBACKS ========

# #=========================
# #====== NOTIFICAÇÕES ========

# #NOTIFICAÇÃO TELEFONE
# @app.callback(
#     Output("ntFone", "children"),
#     Input("addTelefoneX", "n_clicks"),
#     prevent_initial_call=True,
# )
# def show(n_clicks):
#     return dmc.Notification(
#         title="Telefone alterado!",
#         id="simple-notify",
#         action="show",
#         message="Os dados de usuário foram salvos.",
#         icon=[DashIconify(icon="ic:round-celebration")],
#     )

# #NOTIFICAÇÃO LOGIN
# @app.callback(
#     Output("ntLogin", "children"),
#     Input("addLoginX", "n_clicks"),
#     prevent_initial_call=True,
# )
# def show(n_clicks):
#     return dmc.Notification(
#         title="Login alterado!",
#         id="simple-notify",
#         action="show",
#         message="Os dados de usuário foram salvos.",
#         icon=[DashIconify(icon="ic:round-celebration")],
#     )

# #NOTIFICAÇÃO E-MAIL
# @app.callback(
#     Output("ntEmail", "children"),
#     Input("addEmailX", "n_clicks"),
#     prevent_initial_call=True,
# )
# def show(n_clicks):
#     return dmc.Notification(
#         title="E-mail alterado!",
#         id="simple-notify",
#         action="show",
#         message="Os dados de usuário foram salvos.",
#         icon=[DashIconify(icon="ic:round-celebration")],
#     )

# #NOTIFICAÇÃO SENHA
# @app.callback(
#     Output("ntSenha", "children"),
#     Input("addSenhaX", "n_clicks"),
#     prevent_initial_call=True,
# )
# def show(n_clicks):
#     return dmc.Notification(
#         title="Senha alterada!",
#         id="simple-notify",
#         action="show",
#         message="Os dados de usuário foram salvos.",
#         icon=[DashIconify(icon="ic:round-celebration")],
#     )
# #=========================
# #====== CONSULTAS NO DB ========

# # #TELEFONE ATUAL
# # def current_telefone():
# #     if current_user.is_authenticated:
# #         #username = request.authorization['username']
# #         c = conn.cursor()
# #         c.execute("SELECT telefone FROM users WHERE username = '{u}'".format(u=current_user.username))
# #         sql_query = c.fetchall()
# #         fone = pd.DataFrame(sql_query, columns = ['telefone'])
# #         var = fone.iloc[0][0]
# #         #print(var)
# #         if var is None:
# #             return "Você não tem telefone cadastrado."
# #         if var is not None:
# #             return "Telefone cadastrado: {}".format(var)

# # #LOGIN ATUAL
# # def current_login(aluno):
# #     if aluno is not None:
# #         sql_query = pd.read_sql("SELECT username FROM users WHERE username = '{u}'".format(u=aluno), conn)
# #         loginUser = pd.DataFrame(sql_query, columns = ['username'])
# #         var = loginUser.iloc[0][0]
# #         #print(var)
# #         if var is not None:
# #             return "Seu nome de usuário é: {}".format(var)

# #E-MAIL ATUAL
# def current_email():
#     #if aluno is not None:
#         # sql_query = pd.read_sql("SELECT email FROM users WHERE username = '{u}'".format(u=aluno), conn)
#         # emailUser = pd.DataFrame(sql_query, columns = ['email'])
#         # var = emailUser.iloc[0][0]
#     #if current_user.is_authenticated:
#         #username = request.authorization['username']
#         conn = open_connection()
#         c = conn.cursor()
#         c.execute("SELECT email FROM users WHERE username = '{u}'".format(u=current_user.username))
#         sql_query = c.fetchall()
#         c.close()
#         conn.close()
#         mail = pd.DataFrame(sql_query, columns = ['email'])
#         var = mail.iloc[0][0]
#         if var is None:
#             return "{}, você não tem e-mail cadastrado.".format(primeiro_nome(userFullname()))
#         if var is not None:
#             return "Seu e-mail: {}".format(var)

# #VENCIMENTO ATUAL
# def current_vencimento():
#     # if aluno is not None:
#     #     sql_query = pd.read_sql("SELECT vencimento FROM users WHERE username = '{u}'".format(u=aluno), conn)
#     #     diaVencimento = pd.DataFrame(sql_query, columns = ['vencimento'])
#     #     var = diaVencimento.iloc[0][0]
#     #if current_user.is_authenticated:
#         #username = request.authorization['username']
#         conn = open_connection()
#         c = conn.cursor()
#         c.execute("SELECT vencimento FROM users WHERE username = '{u}'".format(u=current_user.username))
#         sql_query = c.fetchall()
#         c.close()
#         conn.close()
#         vencimento = pd.DataFrame(sql_query, columns = ['vencimento'])
#         var = vencimento.iloc[0][0]
#         if var is None:
#             var = 0
#         return "Seu dia de vencimento atual é: {}".format(var)

# #=========================
# #====== MUDANÇAS NO DB ========

# #NOVO TELEFONE
# @app.callback(Output('telX','children'),
#             [Input('foneX', 'value')],
#             [Input('addTelefoneX','n_clicks')])
# def update_telefone(value, n_clicks):
#     if n_clicks is not None:
#         #if current_user.is_authenticated:
#             #username = request.authorization['username']
#             conn = open_connection()
#             c = conn.cursor()
#             c.execute("UPDATE users SET telefone = %i WHERE username = %s", (value, current_user.username))
#             conn.commit()
#             c.close()
#             conn.close()


# #NOVO E-MAIL
# @app.callback(Output('email','children'),
#             [Input('inputMail', 'value')],
#             [Input('addEmailX','n_clicks')])
# def update_email(value, n_clicks):
#     if n_clicks is not None:
#         #if current_user.is_authenticated:
#             #username = request.authorization['username']
#             conn = open_connection()
#             c = conn.cursor()
#             c.execute("UPDATE users SET email = %s WHERE username = %s", (value, current_user.username))
#             conn.commit()
#             c.close()
#             conn.close()


# #NOVA SENHA
# @app.callback(Output('senha','children'),
#             [Input('inputPass', 'value')],
#             [Input('addSenhaX','n_clicks')])
# def update_senha(value, n_clicks):
#     if n_clicks is not None:
#         #hashed_password = generate_password_hash(value, method='sha256')
#         #if current_user.is_authenticated:
#             #username = request.authorization['username']
#             conn = open_connection()
#             c = conn.cursor()
#             c.execute("UPDATE users SET password = %s WHERE username = %s", (value, current_user.username))
#             conn.commit()
#             c.close()
#             conn.close()

# #=========================
# #====== LOGOUT DO SISTEMA ========

# # #LOGOUT
# # @app.callback(
# #     Output('profile-url', 'pathname'),
# #     Input('logout_button', 'n_clicks'),
# # )
# # def successful(n_clicks):
# #     if n_clicks == None:
# #         raise PreventUpdate
    
# #     if current_user.is_authenticated:
# #         logout_user()
# #         return '/login'
# #     else:
# #         return '/login'

