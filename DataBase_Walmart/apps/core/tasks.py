from celery.task import periodic_task
from celery.schedules import crontab

@periodic_task(ignore_result=True, run_every=crontab())  # раз в минуту
def just_print():
    print("Print from celery task")
