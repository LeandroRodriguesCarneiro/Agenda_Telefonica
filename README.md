﻿# Agenda_Telefonica
## Configurando ambiente virtual
Inicialmente é necessário criar o ambiente virtual. Para criá-lo, basta usar o seguinte comando.

- No Linux, utilizando o bash:

Para criar o ambiente virtual:

    python3 -m venv myenv

Para iniciar o ambiente virtual:

    source myenv/bin/activate
    
- No Windows, utilizando o PowerShell:

Para criar o ambiente virtual:

    python -m venv venv

Para iniciar o ambiente virtual:

    venv/Scripts/activate.ps1

Utilize o comando para instalar as bibliotecas necessárias do projeto após iniciar o ambiente virtual.

    pip install -r requirements.txt

Observação: pode ser necessário utilizar outros comandos para criar o ambiente virtual. Se ocorrer algum problema, favor pesquisar como configurar a máquina para uso dos ambientes virtuais do Python.

- Iniciando o banco de dados e utilizando o código SQL no arquivo database.sql para criar o banco de dados e a tabela necessária.
- Dentro da pasta "dados" tem o arquivo CSV com os dados para realizar a importação no banco de dados, dentro da tabela "contato".
- Após iniciar a IDE, para abrir o projeto, abra o arquivo .env e adicione as seguintes informações:

    HOST= endereço.

    USER= usuário.

    PSW= senha.

    DB= nome do banco de dados.

- Para uso local:

    HOST=localhost

    USER=root

    PSW=

    DB=agenda

Após a configuração, basta utilizar o seguinte comando para iniciar o projeto:

    python app.py

## Testes

Para realizar os testes, foi utilizado o programa Postman.

Endpoints
- /adicionar e /atualizar utilizando o método POST:
  
Foram realizados testes em cada endpoint. Os campos "nome" e "telefone" são obrigatórios e precisam ter valor. A API contém os tratamentos necessários caso esses campos não estejam presentes ou não possuam valor. Os campos "sobrenome" e "email" são opcionais e também possuem tratamento para serem salvos na API, inclusive verificando se o email possui um formato válido. No endpoint de atualização, é necessário um campo "id_contato", que deve conter o ID do contato a ser atualizado.

- /ler e /Busca?buscar utilizando o método GET:
  
O endpoint "ler" precisa de um JSON com "id_contato" para retornar as informações detalhadas do contato. Também possui tratamento para uso com números negativos.

O endpoint "busca" utiliza o parâmetro "buscar", onde é passado o nome ou o texto sobre o qual deseja buscar.

- /deletar utilizando o método DELETE:

Ao enviar o "id_contato" do contato que deseja apagar, possui tratamento para não aceitar números negativos, e apaga se encontrar o ID no banco de dados.

Possui também tratamento básico para execução de SQL no banco de dados.
