# Projeto Business Control

Este é um sistema de controle de negócios desenvolvido com Django e Django REST Framework, focado no gerenciamento de empresas e funcionários. O projeto permite a criação, listagem, atualização e exclusão de empresas e funcionários.

Este projeto fornece funcionalidades para o gerenciamento de empresas e funcionários. Ele usa Django para a parte de back-end e Django REST Framework para fornecer uma API RESTful para interagir com os dados.

## Pré-requisitos

Antes de rodar o projeto, verifique se você tem os seguintes pré-requisitos instalados:

- [Python 3.x](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)

Se você ainda não tem o Python instalado, pode fazer o download no site oficial.

## Instalação

Siga os passos abaixo para configurar o ambiente e instalar as dependências do projeto.

1. **Clone o repositório:**
   git clone https://github.com/seu-usuario/business-control.git
2. **Vá até a pasta do projeto.**
3. **Crie um ambiente virtual:**
   python -m venv venv (Windows)
4. **Ative o ambiente virtual:**
   venv\Scripts\Activate.ps1 (Windows)
5. **Instale as dependências:**
   pip install -r requirements.txt

## Configuração

**Configuração do banco de dados:**

O projeto usa um banco de dados SQLite por padrão, mas você pode configurar outro banco de dados como PostgreSQL, alterando as configurações no arquivo settings.py.

**Obs:** Crie as migrações e aplique-as:
python manage.py makemigrations
python manage.py migrate

**Crie um superusuário (caso queira utlizar o admin do Django):**
python manage.py createsuperuser

**Rodando o Servidor**
Para acessar o sistema , use o seguinte comando:
python manage.py runserver

Se preferir acessar a API RESTful, você pode usar o seguinte endpoint:

Empresas: http://127.0.0.1:8000/empresas/
Funcionários: http://127.0.0.1:8000/funcionarios/


**Testes**
Para rodar os testes do projeto, use o comando abaixo:
python manage.py test
Os testes serão executados e o Django irá fornecer um relatório com os resultados.

**Postman**
Também é possível fazer requisições para a API através do postman:
Entre na pasta postman e vá até collection.json, com esta collection importada para seu postman, você poderá executar um CRUD, lembre-se de rodar o servidor antes.


