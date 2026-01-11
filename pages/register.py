from app import *
from datetime import date
hoje = date.today()

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

def render_layout(message):
    message = "Ocorreu um erro durante o registro." if message == "error" else message

    register = dbc.Row([

        dbc.Card(
        [
            html.Div([
                #LOGOTIPO DO CLIENTE
                dbc.CardImg(src="/static/logo.png", top=True, style={"width":"60%"}),
            ], style={'textAlign': 'center'}),
            dbc.CardBody(
                [
                    html.H4("Cadastre-se para realizar pedidos", className="card-title"),
                    dbc.Input(id="nome_register", placeholder="Nome completo", type="text", className="form"),
                    #dbc.Input(id="cpf_register", placeholder="Seu CPF", type="number", className="form"),
                    dbc.Input(id="email_register", placeholder="Seu e-mail", type="email", className="form"),
                    dbc.Input(id="pwd_register", placeholder="Sua senha", type="password", className="form"),
                    html.Div([
                        #dbc.Button("CADASTRE-SE NO TIME GN", id="register-button", className="botaoRegistro"),
                        dmc.Button("REALIZAR CADASTRO", variant="gradient", gradient={"from": "indigo", "to": "cyan"}, leftSection=DashIconify(icon="mdi:register"), radius="30px", id="register-button")
                    ], className="d-grid gap-2 d-md-flex justify-content-md-center", style={"margin-bottom":"15px"}),
                    #html.Div([html.Span(message, className="mensagem")], style={"justify-content":"center", "display":"flex"}),
                    html.Label("Já tem cadastro?", style={"justify-content":"center", "display":"flex", "margin-bottom":"5px", "font-size":"13px"}),
                    html.Div([
                        html.A([
                            dmc.Button(
                                "FAÇA SEU LOGIN",
                                variant="gradient",
                                gradient={"from": "indigo", "to": "cyan"},
                                radius="30px",
                                leftSection=DashIconify(icon="mdi:login")
                            ),
                        ], href="/login")
                    ],style={"justify-content":"center", "display":"flex"})
                ]
            ),

            ],
                color="#ff7f1a", #inverse=True,
                #style={"width": "25rem", "padding":"20px", "border-radius":"30px"}, 
                className="caixaLogin"),

        ],style={'height':'100vh', 'display':'flex', 'justify-content':'center'}, className="fundoTela"),
    return register

@app.callback(
    Output('register-state', 'data'),

    Input('register-button','n_clicks'),
    [
        State('nome_register', 'value'),
        #State('cpf_register', 'value'),
        State('email_register','value'),
        State('pwd_register', 'value')
    ]
)
def register(n_clicks, full_name, email, password):
    if n_clicks == None:
        raise PreventUpdate
        
    # if full_name is not None and email is not None and password is not None:
    #     #hashed_password = bcrypt.generate_password_hash(password)
    #     #hashed_password = generate_password_hash(password, method='sha256')
    #     conn = open_connection()
    #     c = conn.cursor()
    #     c.execute(
    #         "INSERT INTO users (username, nome, email, password, ativo, agendamento) VALUES (%s, %s, %s, %s, %s, %s);"
    #         "INSERT INTO agendados (username) VALUES (%s)",
    #         ('AT'+full_name, full_name, email, password, 'Sim', 'False', full_name)
    #         #('AT'+full_name, full_name, email, password, 'Sim', 'False', full_name)
    #     )
    #     conn.commit()
    #     c.close()
    #     conn.close()
    #     return ''
    # else:
    #     return 'error'
    
    