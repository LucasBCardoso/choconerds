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
# import datetime as dt 
# from datetime import date, datetime, timedelta, time

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

# def senha(usuario):
#     print("ACESSO DE SENHAS")
#     #if current_user.is_authenticated:
#     #username = request.authorization['username']
#     if current_user.email == 'lucasbrasilcardoso@gmail.com':
#         conn = open_connection()
#         c = conn.cursor()
#         c.execute("SELECT password FROM users WHERE username = '{u}'".format(u=usuario))
#         sql_query = c.fetchall()
#         status = pd.DataFrame(sql_query, columns = ['password'])
#         c.close()
#         conn.close()
#         var = status.iloc[0][0]
#         print("Senha: {}".format(var))
#         return html.Div([
#                 html.P("Senha: {}".format(var), className="subtexto3", style={"justify-content":"center", "display":"flex"}),
#             ]),
#     else:
#         dash.no_update

# # Defina as opções para o dropdown de horas
# hora_opcoes = [{'label': time(hour=i, minute=j).strftime('%H:%M'), 'value': i*60+j} for i in range(0, 24) for j in range(0, 60, 30)]

# #========== LAYOUT
# def render_layout():
#     template = html.Div(children=[

#             dcc.Location(id="gerencia-url"),

#             html.Div([
        
#                 #header
#                 dbc.Row([
#                     dmc.Grid(children=[

#                         html.A([
#                             html.Div([
#                                 dbc.CardImg(src="/static/agendalogo-white.png", class_name="logotipo"),
#                             ], style={'textAlign': 'center'},className="logo-agenda"),  
#                         ],href="https://agendatreino.com"),

#                         # html.A([
#                         #     html.Div([
#                         #         #dmc.Button("PERFIL", variant="light", leftIcon=DashIconify(icon="gg:profile"), radius="30px")
#                         #         html.A([html.Div([dmc.Button("GERENCIAR", variant="light", leftIcon=DashIconify(icon="fluent:settings-32-regular"), radius="30px")], id="escondeAdm", style={'display':'none'},className="botoes-inicio2")],href="/gerencia"),
#                         #     ], style={'align-self': 'end', "margin-right":"10px", "justify-content":"end"}),
#                         # ],href="/perfil"),

#                     ],justify="center",align="center"),
#                 ], justify="center", style={"display":"flex", "justify-content":"center"}, class_name="lowbar"),

#                 dbc.Row([
#                     html.Div([
#                         html.Div([
#                             dbc.CardImg(src="/static/logogn.png", class_name="logotipo3"),
#                         ], style={'textAlign': 'center'})
#                     ],className="topBar"),
#                 ], justify="center", style={"display":"flex", "justify-content":"center"}),

#                 #BOTAO VOLTAR
#                 # html.Div([
#                 #     dbc.Col([
#                 #         dbc.Button("INÍCIO", href="/", className="botaoSair"),
#                 #         dmc.Button("DADOS DO PERFIL", variant="gradient", leftIcon=DashIconify(icon="gg:profile"), radius="30px")
#                 #         #dbc.Button("VOLTAR", color="primary", id="voltar1", className="voltar"),
#                 #     ], width=2, style={"margin-top":"20px", "margin-left":"10px","display":"flex", "justify-content":"start"}),
#                 # ], style={"display":"flex", "justify-content":"start"}),

#                 dbc.Row([
#                     html.A([
#                         html.Div([
#                             dmc.Button("VOLTAR AO INÍCIO", variant="gradient", leftIcon=DashIconify(icon="material-symbols:home"), radius="30px")
#                         ],style={"justify-content":"start", "display":"flex"}),
#                     ],href="/"),
#                 ], style={"margin-top":"20px", "margin-left":"10px","display":"flex", "justify-content":"start"}),

#                 #BOAS VINDAS
#                 dbc.Row([
#                     html.Div([
#                         html.P("Olá,", style={"margin-right":"5px"}, className="saudacao0"),
#                         html.P("{}.".format(primeiro_nome(userFullname())), className="saudacao2"),
#                     ],style={"justify-content":"center", "display":"flex"})
#                 ], justify="center", style={"margin-bottom":"-20px", "display":"flex", "justify-content":"center"}),

#                 dbc.Row([
#                     html.Div([
#                         html.P("bem-vindo(a) às opções de gerência", style={"margin-right":"5px"}, className="saudacao0"),
#                     ],style={"justify-content":"center", "display":"flex"})
#                 ], justify="center", style={"margin-bottom":"-15px", "display":"flex", "justify-content":"center"}),
                
