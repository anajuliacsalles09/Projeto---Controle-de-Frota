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

## Permissoes dos funcionarios

Ao salvar um `Usuario` do tipo `FUNCIONARIO`, o sistema vincula a conta
automaticamente ao grupo `Funcionario`. A migracao `usuario.0005` tambem
configura esse grupo e vincula os funcionarios existentes.

O acesso padrao permite adicionar e visualizar abastecimentos, despesas,
manutencoes e viagens, e visualizar cargas e veiculos. Nao concede edicao,
exclusao ou gerenciamento de usuarios. Menus e botoes respeitam as permissoes;
as views continuam verificando o acesso no servidor.

Permissoes adicionais concedidas manualmente por outros grupos ou diretamente
ao usuario continuam valendo. Alterar o tipo para `ADMIN` remove o vinculo com
o grupo `Funcionario`; as permissoes administrativas continuam sendo gerenciadas
separadamente, sem promover a conta a superusuario.

## Git

A branch `main` acompanha `origin/main`. Antes de enviar alteracoes:

```powershell
git status
git diff
git diff --cached
```

A remocao do banco e dos caches do versionamento preserva os arquivos locais, mas nao remove copias de commits antigos. A chave anteriormente escrita no codigo foi substituida; o historico remoto nao foi reescrito.
