<div align="center">
  <h1>📑 Plataforma de Cursos</h1>
</div>

<br>

![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

<div align="center">
    <a href="#sobre">Sobre</a> | <a href="#tecnologias">Tecnologias</a> | <a href="#run">Rodando o projeto</a>
</div>

<a id="sobre"></a>

## 📑 Sobre o projeto

O projeto **de uma plataforma de cursos** visa ajudar pessoas a terem acesso a cursos gratuitos de uma forma fácil e eficiente.

O site conta ainda com um sistema de cadastro, sistema de avaliações e dentre outras features. 🥰

<a id="tecnologias"></a>

## :computer: Tecnologias

O backend da aplicação foi desenvolvido utilizando as tecnologias:

- [Django](https://www.djangoproject.com/)
- [Docker](https://www.docker.com)
- [Postgres](https://www.postgresql.org/)

<a id="run"></a>

## :running: Rodando o projeto

### DEV Containers 🤯

A aplicação tem suporte para **[DevContainers](https://code.visualstudio.com/docs/remote/containers)**, para rodar basta ter o **[Docker](https://www.docker.com)** rodando na maquina e o VsCode para entrar no container de desenvolvimento.

### Rodando através da fonte:

### 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Você instalou a versão mais recente de `< Docker/ Python>`
- Você tem uma máquina `< Windows / Linux / Mac >`.
- Você possui um `< editor de código / Gerenciador de banco de dados >`.

## 🚀 Instalando

```bash
$ pip install -r requirements
```

## ☕ Rodando

Preencha o arquivo `.env.example` com as informações cobradas e depois renomeie para `.env`.

```env
# DJANGO

# DEBUG = 1 or 0
DEBUG=
SECRET_KEY=

# DJANGO_ALLOWED_HOSTS = localhost 127.0.0.1 [::1] ...
DJANGO_ALLOWED_HOSTS=

# POSTGRES
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=

# PGADMIN
PGADMIN_DEFAULT_EMAIL=
PGADMIN_DEFAULT_PASSWORD=
```

Crie um banco de dados com o docker-compose

```bash
$ docker-compose up db
```

Agora realize as migrações necessárias:

```bash
$ python manage.py makemigrations && python manage.py migrate
```

E por fim, rode o aplicativo:

```bash
$ python manage.py runserver
```

#### _Sinta-se livre para colaborar, toda ajuda é bem vinda ;)_
