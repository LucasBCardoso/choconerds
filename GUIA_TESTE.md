# 🧪 GUIA DE TESTE LOCAL - Choco Nerds!

## Configuração Rápida para Testar

### 1️⃣ Preparar o Ambiente

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar (Windows)
venv\Scripts\activate

# Ativar (Linux/Mac)
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### 2️⃣ Configurar Gist (Teste Rápido)

Se quiser testar sem Gist real (usa dados padrão):

```bash
# Criar arquivo .env com valores vazios
echo GIST_ID=teste > .env
echo GIST_TOKEN=teste >> .env
```

A aplicação carregará dados padrão automaticamente.

### 3️⃣ Configurar Gist (Teste Real)

1. Crie um Gist em https://gist.github.com
2. Arquivo: `data.json`
3. Cole o payload (veja em IMPLEMENTACAO_COMPLETA.md)
4. Copie o ID da URL

```bash
# Editar .env
echo GIST_ID=seu_id_aqui > .env
echo GIST_TOKEN=seu_token_aqui >> .env
```

### 4️⃣ Executar

```bash
python index.py
```

Acesse: **http://localhost:8050**

---

## ✅ TESTE DA FUNCIONALIDADE

### 1. Página Inicial
- [ ] Logo carrega corretamente
- [ ] 5 produtos aparecem
- [ ] Cada produto mostra: nome, sabor, preço, descrição, imagens

### 2. Carrinho
- [ ] Clique em "ACESSAR O CARRINHO" (botão vazio inicialmente)
- [ ] Adicione quantidade em um produto
- [ ] Clique em "ADICIONAR AO CARRINHO"
- [ ] Verifique se o item aparece no carrinho

### 3. Cálculo de Totais
- [ ] Adicione múltiplos produtos
- [ ] Verifique se o cálculo está correto:
  - 1x DARTH VADER = R$6,00
  - 2x GANDALF = R$12,00
  - Total: R$18,00

### 4. WhatsApp
- [ ] Clique em "FECHAR O PEDIDO"
- [ ] Uma nova aba deve abrir no WhatsApp Web
- [ ] Verifique se a mensagem contém:
  - [x] Data e hora
  - [x] Produtos e quantidades
  - [x] Total do pedido
  - [x] Número de contato

### 5. Gist Integration
- [ ] Verifique `app.log` para erros
- [ ] Se não houver GIST_ID/TOKEN, dados padrão devem carregar
- [ ] Se houver credenciais válidas, dados devem vir do Gist

---

## 🔍 VERIFICAÇÃO DO CÓDIGO

### Imports Removidos ✅
```python
# NÃO DEVE EXISTIR:
from flask_sqlalchemy import SQLAlchemy
from flask_login import ...
import psycopg2
```

### Novo Módulo ✅
```python
# DEVE EXISTIR:
from utils import get_products, get_gist_data
```

### Funções Melhoradas ✅
```python
# DEVE INCLUIR:
def calcula_total_carrinho()
def monta_pedido(nome, sabor, quantidade)
```

---

## 📊 VERIFICAÇÃO DO GIST

1. Acesse sua URL do Gist
2. Verifique se contém:
   ```json
   {
     "company": {...},
     "products": [...],
     "schedules": {...},
     "orders": []
   }
   ```

3. Produto exemplo deve ter:
   - `id`, `name`, `flavor`, `price`, `description`

---

## 🚀 TESTE DE DEPLOY (Render)

1. Faça push para GitHub
2. Crie web service no Render
3. Configure variáveis de ambiente:
   - `GIST_ID`
   - `GIST_TOKEN`
   - `PYTHON_VERSION`
   - `PORT`

4. Deploy automático
5. Acesse a URL fornecida
6. Repita testes de funcionalidade

---

## 🐛 POSSÍVEIS ERROS E SOLUÇÕES

### Erro: "ModuleNotFoundError: No module named 'utils'"

**Solução**: Certifique-se que `utils.py` está na raiz do projeto

### Erro: "GIST_ID ou GIST_TOKEN não configurados"

**Solução**: Crie arquivo `.env` com:
```
GIST_ID=seu_id
GIST_TOKEN=seu_token
```

### Erro: 404 ao acessar Gist

**Soluções**:
1. Verifique se o Gist é **público**
2. Confirme GIST_ID correto
3. Valide token GitHub

### Carrinho vazio mesmo após adicionar

**Soluções**:
1. Limpe cache: `Ctrl+Shift+Delete`
2. Recarregue página: `Ctrl+F5`
3. Verifique console do navegador (F12)

### Produtos não carregam

**Soluções**:
1. Verifique `app.log` para erros
2. Acesse diretamente: http://localhost:8050/data
3. Confirme dados padrão ou Gist

---

## 📱 TESTE COM DISPOSITIVOS REAIS

### Mobile
1. Obtenha IP local: `ipconfig` (Windows) ou `ifconfig` (Linux)
2. Acesse: `http://seu_ip:8050`
3. Teste em celular na mesma rede

### WhatsApp
1. Teste em dispositivo com WhatsApp instalado
2. Verifique formatação da mensagem
3. Confirme número de contato

---

## ✨ CHECKLIST DE TESTE COMPLETO

- [ ] Ambiente virtual criado
- [ ] Dependências instaladas
- [ ] Arquivo .env configurado
- [ ] Aplicação inicia sem erros
- [ ] Página carrega completamente
- [ ] 5 produtos visíveis
- [ ] Carrinho funciona
- [ ] Cálculo de totais correto
- [ ] WhatsApp abre com mensagem formatada
- [ ] Logs não mostram erros críticos
- [ ] Gist data carrega (se configurado)
- [ ] Deploy em Render bem-sucedido
- [ ] Tudo funciona em dispositivo mobile

---

## 📞 PRÓXIMOS PASSOS

1. ✅ Testar localmente
2. ✅ Configurar Gist real
3. ✅ Fazer deploy no Render
4. ✅ Testar em produção
5. ✅ Compartilhar link com clientes

**Pronto? Comece agora com:**
```bash
python index.py
```

Boa sorte! 🍫✨
