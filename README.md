# 🍫 Choco Nerds

Uma aplicação web para venda de brownies artesanais com temática geek/nerd.

## 📋 Sobre o Projeto

Choco Nerds é um e-commerce de brownies temáticos, desenvolvido com Python e Dash. Os brownies possuem nomes inspirados em personagens icônicos da cultura pop como Darth Vader, Gandalf, Spock, Wookie e Sauron.

## 🚀 Tecnologias

- **Python 3.10+**
- **Dash 3.0+** - Framework web
- **Dash Mantine Components 2.4** - Componentes UI modernos
- **Dash Bootstrap Components** - Componentes Bootstrap
- **Flask** - Backend web
- **Flask-SQLAlchemy** - ORM para banco de dados
- **PostgreSQL** - Banco de dados
- **Pandas** - Manipulação de dados

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/choconerds.git
cd choconerds
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

5. Execute a aplicação:
```bash
python index.py
```

6. Acesse no navegador: `http://127.0.0.1:8050`

## 🔧 Variáveis de Ambiente

| Variável | Descrição |
|----------|-----------|
| `DATABASE_URL` | URL de conexão com o banco PostgreSQL |
| `SECRET_KEY` | Chave secreta para sessões Flask |

## 📁 Estrutura do Projeto

```
choconerds/
├── app.py              # Inicialização do Dash app
├── index.py            # Layout principal e roteamento
├── create_database.py  # Script de criação do banco
├── requirements.txt    # Dependências do projeto
├── assets/
│   └── styles.css      # Estilos customizados
├── pages/
│   ├── data.py         # Página principal com produtos
│   ├── login.py        # Página de login
│   ├── register.py     # Página de registro
│   ├── perfil.py       # Página de perfil
│   ├── gerencia.py     # Painel de gerenciamento
│   ├── finalizar.py    # Finalização de pedido
│   └── sucesso.py      # Página de sucesso
└── static/             # Arquivos estáticos
```

## 🍪 Produtos

- **Darth Vader** - Brownie tradicional com cobertura de chocolate
- **Gandalf** - Brownie com nozes e caramelo
- **Spock** - Brownie com menta e chocolate branco
- **Wookie** - Brownie com cookies e cream
- **Sauron** - Brownie com pimenta e especiarias

## 👤 Autor

**Lucas Cardoso**
- Website: [lucasbcardoso.com.br](https://www.lucasbcardoso.com.br)

## 📝 Licença

Este projeto está sob a licença MIT.

---

**2026 v2.0 | Choco Nerds!**