#                 # html.Div([dbc.Button("SINCRONIZAR", id="botaoSinc", className="botaoSair")],style={"display":"flex", "justify-content":"center"}),
#                 html.Div(id="sincronize", style={"display":"none"}),
#                 dbc.Button(id="user_sync", style={"display":"none"}),
#                 #, href="/gerencia"

#                 #dbc.Button("REGISTROS", href="/register", className="botaoSair"),

#                 # #ALTERAÇÃO DE HORÁRIOS
#                 # dbc.Row([
#                 #     dbc.Col([
#                 #         dbc.Card([ 
#                 #             #dbc.CardImg(src="/static/treino1.jpeg", top=True),
#                 #             dbc.CardBody([
#                 #                 html.Div([html.H4("Configuração de horários:", style={"font-family":"Arial"})], style={"margin-top":"15px", "margin-bottom":"5px", "justify-content":"center", "display":"flex"}),
#                 #                 # html.Div([
#                 #                 #     html.A([dbc.Button("CANCELAR TREINO", className="bt-treinos", id="cancelarTreino")], href="/"),
#                 #                 # ], style={"justify-content":"center", "display":"flex"}, id="botaoCancelar"),
#                 #                 html.Div([
#                 #                     dbc.Checklist(
#                 #                         options = [
#                 #                         {"label": i, "value": i} for i in horarios_de_treino[hour].unique() #if i != ' ' and i != 'Não há treinos hoje.'
#                 #                         ],
#                 #                         id="selectTreino", 
#                 #                         switch=True
#                 #                     ),
#                 #                     ], style={"margin-top":"20px", "display":"flex", "justify-content":"center"}),
#                 #             ], className="cartao")
#                 #         ],color="dark", inverse=True, style={"width": "27rem"})
#                 #     ], style={"display":"flex", "justify-content":"center", "align-items":"center"})
#                 # ], justify="center", style={"margin-top":"10px", "display":"flex", "justify-content":"center"}),

#                 #CONFIGURAÇÃO DE TREINOS
#                 # dbc.Row([
#                 #     dbc.Col([
#                 #         dbc.Card([ 
#                 #             dbc.CardBody([
        
#                 #                 html.Div([html.H5("CONFIGURAÇÃO DE TREINOS", style={"font-family":"Arial"})], style={"margin-top":"15px", "margin-bottom":"5px", "justify-content":"center", "display":"flex"}),
                                
#                 #                 #SELETOR DE DIA
#                 #                 html.Div([
#                 #                     dmc.Select(
#                 #                         placeholder="Selecione o dia da semana",
#                 #                         id='dpDiaDaSemana',
#                 #                         data=[
#                 #                             {'value':i, 'label':i} for i in dia_da_semana
#                 #                         ]
#                 #                         ,clearable=True
#                 #                         ,style={"width": 350, "color":"#CB2128"}
#                 #                         ,icon=[DashIconify(icon="mdi:gym")]
#                 #                         ,persistence_type="local"
#                 #                     ),
#                 #                     html.Div(id='resDiaDaSemana'),
#                 #                 ], style={"display":"flex", "justify-content":"center"}),
                                
#                 #                 # #SELETOR DE HORAS
#                 #                 # html.Div([
#                 #                 #     dmc.Select(
#                 #                 #         placeholder="Selecione um horário"
#                 #                 #         ,id='hora-select'
#                 #                 #         ,searchable=True
#                 #                 #         ,data=hora_opcoes
#                 #                 #         ,clearable=True
#                 #                 #         ,style={"width": 350, "color":"#CB2128"}
#                 #                 #         ,icon=[DashIconify(icon="ic:round-access-time-filled")]
#                 #                 #     ),
#                 #                 # ], style={"display":"flex", "justify-content":"center"}),

#                 #                 #MULTI-SELETOR DE HORAS
#                 #                 html.Div([
#                 #                     dmc.MultiSelect(
#                 #                         placeholder="Selecione os horários de treino"
#                 #                         ,id="framework-multi-select"
#                 #                         ,searchable=True
#                 #                         ,data=hora_opcoes
#                 #                         ,clearable=True
#                 #                         ,style={"width": 350, "color":"#CB2128"}
#                 #                         ,icon=[DashIconify(icon="ic:round-access-time-filled")]
#                 #                     ),
#                 #                     dmc.Text(id="multi-selected-value"),
#                 #                 ], style={"display":"flex", "justify-content":"center"}),

