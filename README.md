<div align="center">

# Tasks Flask CRUD

Uma API REST desenvolvida em **Python** e **Flask** para gerenciamento de tarefas, implementando as operações fundamentais de um CRUD.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask)
![REST API](https://img.shields.io/badge/API-REST-blue?style=flat-square)
![Status](https://img.shields.io/badge/status-completed-success?style=flat-square)

</div>

---

## Sobre

Este projeto foi desenvolvido com o objetivo de praticar os conceitos fundamentais de desenvolvimento backend utilizando **Flask**.

A API disponibiliza operações completas de **CRUD** para gerenciamento de tarefas, seguindo os princípios básicos de uma arquitetura REST e utilizando armazenamento em memória.

---

## Funcionalidades

- Criação de tarefas
- Listagem de todas as tarefas
- Consulta por ID
- Atualização de tarefas
- Remoção de tarefas

---

## Tecnologias

| Tecnologia | Descrição |
|------------|-----------|
| Python | Linguagem principal |
| Flask | Framework Web |
| REST API | Arquitetura da aplicação |
| JSON | Formato de comunicação |

---

## Estrutura

```text
tasks-flask-crud
│
├── models
│   └── task.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Endpoints

| Método | Endpoint | Descrição |
|:-------:|----------|-----------|
| POST | `/tasks` | Criar tarefa |
| GET | `/tasks` | Listar tarefas |
| GET | `/tasks/{id}` | Buscar tarefa |
| PUT | `/tasks/{id}` | Atualizar tarefa |
| DELETE | `/tasks/{id}` | Excluir tarefa |

---

## Exemplo

### Requisição

```json
POST /tasks
```

```json
{
    "title": "Estudar Flask",
    "description": "Criar uma API REST"
}
```

### Resposta

```json
{
    "message": "Nova tarefa criada com sucesso!"
}
```

---

## Executando o projeto

```bash
git clone https://github.com/seuusuario/tasks-flask-crud.git

cd tasks-flask-crud

pip install -r requirements.txt

python app.py
```

Servidor disponível em

```
http://127.0.0.1:5000
```

---

## Próximos passos

- Persistência com SQLite
- SQLAlchemy
- Validação de dados
- Docker
- Testes automatizados
- Swagger/OpenAPI

---

<div align="center">

Desenvolvido por **Kaique Borlenghi**

</div>