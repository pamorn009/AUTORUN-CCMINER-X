import schedule
import time
import os
from config import bannerup


def job():
    os.system(f"update")
#schedule.every().day.at('05:00').do(updatedata)
schedule.every(5).second.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