#                 #                 html.Div([
#                 #                     dmc.Button(
#                 #                         "SALVAR HORÁRIOS",
#                 #                         variant="gradient",
#                 #                         gradient={"from": "orange", "to": "red"},
#                 #                         radius="30px",
#                 #                         id="btSalvaHorarios",
#                 #                         style={"font-weight":"bold"}
#                 #                     ),
#                 #                 ],style={"justify-content":"center", "display":"flex", "margin-top":"25px"}),


#                 #             ], className="cartao")

#                 #         ],color="dark", inverse=True,
#                 #         class_name="opUsuario"
#                 #         #style={"width": "25rem", "border-radius":"20px"}
#                 #         )
#                 #     ], style={"display":"flex", "justify-content":"center", "align-items":"center"})
#                 # ], justify="center", style={"margin-top":"10px", "margin-bottom":"15px", "display":"flex", "justify-content":"center"}),

#                 #ACESSO À SENHA DO USUÁRIO
#                 dbc.Row([
#                     dbc.Col([
#                         dbc.Card([ 
#                             dbc.CardBody([
#                                 html.Div([html.H4("Acesso de senhas", style={"font-family":"Arial"})], style={"margin-top":"15px", "margin-bottom":"5px", "justify-content":"center", "display":"flex"}),
#                                 html.Div([],id="senha_user", style={"justify-content":"center", "display":"flex"}),
#                             ], className="cartao")
#                         ],color="dark", inverse=True, 
#                         class_name="opUsuario"
#                         #style={"width": "25rem", "border-radius":"20px"}
#                         )
#                     ], style={"display":"flex", "justify-content":"center", "align-items":"center"})
#                 ], justify="center", style={"margin-top":"10px", "display":"flex", "justify-content":"center"}),

#                 #INFORMAÇÕES ADICIONAIS DE USUÁRIO
#                 # dbc.Row([
#                 #     dbc.Col([
#                 #         dbc.Card([ 
#                 #             dbc.CardBody([
#                 #                 html.Div([html.H4("Treinos de usuário", style={"font-family":"Arial"})], style={"margin-top":"15px", "margin-bottom":"5px", "justify-content":"center", "display":"flex"}),
#                 #                 #html.Div([],id="senha_user", style={"justify-content":"center", "display":"flex"}),
#                 #             ], className="cartao")
#                 #         ],color="dark", inverse=True, style={"width": "27rem", "border-radius":"50px"})
#                 #     ], style={"display":"flex", "justify-content":"center", "align-items":"center"})
#                 # ], justify="center", style={"margin-top":"10px", "display":"flex", "justify-content":"center"}),
                
#                 #OPÇÕES DE USUÁRIO
#                 dbc.Row([
#                     dbc.Col([
#                         dbc.Card(
#                         [   
#                             #dbc.CardImg(src="/assets/treino1.jpeg", top=True),
#                             dbc.CardBody(
#                                 [
#                                     html.H4("Opções de usuário", style={"margin-bottom":"10px", "margin-top":"20px"}),
#                                     html.P("Selecione um aluno para começar:", style={"font-family":"Arial"}, className="opcoesUser"),
#                                     #html.P("Treino agendado para hoje às {}."),
#                                     html.Div([],id="emailAtual", className="subtexto"),

#                                     html.Div(id="listaAlunos", style={"display":"flex", "justify-content":"center"}),
#                                     dcc.Interval(
#                                         id="updateSelection",
#                                         interval=1*300000, # in milliseconds 300000 = 5 min
#                                         n_intervals=0
#                                     ),

#                                     # html.Div(
#                                     # [
#                                     #     dmc.Select(
#                                     #         #label="Select framework",
#                                     #         placeholder="Selecione o aluno",
#                                     #         id='dropdown4',
#                                     #         data=[
#                                     #             {'value':i, 'label':i} for i in df_resx['valor']
#                                     #         ]                                     
#                                     #         ,searchable=True
#                                     #         ,clearable=True
#                                     #         ,nothingFound="Não há alunos."
#                                     #         ,style={"width": 350}
#                                     #         ,icon=[DashIconify(icon="mdi:user-circle")]
#                                     #         #,rightSection=[DashIconify(icon="radix-icons:chevron-down")]
#                                     #     ),
#                                     #     html.Div([html.Div(id='output0')], style={"display":"none", "justify-content":"center"}),

