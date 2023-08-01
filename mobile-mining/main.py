import os
import json
import time
import pip
from config import banner



# check import module
try:
    from progress.bar import ShadyBar
except ImportError:
    pip.main(['install', '--user', 'progress'])
    from progress.bar import ShadyBar

try:
    import requests
except ImportError:
    pip.main(['install', '--user', 'requests'])
    import requests


def connectNetwork():
    url = "http://192.168.1.28:8080"
    timeout = 5
    try:
        requests.get(url, timeout=timeout)
        return True
    except (requests.ConnectionError, requests.Timeout) as exception:
        return True


# install miner function 
def install():
    try:
        # os.system("git clone --single-branch -b ARM https://github.com/monkins1010/ccminer")
        os.system("git clone https://github.com/pichetx/autorun-ccminer3.8.0")
        os.system("@cls||clear")
        print("\nกำลังติดตั้ง...\n")
    except:
        print("ติดตั้งไม่สำเร็จ!")


zergpool = ["stratum+tcp://verushash.mine.zergpool.com:3300","stratum+tcp://verushash.na.mine.zergpool.com:3300","stratum+tcp://verushash.eu.mine.zergpool.com:3300","stratum+tcp://verushash.asia.mine.zergpool.com:3300"]
# run miner function
def runOnline():

    if connectNetwork() == True:
        banner()
        with open("set-miner/online.json", encoding="utf-8") as set:
            load = set.read()
            loads = json.loads(load)
            pool = loads['pool']
            wallet = loads['wallet']
            password = loads['pass']
    
        push = {
        'status': True,
        'pool': pool,
        'wallet': wallet,
        'pass': password
    }
    with open("set-miner/online.json", "w") as set:
        json.dump(push, set, indent=4)



def runOffline():
    banner()
    try:
        with open("set-miner/offline.json", encoding="utf-8") as set:
            load = set.read()
            loads = json.loads(load)
            pool = loads['pool']
            wallet = loads['wallet']
            name = loads['name']
            password = loads['pass']
            cpu = loads['cpu']
        if pool == "" or wallet == "":
            print("ไม่พบการตั้งค่า miner กรุณาตั้งค่าโดยใช้คำสั่ง edit-miner")
            return
        print("\033[1;34;40m")   
        print("WALLET =",wallet)
        print("NAME   =",name)
        print("POOL   =",pool)
        print("CPU    =",cpu)
        if pool in zergpool:

           print("PASS   = ",password +",ID="+name)
           print("\033[00m\n")

           time.sleep(2)
           os.system(f"cd ccminer && ./ccminer -a verus -o {pool} -u {wallet}.{name} -p {password},ID={name} -t {cpu}")
       
        else:
        	
         print("PASS   =",password)
         print("\033[00m\n")

         time.sleep(2)
         os.system(f"cd ccminer && ./ccminer -a verus -o {pool} -u {wallet}.{name} -p {password} -t {cpu}")
    except:
        push = {'status': False,'pool': '','wallet': '','name': '','pass': '','cpu': ''}
        with open("set-miner/offline.json", "w") as set:
            json.dump(push, set, indent=4)
        os.system("@cls||clear")
        print("\n\n\033[1;31;40mไม่พบการตั้งค่า หรือ การตั้งค่าไม่ถูกต้อง\nกรุณาตั้งค่าใหม่โดยใช้คำสั่ง edit-miner\033[0m\n\n")




while True:
    os.system("@cls||clear")
    with ShadyBar("\033[1;34;40m Start Mining\033[00m") as bar:
        for i in range(100):
            time.sleep(0.05)
            bar.next()
    if os.path.exists("ccminer") == False:
        install()
        break
    # if os.path.isfile("active.json") == True:
    with open("active.json", encoding="utf-8") as set:
        load = set.read()
        loads = json.loads(load)
        status = loads['status']
    if status == "on":
        runOnline()
        break
    elif status == "off":
        runOffline()
        break
    else:
        os.system("@cls||clear")
        print("\n\n\033[1;31;40mไม่พบการตั้งค่า miner กรุณาตั้งค่าโดยใช้คำสั่ง edit-miner\033[0m\n\n")
        break
    
        
        
