"""
Página de Finalização - Choco Nerds!
Exibe confirmação de pedido e opção de compartilhar/salvar
"""

from dash import html, dcc, callback
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash_iconify import DashIconify

from app import app, carrinho
from utils import save_order_to_gist, get_company_info
from datetime import datetime
import urllib.parse

company_info = get_company_info()


def calcula_total_pedido():
    """Calcula total de todos os itens no carrinho"""
    total = 0
    for pedido in carrinho:
        try:
            linhas = pedido.split('\n')
            total_str = linhas[2].split('R$')[1].strip()
            total += float(total_str.replace(',', '.'))
        except:
            pass
    return total


def formata_pedido_exibicao():
    """Formata pedido para exibição na página"""
    items = []
    
    if not carrinho:
        return html.P("Carrinho vazio", style={"textAlign": "center", "color": "#999"})
    
    for idx, pedido in enumerate(carrinho):
        try:
            linhas = pedido.split('\n')
            nome = linhas[0].strip('*').strip()
            qtd = linhas[0].split(':')[1].strip() if ':' in linhas[0] else "1"
            sabor = linhas[1].split(': ')[1] if len(linhas) > 1 else ""
            total = linhas[2].split(': ')[1] if len(linhas) > 2 else "R$0,00"
            
            item = dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.H5(nome, className="card-title"),
                            html.P(f"Quantidade: {qtd} un.", style={"fontSize": "14px"}),
                            html.P(f"Sabor: {sabor}", style={"fontSize": "14px"}),
                            html.P(f"Total: {total}", style={"fontSize": "16px", "fontWeight": "bold", "color": "#d64545"}),
                        ]
                    )
                ],
                className="mb-2"
            )
            items.append(item)
        except Exception as e:
            print(f"Erro ao formatar item: {e}")
            continue
    
    return html.Div(items)


#========== LAYOUT

def render_layout():
    """Layout da página de finalização"""
    total = calcula_total_pedido()
    
    return html.Div([
        dcc.Location(id='url-finalizar', refresh=False),
        
        # Header
        dbc.Row([
            dbc.Col([
                html.Div([
                    dbc.CardImg(src="/assets/logo.png", class_name="logotipo"),
                ], style={'textAlign': 'center'}, className="logo-agenda"),
            ], className="d-flex justify-content-center")
        ], className="lowbar mb-4"),
        
        # Container principal
        dbc.Container([
            # Título
            html.Div([
                html.H2("Seu Pedido", style={"textAlign": "center", "fontWeight": "bold", "marginBottom": "30px"}),
            ]),
            
            # Itens do carrinho
            dbc.Row([
                dbc.Col([
                    html.H5("Itens do Pedido:", style={"marginBottom": "15px"}),
                    formata_pedido_exibicao(),
                ], md=8),
                
                # Resumo
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H6("Resumo", style={"fontWeight": "bold"}),
                            html.Hr(),
                            html.P(f"Subtotal: R${total:.2f}", style={"fontSize": "14px"}),
                            html.P(f"Entrega: A combinar", style={"fontSize": "14px"}),
                            html.Hr(),
                            html.H5(f"Total: R${total:.2f}", style={"fontWeight": "bold", "color": "#d64545"}),
                            html.Hr(),
                            html.P("Data do Pedido:", style={"fontSize": "12px", "color": "#999"}),
                            html.P(datetime.now().strftime("%d/%m/%Y %H:%M"), style={"fontSize": "12px", "color": "#999"}),
                        ])
                    ], className="mt-3")
                ], md=4),
            ], className="mb-4"),
            
            # Botões de ação
            dbc.Row([
                dbc.Col([
                    html.A([
                        dmc.Button(
                            "Enviar pelo WhatsApp",
                            id="btn-whatsapp-finalizar",
                            variant="gradient",
                            gradient={"from": "green", "to": "lime", "deg": 105},
                            fullWidth=True,
                            size="lg",
                            radius="lg",
                            leftSection=DashIconify(icon="mdi:whatsapp", width=24)
                        )
                    ], id="link-whatsapp", href="#", target="_blank", style={"textDecoration": "none"})
                ], md=6, className="mb-2"),
                
                dbc.Col([
                    dmc.Button(
                        "Salvar Pedido",
                        id="btn-salvar-pedido",
                        variant="outline",
                        fullWidth=True,
                        size="lg",
                        radius="lg",
                        leftSection=DashIconify(icon="mdi:content-save", width=24)
                    )
                ], md=6, className="mb-2"),
            ], className="mb-4"),
            
            # Botão voltar
            dbc.Row([
                dbc.Col([
                    html.A([
                        dmc.Button(
                            "Voltar e Adicionar Mais",
                            variant="subtle",
                            fullWidth=True,
                            size="md",
                            radius="lg",
                            leftSection=DashIconify(icon="mdi:arrow-left", width=20)
                        )
                    ], href="/data", style={"textDecoration": "none"})
                ], md=12),
            ]),
            
            # Aviso
            dbc.Row([
                dbc.Col([
                    dmc.Alert(
                        "Seu pedido será processado assim que for enviado pelo WhatsApp. Nossa equipe entrará em contato para confirmar detalhes e formas de pagamento.",
                        title="Informação",
                        color="info",
                        style={"marginTop": "30px"}
                    )
                ], md=12)
            ]),
            
        ], fluid=True, className="content"),
        
        # Divider
        html.Div([], style={"padding": "20px"}),
        
        # Footer
        html.Div([
            html.A(
                "Criado por Lucas Cardoso",
                href="https://www.lucasbcardoso.com.br",
                target="_blank",
                style={"fontFamily": "Arial", "fontSize": "12px", "color": "#666", "textDecoration": "none"}
            ),
        ], style={"display": "flex", "justifyContent": "center", "padding": "20px"}),
        
    ], style={"display": "block"})




