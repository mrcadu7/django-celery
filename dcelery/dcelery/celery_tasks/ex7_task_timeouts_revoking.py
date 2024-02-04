from dcelery.celery_config import app
from time import sleep
import sys

@app.task(queue='tasks', time_limit=10)
def long_running_task():
    sleep(6)
    return "Task completed successfully!"


@app.task(queue='tasks', bind=True)
def process_task_result(self, result):
    if result is None:
        return "Task was revoked, skipping result processing"
    else:
        return f"Task result: {result}"


def execute_task_examples():
    result = long_running_task.delay()
    try:
        task_result = result.get(timeout=40)
    except TimeoutError:
        print("task timed out")
        
    
    task = long_running_task.delay()
    task.revoke(terminate=True)
    sleep(3)
    sys.stdout.write(task.status)
    
    if task.status == "REVOKED":
        process_task_result.delay(None)
    else:
        process_task_result.delay(task_result)

# from dcelery.celery_tasks.ex7_task_timeouts_revoking import long_running_task