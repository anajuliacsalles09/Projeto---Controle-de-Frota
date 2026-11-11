# Revisao do projeto — 11/11/2026

Revisao do codigo proprio dos sete aplicativos Django, configuracoes, rotas, formularios, modelos, administracao, templates, banco e estado local do Git. Nenhuma correcao funcional, commit ou push foi realizado nesta revisao.

## Falhas confirmadas

1. **Edicao de usuario bloqueada.** `usuario/views.py` reutiliza `UsuarioForm`, derivado de `UserCreationForm`, na edicao. Sem senha nova, o formulario exige `password1` e `password2`. Mesmo fornecendo senhas validas, manter o nome de usuario existente retorna erro de unicidade, por causa da validacao do formulario de criacao sobre o usuario pai. Usar um formulario de edicao separado e um fluxo especifico para alterar senha.

2. **Sair pelo dashboard retorna HTTP 405.** `templates/base.html` usa um link GET para `LogoutView`, que aceita POST. Usar formulario POST com CSRF. O formulario de saida de `usuario_list.html` ja usa POST corretamente.

3. **Seis rotas retornam HTTP 500 para registros inexistentes.** Detalhar, editar e excluir usuarios e viagens usam `objects.get()` sem tratar `DoesNotExist`. Confirmado com um administrador e ID inexistente nos dois aplicativos. Usar `get_object_or_404`, como nos demais aplicativos.

4. **Dashboard acessivel sem autenticacao.** `controle_frota/views.py` nao aplica autenticacao nem permissoes. Uma requisicao anonima a `/` recebe HTTP 200 com os totais dos sete modulos, enquanto os demais modulos exigem login e permissao. Proteger o painel conforme a politica de acesso desejada.

5. **Fluxo de cadastro e entrada inconsistente.** O login oferece "Criar uma conta", mas a rota exige usuario autenticado com permissao de adicionar usuario; um visitante recebe redirecionamento de volta ao login. Contas comuns sem permissoes recebem HTTP 403 em `/usuarios/`, destino configurado apos o login. Definir se o cadastro e exclusivo de administradores e ajustar o link, as permissoes e o destino apos entrada.

6. **Formularios aceitam dados inconsistentes.** Confirmado que `VeiculoForm` aceita placa ja cadastrada, ano negativo, quilometragem negativa, capacidade negativa e status arbitrario. `ViagemForm` aceita retorno anterior a saida, distancia negativa e frete negativo. Os demais modelos tambem nao definem limites minimos para litros, pesos e custos. Adicionar validacoes conforme as regras de negocio; saldo de resultado negativo pode ser valido e deve ser tratado separadamente.

7. **Administracao de usuarios sem tratamento de senha.** `usuario/admin.py` registra `Usuario` no `ModelAdmin` padrao. O campo `password` aparece como `CharField` com `AdminTextInputWidget`, sem o fluxo adequado de troca e criptografia de senha do administrador de usuarios. Digitar uma senha comum nesse campo nao a transforma automaticamente em hash e pode inutilizar o login. Configurar um administrador apropriado ao modelo herdado e formularios que usem `set_password`.

8. **Residuos de Markdown e HTML incorreto.** Os quatro templates de viagens contem delimitadores de bloco Markdown, que aparecem como texto nas paginas. `usuario/templates/usuario/usuario_list.html` comeca com `<<!DOCTYPE html>`, com um caractere extra.

## Riscos e melhorias que dependem das regras do sistema

9. **Exclusao em cascata do historico operacional.** Excluir um veiculo elimina viagens e, por consequencia, cargas e despesas; tambem elimina abastecimentos e manutencoes. O coletor de exclusoes confirmou esse comportamento em dados de teste. Excluir um usuario tambem pode atingir viagens e seus dependentes. As telas de confirmacao nao explicam toda essa abrangencia. Avaliar `PROTECT`, desativacao de cadastros ou confirmacao explicita, conforme a necessidade de preservar historico.

