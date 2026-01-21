# 🍫 Choco Nerds! - Sistema de Pedidos

Sistema web moderno para gerenciamento de pedidos de brownies temáticos com interface interativa e integração com Gist GitHub para armazenamento de dados.

## 📋 Sobre o Projeto

**Choco Nerds!** é uma aplicação web desenvolvida com Dash/Flask que permite aos clientes navegar por um catálogo de brownies temáticos e realizar pedidos através do WhatsApp. O sistema utiliza Gist GitHub como banco de dados, eliminando a necessidade de um servidor de banco de dados dedicado.

### Características Principais

- 🎯 **Interface Intuitiva**: Design responsivo e moderno com Dash Mantine Components
- 🛒 **Carrinho Funcional**: Sistema de carrinho melhorado com cálculo automático de totais
- 📱 **Integração WhatsApp**: Envio de pedidos direto para WhatsApp com formatação automática
- ☁️ **Armazenamento em Gist**: Dados persistentes usando Gist GitHub
- 🎨 **5 Sabores Únicos**: Darth Vader, Gandalf, Spock, Wookie e Sauron
- 💰 **Preço Fixo**: R$ 6,00 por unidade

## 🚀 Início Rápido

### Pré-requisitos

- Python 3.10+
- Conta GitHub (para criar um Gist)
- Token de acesso GitHub (Personal Access Token)

### Instalação Local

1. **Clone ou baixe o projeto**
   ```bash
   cd choconerds
   ```

2. **Crie um ambiente virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente**
   Crie um arquivo `.env` na raiz do projeto:
   ```
   GIST_ID=seu_gist_id_aqui
   GIST_TOKEN=seu_github_token_aqui
   SECRET_KEY=sua_chave_secreta_aqui
   ```

5. **Execute a aplicação**
   ```bash
   python index.py
   ```

A aplicação estará disponível em `http://localhost:8050`

## 🗂️ Estrutura de Arquivos

```
choconerds/
├── app.py                 # Configuração principal do Dash/Flask
├── index.py              # Ponto de entrada da aplicação
├── utils.py              # Funções utilitárias para Gist e carrinho
├── requirements.txt      # Dependências Python
├── render.yaml           # Configuração de deploy no Render
├── pages/
│   ├── data.py          # Página principal com catálogo de produtos
│   ├── login.py         # Página de login
│   ├── register.py      # Página de registro
│   ├── perfil.py        # Página de perfil do usuário
│   ├── gerencia.py      # Página de gerenciamento
│   ├── finalizar.py     # Página de finalização
│   └── sucesso.py       # Página de sucesso
├── assets/
│   ├── styles.css       # Estilos personalizados
│   ├── logo.png         # Logo da marca
│   └── produtos/        # Imagens dos produtos
└── static/              # Arquivos estáticos
```

## 📊 Configuração do Gist

O sistema armazena todos os dados em um único arquivo Gist no GitHub. Aqui está o formato necessário:

### 1. Crie um Gist no GitHub