#                                     #     dcc.Interval(
#                                     #         id="intervalo",
#                                     #         interval=1*60000, # in milliseconds
#                                     #         n_intervals=0
#                                     #     ),
#                                     # ], style={"margin-top":"20px","display":"flex", "justify-content":"center"}),
                                    
#                                     html.Hr(), #SEPARADOR
                                    
#                                     #NOTIFICAÇÃO TELEFONE
#                                     # dmc.NotificationsProvider(
#                                     #     html.Div([
#                                     #         #ALTERAÇÃO DE TELEFONE
#                                     #         html.P("Informe o telefone do usuário:", style={"font-family":"Arial"}, className="opcoesUser"),
#                                     #         html.Div([],id="telefoneAtual", className="subtexto"),
#                                     #         html.Div([

#                                     #             dmc.TextInput(
#                                     #                 #label="Your Email",
#                                     #                 style={"width": 350},
#                                     #                 #placeholder="Your Email",
#                                     #                 icon=[DashIconify(icon="material-symbols:phone-enabled")],
#                                     #                 id="fone"
#                                     #             ),
#                                     #             html.Div(id="tel"),
#                                     #         ], style={"display":"flex", "justify-content":"center"}),

#                                     #         html.Div([
#                                     #             dbc.Button("SALVAR/ALTERAR TELEFONE", id="addTelefone", className="botaoSair")
#                                     #         ], style={"display":"flex", "justify-content":"center", "margin-bottom":"20px"}),

#                                     #         html.Div(id="notification0"),
#                                     #     ])
#                                     # ),
                                    
#                                     # html.Hr(), #SEPARADOR

#                                     #NOTIFICAÇÃO VENCIMENTO
#                                     dmc.NotificationsProvider(
#                                         html.Div([
#                                             #ALTERAÇÃO DE VENCIMENTO
#                                             html.P("Selecione uma data de vencimento:", style={"font-family":"Arial"}, className="opcoesUser"),
#                                             html.Div([],id="vencimentoAtual", className="subtexto"),
#                                             html.Div([
#                                                 #ADICIONANDO O VENCIMENTO PARA O USUÁRIO
#                                                 dmc.NumberInput(
#                                                     #label="Selecione o dia de vencimento",
#                                                     # description="Step the value when clicking and holding the arrows",
#                                                     stepHoldDelay=500,
#                                                     stepHoldInterval=100,
#                                                     value=0,
#                                                     max=31,
#                                                     style={"width": 350},
#                                                     id="vencimento"
#                                                 ),
#                                                 html.Div(id="venc"),
#                                             ], style={"display":"flex", "justify-content":"center"}),

#                                             html.Div([
#                                                 dbc.Button("SALVAR/ALTERAR VENCIMENTO", id="addVencimento", outline=True, color="danger", className="me-1", style={"border-radius":"30px", "font-weight":"bold"})
#                                             ], style={"display":"flex", "justify-content":"center", "margin-bottom":"20px"}),

#                                             html.Div(id="notification1"),
#                                         ])
#                                     ),

#                                     html.Hr(), #SEPARADOR
                                    
#                                     #NOTIFICAÇÃO ADM
#                                     dmc.NotificationsProvider(
#                                         html.Div([
#                                             #ALTERAÇÃO DE ADM
#                                             html.P("Altere o status de administrador:", style={"font-family":"Arial"}, className="opcoesUser"),
#                                             html.Div([],id="statusAtual", className="subtexto"),
#                                             html.Div(id="novoAdm"),
#                                             html.Div([
#                                                 dbc.Button("SALVAR/ALTERAR STATUS", id="addAdm", outline=True, color="danger", className="me-1", style={"border-radius":"30px", "font-weight":"bold"})
#                                             ], style={"display":"flex", "justify-content":"center", "margin-bottom":"20px"}),
                                        
#                                         html.Div(id="notification2"),
#                                     ])),

#                                     html.Hr(), #SEPARADOR

#                                     #NOTIFICAÇÃO ATIVAR/DESATIVAR ALUNO
#                                     dmc.NotificationsProvider(
#                                         html.Div([
#                                             #ALTERAÇÃO DE ATIVAÇÃO
#                                             html.P("Altere o status de ativação:", style={"font-family":"Arial"}, className="opcoesUser"),
#                                             html.Div([],id="ativacaoAtual", className="subtexto"),
#                                             html.Div(id="novoAtv"),
#                                             html.Div([
#                                                 dbc.Button("ATIVAR/DESATIVAR ALUNO", id="addAtv", outline=True, color="danger", className="me-1", style={"border-radius":"30px", "font-weight":"bold"})
#                                             ], style={"display":"flex", "justify-content":"center", "margin-bottom":"20px"}),
                                        
