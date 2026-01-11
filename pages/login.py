
from app import *

###############################################
            #LAYOUT DA PÁGINA
###############################################
def render_layout(message):

    message = "Ocorreu um erro durante o login." if message == "error" else message
    login = dbc.Row([

        dbc.Card(
        [
            html.Div([
                #LOGOTIPO DO CLIENTE
                dbc.CardImg(src="/static/logo.png", top=True, style={"width":"60%"}),
            ], style={'textAlign': 'center'}),
            dbc.CardBody(
                [
                    html.H4("Realizar login", className="card-title", style={"margin-top":"-5px"}),
                    #dbc.Input(id="user_login", placeholder="Digite seu nome de usuário", type="text", className="form"),
                    dbc.Input(id="email_login", placeholder="Digite seu e-mail", type="email", className="form", style={"border-radius":"30px"}),
                    dbc.Input(id="pwd_login", placeholder="Digite sua senha", type="password", className="form", style={"border-radius":"30px"}),
                    html.Div([
                        #dbc.Button("LOGIN NO TIME GN", id="login_button", className="botaoLogin"),
                        dmc.Button("ACESSAR O SISTEMA", variant="gradient", leftSection=DashIconify(icon="mdi:login"), radius="30px", id="login_button", gradient={"from": "indigo", "to": "cyan"},)
                    ], className="d-grid gap-2 d-md-flex justify-content-md-center", style={"margin-bottom":"15px"}),
                    #html.Div([html.Span(message, className="mensagem")], style={"justify-content":"center", "display":"flex"}),
                    html.Label("Não tem cadastro?", style={"justify-content":"center", "display":"flex", "margin-bottom":"5px", "font-size":"13px"}),
                    html.Div([
                        html.A([
                            dmc.Button(
                                "REGISTRE-SE AGORA",
                                variant="gradient",
                                gradient={"from": "indigo", "to": "cyan"},
                                radius="30px",
                                leftSection=DashIconify(icon="mdi:register")
                            ),
                        ], href="/register")
                    ],style={"justify-content":"center", "display":"flex"})
                ]
            ),

        ],
            color="#ff7f1a", #inverse=True,
            #style={"width": "25rem", "padding":"20px", "border-radius":"30px"}, 
            className="caixaLogin"),

    ],style={'height':'100vh', 'display':'flex', 'justify-content':'center'}, className="fundoTela"),
    return login

#CALLBACKS
#=======================================
@app.callback(
    Output('login-state', 'data'),

    Input('login_button','n_clicks'),
    [
        #State('user_login', 'value'),
        State('email_login','value'),
        State('pwd_login', 'value')
    ]
)
def successful(n_clicks, email, password):
    if n_clicks == None:
        raise PreventUpdate

    user = Users.query.filter_by(email=email).first()
    #print(f"Usuário: {user}")
    
    if user and password is not None:
        print("chegou aqui")
        print("user: {}".format(user))
        print("pass: {}".format(password))
        print("pass-data: {}".format(user.password))
        if user.password == password:
            login_user(user, remember=True, duration=None, force=False, fresh=True)
            return 'success'
        # print("user: {}".format(user))
        # print("pass: {}".format(password))
        # if check_password_hash(user.password, password):
        #     login_user(user, remember=True, duration=None, force=False, fresh=True)
        #     return 'success'
        else:
            print("Password incorrect")
            return 'error'
    else:
        print("deu erro")
        return 'error'
