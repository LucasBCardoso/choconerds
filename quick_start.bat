@echo off
REM Quick Start Guide - Choco Nerds! (Windows)
REM Execute este arquivo para configurar o ambiente rapidamente

echo.
echo Choco Nerds - Configuracao Rapida
echo ===================================
echo.

REM Verificar se Python está instalado
echo [*] Verificando Python...
python --version

REM Criar ambiente virtual
echo [*] Criando ambiente virtual...
python -m venv venv

REM Ativar ambiente virtual
echo [*] Ativando ambiente virtual...
call venv\Scripts\activate.bat

REM Instalar dependências
echo [*] Instalando dependencias...
pip install -r requirements.txt

REM Criar arquivo .env
echo [*] Criando arquivo .env...
if not exist .env (
    copy .env.example .env
    echo.
    echo [!] IMPORTANTE: Edite o arquivo .env com suas credenciais:
    echo     - GIST_ID: ID do seu Gist
    echo     - GIST_TOKEN: Token de acesso GitHub
    echo.
    echo Instrucoes completas em: GIST_SETUP.md
    pause
)

REM Iniciar aplicação
echo.
echo [*] Iniciando a aplicacao...
echo [*] Acesse: http://localhost:8050
echo.
python index.py

pause