# Callback para gerar link WhatsApp
@app.callback(
    Output("link-whatsapp", "href"),
    Input("btn-whatsapp-finalizar", "n_clicks"),
    prevent_initial_call=True
)
def gera_link_whatsapp(n_clicks):
    """Gera link de compartilhamento WhatsApp com pedido formatado"""
    from pages.data import text_format
    
    try:
        texto = text_format()
        phone_number = company_info.get('phone', '+5553984298702').replace('+', '').replace(' ', '')
        url = f"https://wa.me/{phone_number}/?text={urllib.parse.quote(texto)}"
        return url
    except Exception as e:
        print(f"Erro ao gerar link WhatsApp: {e}")
        return "#"


# Callback para salvar pedido no Gist
@app.callback(
    Output("btn-salvar-pedido", "children"),
    Input("btn-salvar-pedido", "n_clicks"),
    prevent_initial_call=True
)
def salva_pedido_gist(n_clicks):
    """Salva pedido no Gist e exibe confirmação"""
    if n_clicks:
        try:
            from pages.data import calcula_total_carrinho
            
            total = calcula_total_carrinho()
            ordem_items = []
            
            for pedido in carrinho:
                try:
                    linhas = pedido.split('\n')
                    nome = linhas[0].strip('*').strip()
                    qtd = linhas[0].split(':')[1].strip() if ':' in linhas[0] else "1"
                    sabor = linhas[1].split(': ')[1] if len(linhas) > 1 else ""
                    ordem_items.append({
                        "produto": nome,
                        "quantidade": int(qtd),
                        "sabor": sabor
                    })
                except:
                    pass
            
            order_data = {
                "items": ordem_items,
                "total": total,
                "status": "novo"
            }
            
            success = save_order_to_gist(order_data)
            
            if success:
                return [
                    DashIconify(icon="mdi:check-circle", width=20),
                    " Salvo com Sucesso!"
                ]
            else:
                return [
                    DashIconify(icon="mdi:alert-circle", width=20),
                    " Erro ao Salvar"
                ]
        except Exception as e:
            print(f"Erro ao salvar pedido: {e}")
            return [
                DashIconify(icon="mdi:alert-circle", width=20),
                " Erro ao Salvar"
            ]
    
    return [
        DashIconify(icon="mdi:content-save", width=20),
        " Salvar Pedido"
    ]