#                                         html.Div(id="notification3"),
#                                     ])),

#                                     html.Hr(), #SEPARADOR

#                                     #NOTIFICAÇÃO EXCLUIR ALUNO
#                                     dmc.NotificationsProvider(
#                                         html.Div([
#                                             #ALTERAÇÃO DE ATIVAÇÃO
#                                             html.P("DESEJA EXCLUIR O ALUNO?", style={"font-family":"Arial"}, className="opcoesUser"),
#                                             html.P("ATENÇÃO: Essa ação não pode ser desfeita!", className="subtexto7", style={"font-family":"Arial"}),
#                                             html.Div(id="novoExc"),
#                                             html.Div([
#                                                 dbc.Button("EXCLUIR ALUNO", id="excluirAluno", outline=True, color="danger", className="me-1", style={"border-radius":"30px", "font-weight":"bold"}, href='/gerencia')
#                                             ], style={"display":"flex", "justify-content":"center", "margin-bottom":"20px"}),
                                        
#                                         html.Div(id="notification4"),
#                                     ])),

#                                 ], className="pesquisa"
#                                 #DELETE FROM customers WHERE city = 'Paris'
#                             ),

#                             # #AVISO DE TREINO AGENDADO
#                             html.Div([], style={"display":"flex", "justify-content":"center"}, id="meioCaminho3"),

#                         ],
#                             color="dark", inverse=True,
#                             class_name="opUsuario"
#                             #style={"width": "25rem", "border-radius":"20px", "display":"flex", "justify-content":"center"}
#                             ),

#                     ], style={"display":"flex", "justify-content":"center"}),
#                 ], justify="center", style={"margin-top":"10px", "display":"flex", "justify-content":"center"}),

#                 html.Div([],style={"padding":"20px"}),

#                 # html.Div([
#                 #     dbc.Button("SAIR DO SISTEMA", id="logout_button", className="botaoSair"),
#                 # ],className="d-grid gap-2 d-md-flex justify-content-md-center", style={"justify-content":"center", "display":"flex"}),

#                 html.Div([

#                     ],style={"padding":"20px"},id="end"),

#                 # dcc.Interval(
#                 #     id='interval-component',
#                 #     interval=1*60000, # in milliseconds
#                 #     n_intervals=0
#                 # ),
#             ], style={"display":"block"}, id="acessoTotal2"),
#             html.Div(id="bloqueado"),

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

# #VISIBILIDADE DA PÁGINA DE GERENCIA
# @app.callback(Output(component_id='acessoTotal2', component_property='style'),
#     [Input('user_sync','n_clicks')],
#     #prevent_initial_call=True,
# )
# def acessoTotal(n_clicks):
#     #if n_clicks is not None:  
#     #print("CHEGOU AQUI")   
#     #if current_user.is_authenticated:
#         #nomeUsuario = request.authorization['username']
#         conn = open_connection()
#         c = conn.cursor()
#         c.execute("SELECT status FROM users WHERE username = '{u}'".format(u=current_user.username))
#         res = c.fetchall()
#         c.close()
#         conn.close()
#         acesso = pd.DataFrame(res, columns = ['status'])
#         var_acesso = acesso.iloc[0][0]
#         #if var_acesso == 'Não':
#         if current_user.email == 'lucasbrasilcardoso@gmail.com' or var_acesso == 'True':
#             return dict()
#         else:
#             return dict(display='none')

# #VISUALIZADOR DE SENHAS
# @app.callback(Output("senha_user","children"),
#     State("gerenciaAlunos","value"),
#     Input("botaoSelect","n_clicks"))
# def alunoEscolhido(value, n_clicks):
#     if n_clicks is not None:
#         #if current_user.is_authenticated:
#             #username = request.authorization['username']
#             if current_user.email == 'lucasbrasilcardoso@gmail.com':
#                 conn = open_connection()
#                 c = conn.cursor()
#                 c.execute("SELECT email, password FROM users WHERE nome = '{u}'".format(u=value))
#                 sql_query = c.fetchall()
#                 status = pd.DataFrame(sql_query, columns = ['email','password'])
#                 c.close()
#                 conn.close()
#                 var1 = status.iloc[0][0]
#                 print("email: {}".format(var1))
#                 var2 = status.iloc[0][1]
#                 print("Senha: {}".format(var2))
#                 return html.Div([
#                         html.P("Email: {}".format(var1), className="subtexto3", style={"justify-content":"center", "display":"flex"}),
#                         html.P("Senha: {}".format(var2), className="subtexto3", style={"justify-content":"center", "display":"flex"}),
#                     ]),
#     else:
#         return html.Div([
#                 html.P("Nenhum usuário selecionado.", className="subtexto3", style={"justify-content":"center", "display":"flex"}),
#             ]),

