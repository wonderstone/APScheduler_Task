# -*- coding: utf-8 -*-
# @Time    : 2018/4/7 下午1:20
# @Author  : wonderstone
# @FileName: aps_task.py
# @Software: PyCharm
# @Ref     : https://wxnacy.com/2018/01/23/python-apscheduler/
# @Ref     : https://segmentfault.com/a/1190000011084828

import os
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.events import *
from datetime import datetime

# scheduler = BlockingScheduler()
#
scheduler = BackgroundScheduler()
scheduler.start()
datetime.now()

def my_job():
    print(os.getpid(), f'{datetime.now():%H:%M:%S} Hello World ')


def my_listener(event):
    if event.exception:
        print('The job crashed :(')
    else:
        print('The job worked :)')

# def my_listener1(event):
#     print(event)





# scheduler.add_job(my_job, 'interval', seconds=3)
# scheduler.start()
# while True:
#     pass

#
# scheduler.add_job(my_job, 'interval', seconds=3, start_date='2018-04-07 13:49:00', end_date='2018-04-07 17:19:00',
#                   id='my_job_id')
scheduler.add_job(my_job, 'interval', seconds=3, id='my_job_id')


scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
# scheduler.add_listener(my_listener1)

jobs = scheduler.get_jobs()
scheduler.print_jobs()
scheduler.start()
# scheduler.pause_job('my_job_id')
# scheduler.resume_job('my_job_id')
# scheduler.remove_job('my_job_id')
# scheduler.shotdown(wait=False)