Sistema de Cadastro de Membros e Tarefas
Este script tem como objetivo cadastrar membros de uma família e atribuir a eles tarefas diárias da casa. Usando um banco de dados MySQL, o sistema permite:

Inserir informações dos membros da família.
Cadastrar tarefas e atribuí-las a membros específicos.
Realizar consultas para visualizar quais tarefas cada membro está responsável por executar.
Funcionalidades
Cadastro de Membros: Adicione membros da família com informações como CPF, nome, telefone, e-mail e data de nascimento.
Cadastro de Tarefas: Cadastrar tarefas com título, descrição, status (pendente ou concluída), prazo e membro responsável.
Consultas: Realize consultas para saber quais tarefas estão atribuídas a cada membro da família.
Tecnologias Utilizadas
Python: Linguagem utilizada para o desenvolvimento do sistema.
Tkinter: Biblioteca para criação da interface gráfica (GUI).
MySQL: Banco de dados para armazenar as informações dos membros e tarefas.
mysql.connector: Conector Python para comunicação com o banco de dados MySQL.
Como Usar
Configuração do Banco de Dados: Crie um banco de dados no MySQL com as tabelas necessárias.
Configuração de Conexão: Modifique a configuração de conexão no script Python para conectar ao seu banco de dados.
Executar o Script: Execute o script Python para abrir a interface gráfica (GUI). Cadastre membros e tarefas e realize consultas.
Consultas: Utilize o botão de pesquisa para visualizar as tarefas atribuídas a cada membro.