# # @app.callback(Output('listaAlunos','children'),
# #     [Input('botaoSinc','n_clicks')])
# # def sinc(n_clicks):
# #     if n_clicks is not None:
# #         sincronizar()

# # @app.callback(
# #     Output('end','children'),
# #     [Input('selectTreino','value')]
# # )
# # def horarios_por_dia(horario_selecionado):
# #     horarios.loc[0] = horario_selecionado
# #     print(horarios)

# @app.callback(Output('listaAlunos','children'),
#     [Input('updateSelection','n_intervals')])
# def sincronizar(n):
#     # print(value)
#     # print(hoje)
#     conn = open_connection()
#     c = conn.cursor()
#     c.execute("SELECT nome FROM users")
#     res = c.fetchall()
#     df_new = pd.DataFrame(res, columns=['nome']).sort_values(by="nome")
#     c.close()
#     conn.close()
#     #print(df_new)
#     return html.Div([
#         dmc.Select(
#             #label="Select framework",
#             placeholder="Lista de alunos",
#             id='gerenciaAlunos',
#             data=[
#                 {'value':i, 'label':i} for i in df_new['nome']
#             ]                                     
#             ,searchable=True
#             ,clearable=True
#             ,nothingFound="Não há alunos."
#             ,style={"width": 300}
#             ,icon=[DashIconify(icon="mdi:user-circle")]
#             #,rightSection=[DashIconify(icon="radix-icons:chevron-down")]
#         ),
#         #html.Div([html.Div(id='output0')], style={"display":"none", "justify-content":"center"}),
#         html.Div([dbc.Button("SELECIONAR", id="botaoSelect", outline=True, color="danger", className="me-1", style={"border-radius":"30px", "font-weight":"bold"})],style={"display":"flex", "justify-content":"center"}),

#     ])

# @app.callback(Output("sincronize","children"),
#     State("gerenciaAlunos","value"),
#     Input("botaoSelect","n_clicks"))
# def alunoEscolhido(value, n_clicks):
#     if n_clicks is not None:
#         escolhido = value
#         return escolhido

# #USUÁRIO SELECIONADO NO DROPDOWN
# # @app.callback(Output('output0', 'children'),
# #           [Input('dropdown4', 'value')])
# # def update_output_1(value):
# #     if value is not None:
# #         filtered_df = df_resx[df_resx['valor'] == value]
# #         return filtered_df.iloc[0]['valor']

# #===================================================

# #NOTIFICAÇÃO EXCLUIR ALUNO
# @app.callback(
#     Output("notification4", "children"),
#     Input("excluirAluno", "n_clicks"),
#     prevent_initial_call=True,
# )
# def show(n_clicks):
#     return dmc.Notification(
#         title="Aluno excluido!",
#         id="simple-notify",
#         action="show",
#         message="Os dados de usuário foram salvos.",
#         icon=[DashIconify(icon="ic:round-celebration")],
#     )

# #NOTIFICAÇÃO TELEFONE
# @app.callback(
#     Output("notification0", "children"),
#     Input("addTelefone", "n_clicks"),
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

# #NOTIFICAÇÃO VENCIMENTO
# @app.callback(
#     Output("notification1", "children"),
#     Input("addVencimento", "n_clicks"),
#     prevent_initial_call=True,
# )
# def show(n_clicks):
#     return dmc.Notification(
#         title="Vencimento alterado!",
#         id="simple-notify",
#         action="show",
#         message="Os dados de usuário foram salvos.",
#         icon=[DashIconify(icon="ic:round-celebration")],
#     )

# #NOTIFICAÇÃO ADM
# @app.callback(
#     Output("notification2", "children"),
#     Input("addAdm", "n_clicks"),
#     prevent_initial_call=True,
# )
# def show(n_clicks):
#     return dmc.Notification(
#         title="Status alterado!",
#         id="simple-notify",
#         action="show",
#         message="Administrador atualizado com sucesso.",
#         icon=[DashIconify(icon="ic:round-celebration")],
#     )

