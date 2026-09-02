
# Sistema Web de Gestão de Tarefas
Projeto inicial para organização de tarefas.

## Pré-requisito
- Python 3 instalado.


## Estrutura do projeto
- `main.py`: script principal que exibe a mensagem de identificação do sistema.
- `cadastro_tarefa.py:` protótipo de cadastro de tarefas em terminal.
- `menu_tarefas.py:` protótipo de gerenciamento de tarefas por meio de um menu interativo.
- `gerenciador_chamados.py:` protótipo para gerenciamento e consulta de chamados internos.
- `requirements.txt`: lista as dependências instaladas no ambiente virtual do projeto.
- `.gitignore`: evita que a pasta do ambiente virtual (`.venv/`) seja versionada no Git.

## Execução

Para executar o protótipo de cadastro de tarefa:

python cadastro_tarefa.py

Para executar o menu de tarefas:

python menu_tarefas.py

Para executar o gerenciador de chamados:

python gerenciador_chamados.py

## Opções do menu

Cadastrar tarefa
Listar tarefas
Atualizar situação de uma tarefa
Encerrar sistema

Os dados cadastrados permanecem somente em memória durante a execução do programa e são perdidos quando o sistema é encerrado.

## Ambiente virtual

Criação do ambiente virtual:

python -m venv .venv

Ativação no Windows:

.venv\Scripts\activate

Ativação no Linux/macOS:

source .venv/bin/activate

## Autores

Marllon Gil de Matos Souza - 202422929 | 
Lucas Correa Perez - 202422722 | 
Leonardo Souza Virgilio - 202422928