# Descrição

Projeto de um Ponto de Venda com cadastros de Cliente, Produto e Venda, utilizando o Framework Django, para a disciplina Programação para Web, do Curso de Pós Graduação do IFBA de Vitória da Conquista - BA


# Banco de Dados

O bando de dados escolhido foi o MySQL e o minu-mundo diz respeito ao de uma loja X que necessita ter o nome e email dos clientes para contato e realizar vendas de seus produtos para esses clientes.

Dados para criação do baco de dados:
* ENGINE : 'django.db.backends.mysql',
* NAME: 'django_web1',
* USER: 'django',
* PASSWORD: 'django',
* HOST: 'localhost',  
* PORT: '3306',


# Instalação do Ambiente

* Baixar e instalar o Python (https://www.python.org/downloads/);
* Sistema desenvolvido atrás da plataforma PyCharm (https://www.jetbrains.com/pycharm/) e usamos ela como base para instalar o Django;
* É necessário também instalar o CLient do MySql através do comando: pip install mysqlclient
* Também foi utilizado o pacote que usa as classes do Bootstrarp no formulários, ele deve ser instalado com o comando: pip install django-crispy-forms

# Iniciando a Aplicação

* Primeiro passo é criar a migração do banco de dados com o comando: python manage.py makemigrations 
* Depois a migração criada é executada: python manage.py migrate
* Então o servidor deve ser iniciado: python manage.py runserver
* O sistema deve ser acessado através da url: http://127.0.0.1:8000/pdv/



# Problemas encontrados

* Ao tentar instalar o mysqlclient recebi um erro referente a versão do Virtual C++ que deve ser 14.0.0 +, e foi necessária a instalação;
* Mesmo com a versão mais nova do Virtual C++ o client não era instalado, o erro era sobre a falta do arquivo "mysql.h" (Tentamos realizar a instalação em 3 máquinas diferentes com versões diferentes do MySQL e o erro persistia). Após pesquisar muito vimos que o instalador procurava dentro da pasta do conector MySQL uma pasta do MariaDB, e para resolver foi necessário baixar e instalar a versão mais atual do conector C do MariaDB. Depois de instalado foi necessário abrir o diretório de instalação do Conector do MySQL ir na pasta LIB e criar uma pasta com o nome "mariadb" e então copiar o conteudo da pasta LIB do MariaDB para essa pasta. O mesmo passo teve que ser repetido para a pasta INCLUDE (criar a pasta "mariadb" e copiar o conteudo da pasta include do MariaDB)
* Para o relacionamento n-m entre Venda e Produto foi feita uma tabela ProdutoVenda com as chaves primárias de Produto e Venda e os campos de quantidade e valor. O banco de dados foi mapeado e criado corretamente. Porém, o formulário gerado pelo Django criava uma select para escolha do produto e deixava os campos de quantidade e valor de fora. Pergutamos para Fagner e ele nos enviou o repositório de um trabalho com relacionamentos n-m, mas eram relacionamentos simples (sem campos extras, logo o formulário gerado apenas com o select servia) e infelizmente não nos ajudou a resolver o problema. Não conseguimos achar exemplos nem como fazer, alguns tutoriais de versões bem anteriores do Django e outros com partes mais avançadas que não tínhamos conhecimento. Partimos então para tentar implementar o relacionamento na mão, mas não conseguimos utilizar javascript no template de maneira correta, e quando conseguimos fazer uma função JS não acertamos acessar as variáveis enviadas pelo Django. Infelizmente não consegui corrigir esse problema a tempo. Os cadastros de cliente e produtos estão funcionando mas o de venda não.


# Conclusão

A primeira vista o framework Django é muito bom e simples de usar, facilita bastante trabalhos com bancos de dados simples. Porém, encontramos uma problema gigante e aparentemente sem sentido para instalar o client do MySQL. Outro ponto que desagradou foi a dificuldade para utilizar um relacionamento bastante comum n-m com campos extras, onde o framework não cria o template de forma correta e nos obrigou a tentar implementar tudo na mão, o que tira o brilho das facilidades apresentadas. Não conseguimos encontrar um tutorial claro de como fazer na documentação. Porém, é importante ter em mente que esse foi nosso primeiro contato e primeira tentativa de usar o Django.