10. **Dinheiro armazenado como `FloatField`.** Frete, resultado, carga, despesas, abastecimentos e manutencoes usam ponto flutuante binario, sujeito a imprecisao em calculos. Preferir `DecimalField` com precisao definida. Essa mudanca exige migracoes e revisao dos dados; nao foi aplicada.

11. **Identificadores e seletores pouco claros.** A placa e o CPF nao possuem restricao de unicidade; CPF tambem nao tem validacao de digitos. Os modelos operacionais nao implementam `__str__`, entao seletores de veiculos e viagens exibem identificadores genericos em vez de placa, origem ou destino. A necessidade de unicidade de CPF deve ser confirmada nas regras do cadastro.

12. **Layout integrado apenas ao dashboard.** As demais paginas nao herdam `base.html`; abrem sem o menu e o estilo do painel. Links para criar, editar e excluir aparecem independentemente das permissoes, mesmo quando o servidor retorna 403 ao acessa-los. As permissoes no servidor existem nos sete CRUDs; a melhoria e na navegacao e apresentacao.

13. **Configuracao exclusiva de desenvolvimento.** `check --deploy` aponta seis avisos: DEBUG ativo, ALLOWED_HOSTS vazio, ausencia de HSTS, redirecionamento HTTPS e cookies seguros de sessao e CSRF. Nao impedem o uso local. Configurar producao antes de hospedar, considerando o servidor e o proxy utilizados.

14. **Ausencia de testes automatizados.** Os sete arquivos `tests.py` contem apenas o modelo inicial; `manage.py test` encontrou zero testes. Criar testes de autenticacao, permissoes, edicao de usuario, registros inexistentes, validacao dos formularios e exclusoes.

## Validacoes executadas

- Analise de sintaxe dos 81 arquivos Python proprios: sem erro.
- Compilacao dos 36 templates proprios: sem erro de sintaxe Django. Isso nao valida a apresentacao visual do HTML.
- Localizacao de todos os estaticos referenciados pelas tags `static` dos templates proprios: nenhum ausente.
- Abertura das 35 rotas CRUD com registros existentes e administrador: HTTP 200.
- Abertura das 21 rotas de detalhe, edicao e exclusao com IDs inexistentes: seis respostas 500 em usuarios e viagens; as demais retornam 404.
- Banco SQLite real aberto somente para leitura: `integrity_check` retornou `ok`; nenhuma violacao em `foreign_key_check`.
- Todas as migracoes listadas estao aplicadas no banco local. Na verificacao anterior, `makemigrations --check --dry-run` tambem nao identificou mudancas pendentes.
- Migracoes executadas com sucesso em um banco separado em memoria para os testes exploratorios. Cadastros reais nao foram alterados.

## Git e limites da revisao

A branch `main` acompanha `origin/main` e tem zero commits de divergencia em relacao a referencia remota local. Nao existem arquivos rastreados que coincidam com as novas regras do `.gitignore`. As 72 exclusoes preparadas no indice representam o banco e os caches retirados do versionamento; os arquivos locais continuam preservados. As alteracoes proprias, o tema estatico e os arquivos novos continuam aguardando revisao e commit.

`git fsck --full` terminou sem erro de integridade e mostrou objetos `dangling blob`, esperados depois de retirar do indice arquivos anteriormente adicionados sem commit. Eles nao indicam corrupcao; nao foi feita limpeza destrutiva.

O historico antigo ainda contem o banco e a chave anterior. A chave atual foi substituida na correcao anterior; nao foi reescrito o historico. A sincronizacao foi comparada com a referencia local `origin/main`, sem nova consulta de atualizacoes do GitHub nesta revisao.

Esta revisao nao incluiu interacao visual em navegador, testes completos de todos os POSTs, auditoria de vulnerabilidades de todas as bibliotecas de terceiros nem um ambiente real de producao. Nenhuma revisao estatica garante ausencia de outros defeitos.

## Ordem sugerida

Corrigir primeiro edicao de usuario, senha no administrador, logout, respostas 500 e protecao do dashboard. Em seguida, ajustar entrada e permissoes, validar dados e definir a preservacao do historico. Depois, padronizar templates, tipos monetarios e testes.
