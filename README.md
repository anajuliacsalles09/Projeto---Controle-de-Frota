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

## Acesso ao sistema privado

O painel e os sete modulos exigem login. A entrada em `/usuarios/login/`
apresenta um unico formulario de nome de usuario e senha. O sistema identifica
o perfil pela conta autenticada: superusuarios e contas `Usuario.tipo = ADMIN`
sao administradores; as demais sao funcionarios. O login nao altera grupos,
perfis ou permissoes. Os links antigos de login por perfil redirecionam ao
formulario unico, preservando o destino interno solicitado.

O cadastro publico foi desativado. Novas contas sao criadas pela tela interna
de usuarios por administradores com a permissao `usuario.add_usuario`. O endereco antigo
`/usuarios/registrar/` agora exige essa permissao e redireciona para o cadastro
interno. As contas existentes e suas permissoes foram preservadas.

## Git

A branch `main` acompanha `origin/main`. Antes de enviar alteracoes:

```powershell
git status
git diff
git diff --cached
```

A remocao do banco e dos caches do versionamento preserva os arquivos locais, mas nao remove copias de commits antigos. A chave anteriormente escrita no codigo foi substituida; o historico remoto nao foi reescrito.


## Calculo da distancia das viagens

O calculo usa apenas Python e Django, sem mapas, APIs ou consultas externas.
No cadastro, informe a quilometragem de saida e a de chegada, conforme o
painel do veiculo. Ao salvar, o sistema calcula e registra automaticamente:

    distancia = quilometragem de chegada - quilometragem de saida

Para incluir ida e volta, registre a chegada depois do retorno. Origem e
destino continuam como informacoes da viagem, sem calcular rotas.
Os valores nao podem ser negativos, e a chegada nao pode ser menor que a
saida. O resultado nao pode ser digitado ou alterado pelo formulario.

As viagens antigas preservam sua distancia. Ao edita-las, pode-se preencher
as duas leituras para recalcular ou deixar ambas vazias para manter o valor
anterior. Novas viagens exigem as duas leituras. Os valores aparecem na
tela de detalhes. Depois de atualizar o codigo, execute `python manage.py migrate`.


## Operacoes do diagrama de classes

Os sete modulos possuem cadastrar/registrar, listar/consultar, detalhar,
editar/atualizar e excluir implementados em views baseadas em funcoes
(FBVs). O login e logout usam django.contrib.auth. Os models representam
os dados e relacionamentos do diagrama; nao e necessario duplicar os CRUDs
como metodos dos models.

Calculos previstos no diagrama:
- `Despesa.calcular_total(viagem=None)`: soma as despesas de uma viagem;
  sem o argumento, retorna o total geral. A listagem de despesas usa esse metodo.
- `Viagem.calcular_resultado()`: valor do frete menos o total das despesas
  vinculadas a essa viagem, arredondado em duas casas. O resultado pode
  ser negativo. Cargas, abastecimentos e manutencoes nao sao descontados
  automaticamente porque o diagrama nao os define como despesas da viagem.
- O resultado e gravado ao salvar a viagem e atualizado pelos sinais do
  Django quando despesas sao criadas, alteradas, movidas ou excluidas,
  inclusive pelo Admin. Nao e preenchido manualmente no formulario.
  Alteracoes por `QuerySet.update` ou operacoes em lote que nao disparam
  sinais devem recalcular explicitamente os resultados.
- `Manutencao.consultar_historico(veiculo=None)` corresponde a
  `consultarHistorico()` do diagrama: retorna registros do mais recente
  para o mais antigo, com filtro opcional por veiculo. A listagem oferece
  a selecao do veiculo e atualiza os totais conforme o filtro.

Os campos extras `Usuario.tipo`, `Viagem.km_saida` e `Viagem.km_chegada`
foram mantidos para as funcionalidades solicitadas. O CEP permanece como
texto para preservar zeros iniciais. Essas diferencas devem constar na
versao atualizada do diagrama.
