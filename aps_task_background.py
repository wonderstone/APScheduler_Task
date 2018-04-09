# -*- coding: utf-8 -*-
# @Time    : 2018/4/9 下午10:36
# @Author  : wonderstone
# @FileName: aps_task_background.py
# @Software: PyCharm
# @Ref     :

import os, time
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import *
from datetime import datetime


def my_job():
    print(os.getpid(), f'{datetime.now():%H:%M:%S} Hello World ')


def my_listener(event):
    if event.exception:
        print('The job crashed :(')
    else:
        print('The job worked :)')


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(my_job, 'interval', seconds=10)
    scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)

    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(5)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
