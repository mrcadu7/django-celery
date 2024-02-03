from dcelery.celery_config import app
import logging

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


@app.task(queue='tasks')
def my_task():
    try:
        raise ConnectionError("Connection error ocurred...")
    except ConnectionError:
        logging.error('Connection error ocurred...')
        raise ConnectionError()
    
    except ValueError:
        logging.error('Value error ocurred...')
        perform_especific_error_handling()
    
    except Exception:
        logging.error('An error ocurred...')
        notify_admins()
        perform_fallback_action()
        
        

    
def perform_especific_error_handling():
    pass

def notify_admins():
    pass

def perform_fallback_action():
    pass