Acesse [gist.github.com](https://gist.github.com) e crie um novo Gist com o arquivo `data.json`.

### 2. Payload Inicial do Gist

```json
{
  "company": {
    "name": "Choco Nerds!",
    "phone": "+5553984298702",
    "email": "contato@choconerds.com.br",
    "version": "2.0"
  },
  "products": [
    {
      "id": 1,
      "name": "DARTH VADER",
      "flavor": "BRIGADEIRO",
      "price": "R$ 6,00",
      "description": "Brownie 6X6 com muuuuito recheio de BRIGADEIRO para fazer a aliança rebelde tremer de medo!",
      "image": "/assets/p1.png",
      "carousel": "/assets/br0.jpg"
    },
    {
      "id": 2,
      "name": "GANDALF, O BRANCO",
      "flavor": "NINHO",
      "price": "R$ 6,00",
      "description": "Brownie 6X6 com muuuuito recheio de NINHO para derrotar as forças de Sauron e salvar a terra média!",
      "image": "/assets/p2.png",
      "carousel": "/assets/br1.jpg"
    },
    {
      "id": 3,
      "name": "SPOCK, O SÁBIO",
      "flavor": "DUO (BRIGADEIRO E NINHO)",
      "price": "R$ 6,00",
      "description": "Brownie 6X6 com muuuuito recheio DUO (BRIGADEIRO E NINHO) para ir onde ninguém jamais esteve!",
      "image": "/assets/p3.png",
      "carousel": "/assets/br2.jpg"
    },
    {
      "id": 4,
      "name": "WOOKIE, O AVENTUREIRO",
      "flavor": "DOCE DE LEITE",
      "price": "R$ 6,00",
      "description": "Brownie 6X6 com muuuuito recheio de DOCE DE LEITE para as suas aventuras em uma galáxia muito, muito distante!",
      "image": "/assets/p4.png",
      "carousel": "/assets/br0.jpg"
    },
    {
      "id": 5,
      "name": "SAURON, O SOMBRIO",
      "flavor": "NUTELLA",
      "price": "R$ 6,00",
      "description": "Brownie 6X6 com muuuuito recheio de NUTELLA para a todos os brownies comandar!",
      "image": "/assets/p5.png",
      "carousel": "/assets/br0.jpg"
    }
  ],
  "schedules": {
    "Segunda": [" ", "08:30", " ", "19:00", "20:00"],
    "Terça": [" ", " ", " ", "19:00", "20:00"],
    "Quarta": [" ", "08:30", " ", "19:00", "20:00"],
    "Quinta": [" ", "08:30", " ", "19:00", " "],
    "Sexta": [" ", "08:30", " ", "19:00", "20:00"],
    "Sábado": ["Não há treinos hoje.", " ", " ", " ", " "],
    "Domingo": ["Não há treinos hoje.", " ", " ", " ", " "]
  },
  "orders": []
}
```

### 3. Obtenha suas Credenciais

**GIST_ID**: 
- Abra seu Gist no GitHub
- A URL será: `https://gist.github.com/seu_usuario/SEU_GIST_ID`
- Copie a parte `SEU_GIST_ID`

**GIST_TOKEN**:
1. Vá para [GitHub Settings → Developer settings → Personal access tokens](https://github.com/settings/tokens)
2. Clique em "Generate new token"
3. Marque a permissão `gist`
4. Clique em "Generate token" e copie o token

## 🛒 Sistema de Carrinho Melhorado

O carrinho agora inclui:

- ✅ Adição de produtos com quantidade customizável
- ✅ Cálculo automático de totais
- ✅ Visualização elegante de itens
- ✅ Remoção de itens
- ✅ Geração automática de mensagem WhatsApp formatada
- ✅ Informações de contato incluídas automaticamente

### Exemplo de Mensagem Gerada

```
Sistema de pedidos da *Choco Nerds!*
---------------------------
Pedido iniciado em: 
*Segunda, 20/01/2026 às 14:30:45*

*Dados do pedido:* 
---------------------------
*DARTH VADER*, qtd: 2un.
Sabor: BRIGADEIRO
Total: R$12.00
---------------------------
*GANDALF, O BRANCO*, qtd: 1un.
Sabor: NINHO
Total: R$6.00
---------------------------

*TOTAL DO PEDIDO: R$18.00*
---------------------------
Contato: +5553984298702
```

## 🌐 Deploy no Render

1. **Crie uma conta em [Render](https://render.com)**

2. **Conecte seu repositório GitHub**

3. **Configure as variáveis de ambiente:**
   - `GIST_ID`: ID do seu Gist
   - `GIST_TOKEN`: Token GitHub
   - `PYTHON_VERSION`: 3.10.9

4. **Deploy automático**
   - Render detectará o arquivo `render.yaml` e fará o deploy automático

## 📦 Dependências

| Pacote | Versão | Descrição |
|--------|--------|-----------|
| dash | >=3.0.0 | Framework web interativo |
| dash-bootstrap-components | >=1.6.0 | Componentes Bootstrap para Dash |
| dash-mantine-components | >=2.4.0 | Componentes Mantine para Dash |
| Flask | >=3.0.0 | Servidor web WSGI |
| pandas | >=2.2.0 | Manipulação de dados |
| plotly | >=5.24.0 | Gráficos interativos |
| requests | >=2.32.0 | Requisições HTTP para Gist |
| gunicorn | >=23.0.0 | Servidor de produção |

## 🔧 Variáveis de Ambiente

| Variável | Descrição | Obrigatória |
|----------|-----------|------------|
| `GIST_ID` | ID do Gist GitHub | ✅ Sim |
| `GIST_TOKEN` | Token de acesso GitHub | ✅ Sim |
| `SECRET_KEY` | Chave secreta para Flask | ⚠️ Recomendado |
| `PYTHON_VERSION` | Versão do Python | ❌ Não |
| `PORT` | Porta da aplicação | ❌ Não (padrão: 8050) |

## 📱 Integração WhatsApp

O sistema gera automaticamente um link WhatsApp que:

1. Abre o WhatsApp Web ou App
2. Pré-preenche a mensagem com os dados do pedido
3. Envia para o número configurado no Gist

O número padrão é: **+55 53 98429-8702**

Para alterar, edite o arquivo `data.json` do seu Gist na chave `company.phone`.

## 🎨 Personalização

### Alterar Número de Contato

No seu Gist `data.json`:
```json
"company": {
  "phone": "+seu_numero_aqui"
}
```

### Alterar Produtos

Edite o array `products` no Gist com novos sabores e descrições.

### Alterar Horários

Edite o objeto `schedules` no Gist com os horários desejados.

## 🐛 Troubleshooting

**Erro: "GIST_ID ou GIST_TOKEN não configurados"**
- Verifique se as variáveis de ambiente estão definidas
- Confirme que o token GitHub tem permissão `gist`

**Erro: 404 ao acessar o Gist**
- Confirme que o GIST_ID está correto
- Verifique que o Gist é público ou que o token tem acesso

**Carrinho não atualiza**
- Limpe o cache do navegador
- Reinicie a aplicação

## 📄 Licença

Projeto desenvolvido para uso comercial.

## 👨‍💻 Desenvolvedor

**Lucas Cardoso**
- Website: [lucasbcardoso.com.br](https://www.lucasbcardoso.com.br)

---

**Versão**: 2.0  
**Data de Atualização**: 21 de janeiro de 2026  
**Status**: ✅ Ativo e Mantido


5. Execute a aplicação:

```bash
python index.py
```

6. Acesse no navegador: `http://127.0.0.1:8050`

## 🔧 Variáveis de Ambiente

| Variável       | Descrição                             |
| -------------- | ------------------------------------- |
| `DATABASE_URL` | URL de conexão com o banco PostgreSQL |
| `SECRET_KEY`   | Chave secreta para sessões Flask      |

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

## � Deploy no Render

1. Faça fork deste repositório no GitHub

2. Acesse [render.com](https://render.com) e crie uma conta

3. Clique em **New** → **Blueprint** e conecte seu repositório

4. O Render vai detectar o `render.yaml` e configurar automaticamente:

   - Banco de dados PostgreSQL
   - Serviço web Python
   - Variáveis de ambiente

5. Clique em **Apply** e aguarde o deploy

### Deploy Manual

1. Crie um **Web Service** no Render:

   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn index:server --bind 0.0.0.0:$PORT`

2. Adicione as variáveis de ambiente:
   - `DATABASE_URL` - URL do PostgreSQL
   - `SECRET_KEY` - Chave secreta (gere uma aleatória)

## �📝 Licença

Este projeto está sob a licença MIT.

---

**2026 v2.0 | Choco Nerds!**
