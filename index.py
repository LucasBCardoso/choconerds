#IMPORTS
from app import *
from app import server
from pages import login, register, data, perfil, gerencia, finalizar, sucesso

# #LOGIN MANAGER
# login_manager = LoginManager()
# login_manager.init_app(server)
# login_manager.login_view = '/login'

# =========  Layout  =========== #
app.layout = dmc.MantineProvider(
    html.Div(children=[
        dbc.Row([
            dbc.Col([
                dcc.Location(id="base-url", refresh=False), #gestao de páginas
                dcc.Store(id="login-state", data=""),
                dcc.Store(id="register-state", data=""),
                html.Div(id="page-content")
            ]),
        ])
    ], style={"padding": "0px"})
)

#CALLBACKS
#======================================================
# @login_manager.user_loader
# def load_user(user_id):
#     return Users.query.get(int(user_id))


@app.callback(Output("base-url", "pathname"),
    [
        Input("login-state", "data"),
        Input("register-state", "data"),
    ]
)
def render_page_content(login_state, register_state):
    ctx = dash.callback_context
    if ctx.triggered:
        trigg_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if trigg_id == 'login-state' and login_state == "success":
            return '/data'
        if trigg_id == 'login-state' and login_state == "error":
            return '/login'

        if trigg_id == 'register-state':
            if register_state == "":
                return '/login'
            else:
                return '/register'
    else:
        return '/login'


@app.callback(Output("page-content","children"),
            Input("base-url", "pathname"),
            [
                #State("login-state", "data"), 
                State("register-state", "data")
            ]
)
def render_page_content2(pathname, register_state):
    # if pathname == "/login":
    #     if current_user.is_authenticated:
    #         print("login autenticado? {}".format(current_user.is_authenticated))
    #         return data.render_layout()
    #     else:
    #         return login.render_layout(register_state)

    # if pathname == "/register":
    #     if current_user.is_authenticated:
    #         return data.render_layout(current_user.username)
    #     else:
    #         return register.render_layout(register_state)

    if (pathname == "/data" or pathname == "/"):
        return data.render_layout()
        # if current_user.is_authenticated:
        #     print("data autenticado? {}".format(current_user.is_authenticated))
        #     return data.render_layout()
        # else:
        #     return login.render_layout(register_state)
    
    if pathname == "/sucesso":
        return sucesso.render_layout()
        # if current_user.is_authenticated:
        #     return sucesso.render_layout()
        # else:
        #     return login.render_layout(register_state)

#APP RUN
if __name__ == "__main__":
    app.run(debug=True)