# de Sá Incorporações - API

### API para o site mostruário dos empreendimentos de Sá, possibilita o cliente visualizar os imóveis, agendar uma visita e entrar em contato com a empresa.

<p align="center">
 <a href="#pre">Pré-requisitos</a> |
 <a href="#rodando">Rodando a API</a> | 
 <a href="#tecnologias">Tecnologias</a> |  
 <a href="#autor">Autor</a> |
 <a href="#licenca">Licença</a> 
</p>

<h4 align="center"> 
	🚧  Python 🚀 Em construção...  🚧
</h4>

<h3 id="pre">Pré-requisitos para execução local</h3>

---

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [Python](https://www.python.org/).
Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/)

<h3 id="rodando">Rodando a API localmente</h3>

```bash
# Clone este repositório
$ git clone <https://github.com/odair-dev/desa-api>

# Acesse a pasta do projeto no terminal e crie seu ambiente virtual
shell
python -m venv venv

# Ative seu ambiente virtual:
shell
# Linux e Mac:
source venv/bin/activate

# Windows (PowerShell):
.\venv\Scripts\activate

# Windows (GitBash):
source venv/Scripts/activate

# Instale as dependências
$ pip install -r requirements.txt

# Crie seu banco de dados postgre (PowerShell)
$ psql
$ CREATE DATABASE nome_do_banco;

# Crie o arquivo .env para as variaveis de ambiente com base em .env.example e execute a aplicação
$ python manage.py runserver
```

<h3 id="tecnologias">Tecnologias</h3>

---

As seguintes ferramentas foram usadas na construção do projeto:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [psycopg2-binary](https://pypi.org/project/psycopg2-binary/)
- [django-filter](https://django-filter.readthedocs.io/en/stable/)
- [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/)

<h3 id="autor">Autor</h3>

---

Desenvolvido por Odair Sobrinho 🚀 Entre em contato!

[![Linkedin Badge](https://img.shields.io/badge/-Odair-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/odair-sobrinho/)](https://www.linkedin.com/in/odair-sobrinho/)
[![Gmail Badge](https://img.shields.io/badge/-odairodriguez@yahoo.com.br-slateblue?style=flat-square&logo=Yahoo&logoColor=white&link=mailto:odairodriguez@yahoo.com.br)](mailto:odairodriguez@yahoo.com.br)

<h3 id="licenca">Licença</h3>

---

Este projeto está licenciado sob a licença MIT
