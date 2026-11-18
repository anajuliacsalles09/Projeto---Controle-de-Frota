# Controle-Frota 🚗

Uma aplicação web desenvolvida para auxiliar no gerenciamento e controle de frotas de veículos, permitindo a organização de informações relacionadas a usuários, veículos, viagens, cargas, abastecimentos, manutenções e despesas.

## Sumário 📑

- [Sobre o projeto](#sobre-o-projeto-)
- [Funcionalidades](#funcionalidades-)
- [Perfis e permissões](#perfis-e-permissões-)
- [Tecnologias utilizadas](#tecnologias-utilizadas-)
- [Requisitos](#requisitos-)
- [Configuração](#configuração-)
- [Execução](#execução-)
- [Permissões dos funcionários](#permissões-dos-funcionários-)
- [Acesso ao sistema privado](#acesso-ao-sistema-privado-)
- [Boas práticas](#boas-práticas-)
- [Git](#git-)
- [Status do projeto](#status-do-projeto-)
- [Contribuições](#contribuições-)
- [Licença](#licença-)
- [Desenvolvedores](#desenvolvedores-)

## Sobre o projeto 🔍

O Controle-Frota é uma aplicação web desenvolvida por estudantes do curso Técnico Integrado em Informática para Internet do Instituto Federal de Educação, Ciência e Tecnologia Baiano – Campus Guanambi, no ano de 2026.

O projeto tem como objetivo facilitar o gerenciamento de uma frota de veículos, centralizando informações e permitindo o acompanhamento de diferentes operações relacionadas à administração e utilização dos veículos.

A plataforma reúne funcionalidades para o controle de veículos, viagens, cargas, abastecimentos, manutenções e despesas, além de possuir um sistema de autenticação e gerenciamento de usuários com controle de permissões.

O sistema foi desenvolvido utilizando Django, buscando organizar as funcionalidades em módulos e garantir que os acessos sejam realizados de acordo com as permissões atribuídas aos usuários.

## Funcionalidades ✨

- Autenticação de usuários.
- Login e logout.
- Separação de acesso entre Administradores e Funcionários.
- Gerenciamento de usuários.
- Cadastro, visualização, edição e exclusão de veículos, conforme permissões.
- Gerenciamento de viagens.
- Gerenciamento de cargas.
- Registro e acompanhamento de abastecimentos.
- Registro e gerenciamento de manutenções.
- Controle de despesas relacionadas à frota.
- Controle de acesso baseado em grupos e permissões.
- Restrição de acesso às funcionalidades do sistema.
- Interface com menus e funcionalidades condicionados às permissões dos usuários.

## Perfis e permissões 🔐

O Controle-Frota possui diferentes níveis de acesso, definidos de acordo com o perfil do usuário e as permissões atribuídas à sua conta.

| Ação | Administrador | Funcionário |
|---|---|---|
| Realizar login e logout | ✅ | ✅ |
| Acessar o sistema privado | ✅ | ✅ |
| Gerenciar usuários | Conforme permissões | ❌ Por padrão |
| Visualizar veículos | Conforme permissões | ✅ |
| Visualizar cargas | Conforme permissões | ✅ |
| Visualizar viagens | Conforme permissões | ✅ |
| Adicionar viagens | Conforme permissões | ✅ |
| Adicionar abastecimentos | Conforme permissões | ✅ |
| Visualizar abastecimentos | Conforme permissões | ✅ |
| Adicionar despesas | Conforme permissões | ✅ |
| Visualizar despesas | Conforme permissões | ✅ |
| Adicionar manutenções | Conforme permissões | ✅ |
| Visualizar manutenções | Conforme permissões | ✅ |
| Editar registros | Conforme permissões | ❌ Por padrão |
| Excluir registros | Conforme permissões | ❌ Por padrão |

**Administrador:** possui acesso às funcionalidades administrativas de acordo com as permissões atribuídas à sua conta, podendo gerenciar usuários e operações do sistema.

**Funcionário:** possui permissões específicas para realizar e consultar determinadas operações da frota, respeitando as restrições de acesso estabelecidas pelo sistema.

## Tecnologias utilizadas ⚒️

- **Python:** linguagem de programação utilizada no desenvolvimento.
- **Django:** framework utilizado para o desenvolvimento da aplicação web.
- **SQLite:** banco de dados utilizado para armazenar as informações.
- **HTML:** estruturação das páginas por meio dos templates.
- **CSS:** estilização e organização visual da interface.
- **JavaScript:** funcionalidades de interação da interface.
- **Git:** ferramenta de controle de versão.
- **GitHub:** plataforma de hospedagem e colaboração no repositório.

## Requisitos 📄

Para executar o projeto localmente, são necessários:

- Python 3.12 ou superior.
- pip (gerenciador de pacotes Python).
- Git.
- Navegador web atualizado.

## Configuração ⚙️

### 1. Clone o repositório

```bash
git clone https://github.com/anajuliacsalles09/Projeto---Controle-de-Frota.git
```

### 2. Acesse a pasta do projeto

```powershell
cd "Projeto PCC\Controle-Frota"
```

> Caso o repositório tenha sido clonado em outro diretório, acesse a pasta correspondente ao projeto.

### 3. Instale as dependências

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Caso ainda não exista um ambiente virtual, crie-o:

```powershell
python -m venv .venv
```

### 4. Configure o banco de dados

Execute as migrações para criar as tabelas:

```powershell
.\.venv\Scripts\python.exe manage.py migrate
```

### 5. Crie um superusuário

```powershell
.\.venv\Scripts\python.exe manage.py createsuperuser
```

O superusuário poderá acessar a área administrativa nativa do Django.

## Execução ▶️

Após concluir a configuração, execute o servidor de desenvolvimento:

```powershell
.\.venv\Scripts\python.exe manage.py runserver
```

Acesse a aplicação pelo navegador:

http://127.0.0.1:8000/

## Permissões dos funcionários 🔑

Ao salvar um usuário do tipo `FUNCIONARIO`, o sistema vincula automaticamente a conta ao grupo `Funcionario`.

A migração `usuario.0005` também configura esse grupo e vincula os funcionários existentes.

O acesso padrão permite adicionar e visualizar abastecimentos, despesas, manutenções e viagens, além de visualizar cargas e veículos. Essas permissões não concedem, por padrão, edição, exclusão ou gerenciamento de usuários.

Os menus, botões e páginas respeitam as permissões, enquanto as views também verificam o acesso diretamente no servidor.

Permissões adicionais concedidas manualmente por outros grupos ou diretamente ao usuário continuam valendo.

Ao alterar o tipo de uma conta para `ADMIN`, o vínculo com o grupo `Funcionario` é removido. As permissões administrativas continuam sendo gerenciadas separadamente, sem promover automaticamente a conta a superusuário.

## Acesso ao sistema privado 🔒

O painel e os sete módulos do sistema exigem autenticação.

A página `/usuarios/login/` apresenta as opções Administrador e Funcionário, direcionando cada uma para o formulário de login correspondente.

Após a autenticação, o perfil é conferido pelo sistema:

- **Administrador:** superusuários e contas com `Usuario.tipo = ADMIN`.
- **Funcionário:** demais contas de usuários.

A escolha de um quadro na tela de login não atribui grupos nem permissões à conta.

O cadastro público foi desativado. Novas contas são criadas pela tela interna de usuários por administradores que possuam a permissão `usuario.add_usuario`.

O endereço antigo `/usuarios/registrar/` exige essa permissão e redireciona para o cadastro interno.

As contas existentes e suas permissões foram preservadas.

## Boas práticas ✅

- Utilizar ambientes virtuais para organizar as dependências.
- Manter as dependências atualizadas no arquivo `requirements.txt`.
- Executar as migrações sempre que houver alterações nos modelos.
- Não compartilhar informações sensíveis, como senhas e chaves secretas.
- Manter o banco de dados local e arquivos temporários fora do versionamento.
- Manter as migrações Python versionadas.
- Verificar as alterações antes de realizar commits.
- Manter o repositório atualizado com commits frequentes.
- Respeitar as permissões e os níveis de acesso definidos no sistema.

## Git 🌿

O projeto utiliza Git para controle de versão e GitHub para hospedagem do repositório e colaboração entre os desenvolvedores.

A branch `main` acompanha `origin/main`.

Antes de enviar alterações, recomenda-se verificar os arquivos modificados:

```powershell
git status
git diff
git diff --cached
```

A remoção do banco de dados e dos caches do versionamento preserva os arquivos locais, mas não remove cópias de commits antigos.

A chave anteriormente escrita no código foi substituída. O histórico remoto não foi reescrito.

## Status do projeto 🚧

Projeto desenvolvido no contexto acadêmico, com o objetivo de aplicar conhecimentos de desenvolvimento web, programação com Django, modelagem de dados, autenticação, gerenciamento de usuários, controle de acesso e integração de funcionalidades em uma aplicação web.

## Contribuições ➕

Por se tratar de um projeto acadêmico, desenvolvido com finalidade educacional e avaliativa, o Controle-Frota não está aberto a contribuições externas.

## Licença 📃

Este projeto possui finalidade educacional e acadêmica. Todos os direitos reservados aos desenvolvedores.

## Desenvolvedores 👥

Lara Pereira Gomes Fausto - @larafausto1
Ana Júlia Costa Salles - @anajuliacsalles09
Maria Luiza Lopes de Carvalho - @luizacarvalhobom-maker 
