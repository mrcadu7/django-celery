from celery import chain
from dcelery.celery_config import app

@app.task(queue='tasks')
def add(x, y):
    return x + y

@app.task(queue='tasks')
def multply(result):
    if result == 5:
        raise ValueError('Error: Division by zero')
    return result * 2

def run_task_chain():
    task_chain = chain(add.s(2, 3), multply.s())
    result = task_chain.apply_async()
    result.get()