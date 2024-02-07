# Django-Celery

Este projeto é parte do curso "Django Celery Mastery: Python Asynchronous Task Processing" que ensina a configurar um ambiente de trabalho para Django Celery com Docker, criar e gerenciar tarefas, lidar com exceções e erros comuns, e programar tarefas periódicas.

## Instalação

Supondo que já se tem acesso e conhecimento no uso do Docker, basta apenas usar o comando:

```
docker-compose up -d --build
```

É recomendado criar um arquivo txt para guardar o DSN do Sentry na variável de ambiente e incluí-lo no gitignore

## Uso do Celery

O curso abrangeu tópicos como configuração do ambiente de trabalho, criação e gerenciamento de tarefas assíncronas, tratamento de exceções e erros, e agendamento de tarefas periódicas. Um exemplo prático do uso, está em utilizar uma das tasks para verificar se a aplicação está funcionando, caso contrário o sentry estaria monitorando e notificando via email.
