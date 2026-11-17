# Permissões dos funcionários

> Execução: superpowers:executing-plans, nesta sessão. Escopo autorizado pelo usuário em 17/11/2026.

**Objetivo:** funcionários atuais e futuros recebem o acesso definido pelo usuário, através do grupo existente `Funcionario`.

**Arquitetura:** migração de dados configura as dez permissões do grupo e vincula os funcionários existentes; sinal `post_save` de `Usuario` mantém o vínculo nos novos cadastros e nas mudanças de tipo. As verificações `permission_required` permanecem nas views. Templates exibem somente links autorizados.

**Tecnologias:** Django, grupos e permissões nativos, SQLite.

**Especificação aprovada:** adicionar e visualizar abastecimento, despesa, manutenção e viagem; visualizar carga e veículo. Sem conceder gestão de usuários, edição ou exclusão.

## Etapas

- [x] Escrever testes em `usuario/tests.py` para cadastro público/interno, criação pelo modelo, `commit=False`, atualização, migração dos existentes, acesso às rotas e links exibidos.
- [x] Executar `python -B manage.py test usuario` e confirmar as falhas de acesso esperadas antes da implementação.
- [x] Criar `usuario/permissions.py`, `usuario/signals.py`, registrar o sinal em `usuario/apps.py` e adicionar a migração `0005_permissoes_funcionario.py`.
- [x] Condicionar links de navegação e ações nos templates às permissões correspondentes.
- [x] Executar toda a suíte, `check`, `makemigrations --check --dry-run` e revisão do diff.
- [x] Aplicar a migração no banco local, verificar os acessos com leitura apenas e revisar os arquivos alterados.

## Pontos de revisão

- Cadastro público não permite escolher ADMIN ou obter permissões extras.
- `save(commit=False)` só atribui acesso depois de salvar o usuário.
- Atualização mantém grupos adicionais; mudança para ADMIN remove apenas o grupo padrão de funcionário.
- Funcionário não acessa rotas proibidas mesmo digitando a URL ou enviando POST.
- Migração é repetível e funciona em banco novo; não remove contas ou dados operacionais.

## Resultado da execu??o

- Testes iniciais reproduziram 403 nas listagens e aus?ncia das dez permiss?es.
- Revis?o independente identificou sobrescrita dos grupos pelo Django Admin.
  Corrigida em `UsuarioAdmin.save_related`, com teste real de cria??o e promo??o.
- `python -B manage.py test`: 12 testes passaram.
- `check`: sem problemas; `makemigrations --check --dry-run`: sem altera??es pendentes.
- 37 templates compilados; `git diff --check`: sem erros.
- Migra??o aplicada ao banco local ap?s backup SQLite.
- Quatro funcion?rios existentes conferidos: 11 rotas permitidas retornam 200 e
  16 rotas proibidas retornam 403 por funcion?rio.
- Contas e dados operacionais de oito tabelas id?nticos ao backup.
- Revis?o independente ap?s a corre??o: nenhum defeito concreto restante.
