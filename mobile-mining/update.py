import schedule
import time
import os
from config import bannerup


def updatedata():
    os.system(f"update")
#schedule.every().day.at('05:00').do(updatedata)
schedule.every(3000).second.do(updatedata)
