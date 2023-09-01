from apscheduler.schedulers.background import BackgroundScheduler
from .tasks import print_name


sheduler=BackgroundScheduler()

# sheduler.add_job(print_name,"interval",seconds=3)
sheduler.add_job(print_name,"cron",hour=16,minute=23,second=20)