# #NOTIFICAÇÃO ATIVAÇÃO
# @app.callback(
#     Output("notification3", "children"),
#     Input("addAtv", "n_clicks"),
#     prevent_initial_call=True,
# )
# def show(n_clicks):
#     return dmc.Notification(
#         title="Status de ativação alterado!",
#         id="simple-notify",
#         action="show",
#         message="usuário atualizado com sucesso.",
#         icon=[DashIconify(icon="ic:round-celebration")],
#     )

# #===================================================

# # #EMAIL ATUAL
# # @app.callback(Output('emailAtual', 'children'),
# #           [Input('gerenciaAlunos', 'value')],
# #           prevent_initial_call=True,)
# # def current_email(aluno):
# #     if aluno is not None:
# #         sql_query = pd.read_sql("SELECT email FROM users WHERE nomeCompleto = '{u}'".format(u=aluno), conn)
# #         diaVencimento = pd.DataFrame(sql_query, columns = ['email'])
# #         var = diaVencimento.iloc[0][0]
# #         #print(var)
# #         if var is None:
# #             return "{} Não tem e-mail cadastrado.".format(aluno)
# #         if var is not None:
# #             return "O e-mail de {} é {}".format(aluno, var)

# # #TELEFONE ATUAL
# # @app.callback(Output('telefoneAtual', 'children'),
# #           [Input('gerenciaAlunos', 'value')],
# #           prevent_initial_call=True,)
# # def current_telefone(aluno):
# #     if aluno is not None:
# #         sql_query = pd.read_sql("SELECT telefone FROM users WHERE nomeCompleto = '{u}'".format(u=aluno), conn)
# #         diaVencimento = pd.DataFrame(sql_query, columns = ['telefone'])
# #         var = diaVencimento.iloc[0][0]
# #         #print(var)
# #         if var is None:
# #             return "{} não tem telefone cadastrado.".format(aluno)
# #         if var is not None:
# #             return "Telefone de {}: {}".format(aluno, var)

# #VENCIMENTO ATUAL
# @app.callback(Output('vencimentoAtual', 'children'),
#           [Input('sincronize','children')],
#           #[Input('gerenciaAlunos','value')],
#           prevent_initial_call=True,)
# def current_vencimento(aluno):
#     #lock.acquire(True)
#     if aluno is not None:
#         conn = open_connection()
#         c = conn.cursor()
#         c.execute("SELECT vencimento FROM users WHERE nome = '{u}'".format(u=aluno))
#         sql_query = c.fetchall()
#         c.close()
#         conn.close()
#         venc = pd.DataFrame(sql_query, columns = ['vencimento'])
#         var = venc.iloc[0][0]
#         if var is None:
#             var = 0
#         #lock.release()
#         return "O vencimento atual de {} é dia {}".format(aluno, var)
    

# #STATUS ADM ATUAL
# @app.callback(Output('statusAtual', 'children'),
#           [Input('sincronize', 'children')],
#           #[Input('gerenciaAlunos','value')],
#           prevent_initial_call=True,)
# def current_adm(aluno):
#     #lock.acquire(True)
#     if aluno is not None:
#         conn = open_connection()
#         c = conn.cursor()
#         c.execute("SELECT status FROM users WHERE nome = '{u}'".format(u=aluno))
#         sql_query = c.fetchall()
#         c.close()
#         conn.close()
#         st = pd.DataFrame(sql_query, columns = ['status'])
#         var = st.iloc[0][0]
#         if var is None or var == 'False':
#             var = 'Não é admin'
#         if var == 'True':
#             var = 'É admin'
#         #lock.release()
#         return "Status atual de {}: {}".format(aluno, var)
    
# #STATUS ATIVAÇÃO ATUAL
# @app.callback(Output('ativacaoAtual', 'children'),
#           [Input('sincronize', 'children')],
#           #[Input('gerenciaAlunos','value')],
#           prevent_initial_call=True,)
# def current_adm(aluno):
#     #lock.acquire(True)
#     if aluno is not None:
#         conn = open_connection()
#         c = conn.cursor()
#         c.execute("SELECT ativo FROM users WHERE nome = '{u}'".format(u=aluno))
#         sql_query = c.fetchall()
#         c.close()
#         conn.close()
#         atv = pd.DataFrame(sql_query, columns = ['ativo'])
#         var = atv.iloc[0][0]
#         if var is None or var == 'Não':
#             var = 'Usuário desativado.'
#         if var == 'Sim':
#             var = 'Usuário ativo.'
#         #lock.release()
#         return "Status atual de {}: {}".format(aluno, var)

