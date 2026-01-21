#!/bin/bash
# Quick Start Guide - Choco Nerds!
# Execute este script para configurar o ambiente rapidamente

echo "🍫 Choco Nerds - Configuração Rápida"
echo "===================================="
echo ""

# Verificar se Python está instalado
echo "✓ Verificando Python..."
python --version

# Criar ambiente virtual
echo "✓ Criando ambiente virtual..."
python -m venv venv

# Ativar ambiente virtual
echo "✓ Ativando ambiente virtual..."
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate  # Windows

# Instalar dependências
echo "✓ Instalando dependências..."
pip install -r requirements.txt

# Criar arquivo .env
echo "✓ Criando arquivo .env..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo "⚠️  IMPORTANTE: Edite o arquivo .env com suas credenciais:"
    echo "  - GIST_ID: ID do seu Gist"
    echo "  - GIST_TOKEN: Token de acesso GitHub"
    echo ""
    echo "Instruções completas em: GIST_SETUP.md"
fi

# Iniciar aplicação
echo ""
echo "✓ Iniciando a aplicação..."
echo "📱 Acesse: http://localhost:8050"
echo ""
python index.py
