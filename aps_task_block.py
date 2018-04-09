# -*- coding: utf-8 -*-
# @Time    : 2018/4/9 下午11:08
# @Author  : wonderstone
# @FileName: aps_task_block.py
# @Software: PyCharm
# @Ref     :

import os, time
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime


def my_job():
    print(os.getpid(), f'{datetime.now():%H:%M:%S} Hello World ')


def getCourseInfo():
    scheduler = BlockingScheduler()
    scheduler.add_job(my_job, 'interval', seconds=5)

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()


if __name__ == '__main__':
    getCourseInfo()
    # while True:
    #     time.sleep(1)