# #===================================================

# # #NOVO TELEFONE
# # @app.callback(Output('tel','children'),
# #             [State('gerenciaAlunos', 'value')],
# #             [Input('fone', 'value')],
# #             [Input('addTelefone','n_clicks')])
# # def update_df_users(aluno, value, n_clicks):
# #     if n_clicks is not None:
# #         c.execute("UPDATE users SET telefone = {v} WHERE nomeCompleto = '{u}'".format(v=value, u=aluno))
# #         conn.commit()

# #NOVO VENCIMENTO
# @app.callback(Output('venc','children'),
#             [Input('sincronize', 'children')],
#             [Input('vencimento', 'value')],
#             [Input('addVencimento','n_clicks')])
# def update_df_users(aluno, value, n_clicks):
#     #print("vencimento: {}".format(aluno))
#     if n_clicks is not None:
#         conn = open_connection()
#         c = conn.cursor()
#         c.execute("UPDATE users SET vencimento = {v} WHERE nome = '{u}'".format(v=value, u=aluno))
#         conn.commit()
#         c.close()
#         conn.close()

# #NOVO ADM
# @app.callback(Output('novoAdm','children'),
#             [Input('sincronize', 'children')],
#             [Input('addAdm', 'n_clicks')])
# def update_df_users(aluno, n_clicks):
#     #print("adm: {}".format(aluno))
#     if aluno is not None:
#         conn = open_connection()
#         c = conn.cursor()
#         c.execute("SELECT status FROM users WHERE nome = '{u}'".format(u=aluno))
#         sql_query = c.fetchall()
#         c.close()
#         conn.close()
#         statusAdm = pd.DataFrame(sql_query, columns = ['status'])
#         var = statusAdm.iloc[0][0]
#         if n_clicks is not None:
#             if var is None or var == 'False':
#                 conn = open_connection()
#                 c = conn.cursor()
#                 c.execute("UPDATE users SET status = 'True' WHERE nome = '{u}'".format(u=aluno))
#                 conn.commit()
#                 c.close()
#                 conn.close()
#             elif var == 'True':
#                 conn = open_connection()
#                 c = conn.cursor()
#                 c.execute("UPDATE users SET status = 'False' WHERE nome = '{u}'".format(u=aluno))
#                 conn.commit()
#                 c.close()
#                 conn.close()

# #NOVA ATIVAÇÃO
# @app.callback(Output('novoAtv','children'),
#             [Input('sincronize', 'children')],
#             [Input('addAtv', 'n_clicks')])
# def update_df_users(aluno, n_clicks):
#     #print("adm: {}".format(aluno))
#     if aluno is not None:
#         conn = open_connection()
#         c = conn.cursor()
#         c.execute("SELECT ativo FROM users WHERE nome = '{u}'".format(u=aluno))
#         sql_query = c.fetchall()
#         c.close()
#         conn.close()
#         statusAtv2 = pd.DataFrame(sql_query, columns = ['status'])
#         var = statusAtv2.iloc[0][0]
#         if n_clicks is not None:
#             if var is None or var == 'Não':
#                 conn = open_connection()
#                 c = conn.cursor()
#                 c.execute("UPDATE users SET ativo = 'Sim' WHERE nome = '{u}'".format(u=aluno))
#                 conn.commit()
#                 c.close()
#                 conn.close()
#             elif var == 'Sim':
#                 conn = open_connection()
#                 c = conn.cursor()
#                 c.execute("UPDATE users SET ativo = 'Não' WHERE nome = '{u}'".format(u=aluno))
#                 conn.commit()
#                 c.close()
#                 conn.close()

# #NOVA ATIVAÇÃO
# @app.callback(Output('novoExc','children'),
#             [Input('sincronize', 'children')],
#             [Input('excluirAluno', 'n_clicks')])
# def update_df_users(aluno, n_clicks):
#     #print("adm: {}".format(aluno))
#     if aluno is not None:
#         if n_clicks is not None:
#             conn = open_connection()
#             c = conn.cursor()
#             c.execute("DELETE FROM users WHERE nome = '{u}'".format(u=aluno))
#             c.execute("DELETE FROM agendados WHERE username = '{u}'".format(u=aluno))
#             conn.commit()
#             c.close()
#             conn.close()

# # #LOGOUT
# # @app.callback(
# #     Output('gerencia-url', 'pathname'),
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

