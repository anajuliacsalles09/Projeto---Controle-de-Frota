# Controle de Frota

Projeto Django para gerenciar usuarios, veiculos, viagens, cargas, abastecimentos, manutencoes e despesas.

## Instalacao local (PowerShell)

Requer Python 3.12 ou superior.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py createsuperuser
.\.venv\Scripts\python.exe manage.py runserver
```

Acesse http://127.0.0.1:8000/.

## Configuracao local

Defina `DJANGO_SECRET_KEY` no ambiente para fornecer sua propria chave. Sem essa variavel, o Django gera uma chave persistente no arquivo local `.django-secret-key`, ignorado pelo Git. Arquivos `.env` nao sao carregados automaticamente.

O banco `db.sqlite3`, os caches Python e o ambiente virtual permanecem somente na maquina. Ao clonar o projeto, execute as migracoes para criar um banco novo. As migracoes Python devem continuar versionadas.

As configuracoes atuais (`DEBUG = True` e `ALLOWED_HOSTS = []`) sao para desenvolvimento local. Uma publicacao exige configuracao de producao.

## Git

A branch `main` acompanha `origin/main`. Antes de enviar alteracoes:

```powershell
git status
git diff
git diff --cached
```

A remocao do banco e dos caches do versionamento preserva os arquivos locais, mas nao remove copias de commits antigos. A chave anteriormente escrita no codigo foi substituida; o historico remoto nao foi reescrito.
