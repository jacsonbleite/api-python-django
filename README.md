# API com Python e Django

Simples api de estudo de Python com Django e Django Rest Framework
Cadastro de alunos (nome e rg)


### Statando o servidor
```
python manage.py runserver
```

### Url da API
```
http://127.0.0.1:8000/alunos
```

### Exemplo do JSON
```
{
    "id": 1,
    "nome": "Aluno 01",
    "rg": "123456789"
},
```

Obs: A rota alunos é utilizada para utilização de todos os verbos
Http (GET, POST, DELETE)

Para deletar e atualizar um aluno deve ser passado o *id*

```
http://127.0.0.1:8000/alunos/id_do_aluno
```



