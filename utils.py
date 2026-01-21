"""
Utilitários para conectar com Gist e gerenciar dados
"""
import os
import requests
import json
import pandas as pd
from datetime import date, datetime, timedelta

GIST_ID = os.environ.get('GIST_ID', '')
GIST_TOKEN = os.environ.get('GIST_TOKEN', '')

def get_gist_data():
    """
    Lê os dados do Gist via API oficial e retorna como dicionário.
    Usa 'content' do arquivo quando disponível; caso contrário, baixa pelo 'raw_url'.
    """
    try:
        if not GIST_ID:
            print("Erro: GIST_ID não configurado")
            return None
        
        url = f"https://api.github.com/gists/{GIST_ID}"
        headers = {"Accept": "application/vnd.github+json"}
        if GIST_TOKEN:
            headers["Authorization"] = f"Bearer {GIST_TOKEN}"
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            gist_data = response.json()
            files = gist_data.get('files', {})
            target = None
            if 'data.json' in files:
                target = files['data.json']
            else:
                for filename, meta in files.items():
                    if filename.lower().endswith('.json'):
                        target = meta
                        break
            
            if not target:
                print("Erro: Nenhum arquivo .json encontrado no Gist")
                return None
            
            content = target.get('content')
            if content:
                return json.loads(content)
            
            raw_url = target.get('raw_url')
            if raw_url:
                raw_headers = {}
                if GIST_TOKEN:
                    raw_headers["Authorization"] = f"Bearer {GIST_TOKEN}"
                raw_resp = requests.get(raw_url, headers=raw_headers)
                if raw_resp.status_code == 200:
                    return raw_resp.json()
                else:
                    print(f"Erro ao baixar conteúdo bruto do Gist: {raw_resp.status_code}")
                    return None
            
            print("Erro: Arquivo alvo não possui 'content' nem 'raw_url'")
            return None
        else:
            print(f"Erro ao acessar Gist: {response.status_code}")
            return None
    except Exception as e:
        print(f"Erro ao obter dados do Gist: {e}")
        return None

def get_products():
    """
    Retorna os produtos do Gist
    """
    data = get_gist_data()
    if data and 'products' in data:
        return pd.DataFrame(data['products'])
    else:
        # Dados padrão se Gist não estiver disponível
        return pd.DataFrame({
            0: ["1", "2", "3", "4", "5"],
            1:["DARTH VADER","GANDALF, O BRANCO","SPOCK, O SÁBIO","WOOKIE, O AVENTUREIRO", "SAURON, O SOMBRIO"],
            2:["BRIGADEIRO","NINHO","DUO (BRIGADEIRO E NINHO)","DOCE DE LEITE", "NUTELLA"],
            3:["R$ 6,00", "R$ 6,00", "R$ 6,00", "R$ 6,00", "R$ 6,00"],
            4:["Brownie 6X6 com muuuuito recheio de BRIGADEIRO para fazer a aliança rebelde tremer de medo!",
                "Brownie 6X6 com muuuuito recheio de NINHO para derrotar as forças de Sauron e salvar a terra média!",
                "Brownie 6X6 com muuuuito recheio DUO (BRIGADEIRO E NINHO) para ir onde ninguém jamais esteve!",
                "Brownie 6X6 com muuuuito recheio de DOCE DE LEITE para as suas aventuras em uma galáxia muito, muito distante!",
                "Brownie 6X6 com muuuuito recheio de NUTELLA para a todos os brownies comandar!"],
            5:["/assets/p1.png","/assets/p2.png","/assets/p3.png","/assets/p4.png","/assets/p5.png"],
            6:["/assets/br0.jpg","/assets/br1.jpg","/assets/br2.jpg","/assets/br0.jpg","/assets/br0.jpg"],
        })

def save_order_to_gist(order_data):
    """
    Salva um novo pedido no Gist
    """
    try:
        if not GIST_ID or not GIST_TOKEN:
            print("Erro: GIST_ID ou GIST_TOKEN não configurados")
            return False
        
        url = f"https://api.github.com/gists/{GIST_ID}"
        headers = {"Authorization": f"token {GIST_TOKEN}"}
        
        # Obtém dados atuais do Gist
        data = get_gist_data()
        if data is None:
            data = {"orders": []}
        
        # Adiciona novo pedido
        if 'orders' not in data:
            data['orders'] = []
        
        order_data['timestamp'] = datetime.now().isoformat()
        data['orders'].append(order_data)
        
        # Prepara o payload para atualizar o Gist
        files = {
            "data.json": {
                "content": json.dumps(data, indent=2, ensure_ascii=False)
            }
        }
        
        response = requests.patch(url, headers=headers, json={"files": files})
        
        if response.status_code == 200:
            print("Pedido salvo com sucesso no Gist")
            return True
        else:
            print(f"Erro ao salvar pedido no Gist: {response.status_code}")
            return False
    except Exception as e:
        print(f"Erro ao salvar pedido: {e}")
        return False

def get_schedules():
    """
    Retorna os horários de treino do Gist
    """
    data = get_gist_data()
    if data and 'schedules' in data:
        return pd.DataFrame(data['schedules'])
    else:
        # Dados padrão
        return pd.DataFrame({
            "Segunda":[" ","08:30"," ","19:00","20:00"],
            "Terça":[" "," "," ","19:00","20:00"],
            "Quarta":[" ","08:30"," ","19:00","20:00"],
            "Quinta":[" ","08:30"," ","19:00"," "],
            "Sexta":[" ","08:30"," ","19:00","20:00"],
            "Sábado":["Não há treinos hoje."," "," "," "," "],
            "Domingo":["Não há treinos hoje."," "," "," "," "]
        })

def get_company_info():
    """
    Retorna as informações da empresa
    """
    data = get_gist_data()
    if data and 'company' in data:
        return data['company']
    else:
        return {
            "name": "Choco Nerds!",
            "phone": "+5553984298702",
            "email": "contato@choconerds.com.br",
            "version": "2.0"
        }
