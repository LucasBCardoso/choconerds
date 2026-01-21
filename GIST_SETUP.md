# 📊 Configuração do Gist - Choco Nerds!

## Passo a Passo para Configurar o Banco de Dados

Este guia te ajudará a configurar o Gist GitHub que será usado como banco de dados para a aplicação Choco Nerds!

### Pré-requisitos

✅ Conta GitHub  
✅ Permissão para criar Gists  
✅ Token de acesso pessoal do GitHub

---

## 1️⃣ Criar um Token de Acesso no GitHub

### Passos:

1. Acesse [GitHub Settings](https://github.com/settings/tokens)
2. Clique em **"Generate new token"** (Classic)
3. Dê um nome descritivo, ex: `choconerds-gist-token`
4. Selecione a permissão **`gist`**
5. Clique em **"Generate token"**
6. **Copie e guarde o token** (você não poderá vê-lo novamente)

⚠️ **Nunca compartilhe este token!**

---

## 2️⃣ Criar um Novo Gist

### Passos:

1. Acesse [gist.github.com](https://gist.github.com)
2. Clique em **"Create a new gist"**
3. No campo "Gist description", coloque: `Choco Nerds Database`
4. No campo "Filename", coloque: `data.json`
5. Cole o conteúdo JSON abaixo
6. Marque **"Public"** (necessário para a aplicação acessar)
7. Clique em **"Create public gist"**

### Copie o ID do Gist

A URL do seu gist será algo como:  
`https://gist.github.com/seu_usuario/12345abcde`

O ID é a parte `12345abcde`

---

## 3️⃣ Estrutura do JSON do Gist

Cole exatamente este JSON no seu Gist:

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

---

## 4️⃣ Configurar Variáveis de Ambiente

### No Render.com (Deploy em Produção)

1. Acesse seu painel do Render
2. Selecione a aplicação "choconerds"
3. Vá para **Settings → Environment**
4. Adicione as seguintes variáveis:

| Variável | Valor |
|----------|-------|
| `GIST_ID` | Seu ID do Gist (ex: 12345abcde) |
| `GIST_TOKEN` | Token do GitHub que você criou |
| `PYTHON_VERSION` | 3.10.9 |
| `PORT` | 10000 |

5. Salve e redeploy a aplicação

### No Arquivo render.yaml (Alternativa)

O arquivo já está pré-configurado. Apenas substitua:
- `SEU_GIST_ID_AQUI` → seu ID do Gist
- `SEU_GITHUB_TOKEN_AQUI` → seu token

---

## 5️⃣ Testar a Conexão

Para verificar se tudo está funcionando:

1. Execute a aplicação localmente
2. Se a página carregar com os produtos, está funcionando! ✅
3. Se houver erro, verifique:
   - O GIST_ID está correto?
   - O GIST_TOKEN está correto?
   - O Gist está marcado como **Public**?
   - O arquivo no Gist é realmente `data.json`?

---

## 🎨 Personalizar os Dados

### Mudar Número de Contato

No seu Gist, encontre:
```json
"phone": "+5553984298702"
```

Mude para seu número:
```json
"phone": "+55XXXXXXXXXXX"
```

### Adicionar Novo Produto

Adicione um novo objeto ao array `products`:
```json
{
  "id": 6,
  "name": "NOVO PRODUTO",
  "flavor": "SABOR",
  "price": "R$ 6,00",
  "description": "Descrição do novo produto",
  "image": "/assets/novo.png",
  "carousel": "/assets/novo_carousel.jpg"
}
```

### Mudar Horários

Edite o objeto `schedules`. Os horários vazios devem ser `" "`:

```json
"Segunda": [" ", "08:30", " ", "19:00", "20:00"]
```

---

## ✅ Checklist Final

- [ ] Token GitHub criado
- [ ] Gist criado e público
- [ ] ID do Gist obtido
- [ ] Variáveis de ambiente configuradas
- [ ] Aplicação testada localmente
- [ ] Aplicação deployada no Render
- [ ] Pedidos podem ser enviados ao WhatsApp

---

## 📞 Precisa de Ajuda?

Se tiver problemas:

1. **Erro 401**: Token inválido ou expirado
2. **Erro 404**: Gist ID inválido ou privado
3. **Sem dados**: Arquivo JSON com formatação incorreta

Verifique o arquivo de logs `app.log` para mais detalhes.

---

**Versão**: 2.0  
**Data**: 21 de janeiro de 2026
