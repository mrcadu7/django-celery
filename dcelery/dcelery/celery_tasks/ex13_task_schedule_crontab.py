from datetime import timedelta
from dcelery.celery_config import app

from celery.schedules import crontab

# app.conf.beat_schedule = {
#     'task1': {
#         'task': 'dcelery.celery_tasks.ex13_task_schedule_crontab.task1',
#         'schedule': crontab(minute='0-59/10', hour='0-5', day_of_week='mon'),
#         'kwargs': {'foo': 'bar'},
#         'args': (1, 2),
#         'options': {
#             'queue': 'tasks',
#             'priority':5,
#         }
#     },
#     'task2': {
#         'task': 'dcelery.celery_tasks.ex13_task_schedule_crontab.task2',
#         'schedule': timedelta(seconds=10),
#     }
# }


@app.task(queue='tasks')
def task1(a, b, **kwargs):
    result = a + b
    print(f"running task 1 - result: {result}")
    
    
@app.task(queue='tasks')
def task2():
    print("running task 2")


"""
* * * * *
| | | | |
| | | | +----- Day of Week (0 - 6) (Sunday=0 or 7)
| | | +------- Month (1 - 12)
| | +--------- Day of Month (1 - 31)
| +----------- Hour (0 - 23)
+------------- Minute (0 - 59)
"""

"""
* * * * *        # Run every minute
*/5 * * * *      # Run every 5 minutes
30 * * * *       # Run at 30 minutes
0 9 * * *        # Run at 9am
0 14 * * 1       # Run on Monday at 2pm
0 0 1,15 * *     # Run at the 1st and 15th of every month
0 20,23 * * 5    # Run at 8pm and 11pm on Friday
*/15 * * * * *   # Run every 15 minutes
0 0 * * *       # Run every day at midnight
0 12 * * MON    # Run on Monday at 12pm
0 0 1-7 * *     # Run onde the first 7 days of the month
0 0/2 * * *     # Run every 2 hours
0 */6 * * *     # Run every 6 hours
0 0-8/2 * * *   # Run every 2 hours from midnight to 8am
0 0,12 * * *    # Run at midnight and noon every day
0 0 * * 0       # Run every Sunday at midnight
0 0 1 1 *       # Run on January 1 every year
0 0 1 1 MON     # Run on the 1st monday of every year
"""