import os, time, json
from config import banner
from multiprocessing import cpu_count


cpu_thread = cpu_count()


def OnMiner():

    # connect server confix
    push = {
        'status': ""
    }
    with open("active.json", "w") as set:
        json.dump(push, set, indent=4)

    banner()
    print("  [ -- SETTING -- ]  ")
    try:
        minerAPI = input("TAG: ")
        if minerAPI == "":
            raise Exception()
        nameMiner  = input("NAME: ")
        if nameMiner == "":
            nameMiner = "miner01"
        cpuT = int(input("CPU: "))
        if cpuT == "":
            cpuT = cpu_thread-1
        elif cpuT < 0:
            raise Exception()
    except:
        os.system("@cls||clear")
        print("เกิดข้อผิดพลาดโปรดตั้งค่าใหม่!")
        time.sleep(3)
    push = {
        'status': True,
        'miner': minerAPI,
        'name': nameMiner,
        'cpu': cpuT
    }
    with open("set-miner/online.json", "w") as set:
        json.dump(push, set, indent=4)



    try:
        with open("set-miner/offline.json", encoding="utf-8") as set:
            load = set.read()
            loads = json.loads(load)
            pool = loads['pool']
            wallet = loads['wallet']
            name = loads['name']
            password = loads['pass']
            cpu = loads['cpu']
        push = {
            'status': False,
            'pool': pool,
            'wallet': wallet,
            'name': name,
            'pass': password,
            'cpu': cpu
            }
        with open("set-miner/offline.json", "w") as set:
            json.dump(push, set, indent=4)

    except:
        push = {
            'status': False,
            'pool': "",
            'wallet': "",
            'name': "",
            'pass': "",
            'cpu': ""
        }
        with open("set-miner/offline.json", "w") as set:
            json.dump(push, set, indent=4)




def OffMiner():


    # no connect server
    push = {
        'status': "off"
    }
    with open("active.json", "w") as set:
        json.dump(push, set, indent=4)


    banner()
    try:
        print("ชื่อ pool เช่น \033[93mstratum+tcp://ap.luckpool.net:3956\033[00m")
        pool = input("[-o]: ")

        print("เลขกระเป๋า เช่น \033[93mRKh6cinBtWFspyBfK6Xsu8JKJsFyfYmUCr\033[00m")
        wallet = input("[-u]: ")

        print("ชื่อคนงานขุด เช่น \033[93mMiner01\033[00m")
        name = input("[-n]: ")

        print("Password เช่น \033[93mx หรือ hybrid ( เฉพาะ luckpool )\033[00m")
        password = input("[-p]: ")

        print(f"จำนวนthread \033[93mค่าที่ใส่ได้คือ 0 ถึง {cpu_thread}\033[00m")
        cpu = int(input("[-t]: "))
        
        if pool == "" or wallet == "":
            raise Exception()
        if name == "":
            raise Exception()
        if password == "":
            password = "x"
        if cpu == "":
            cpu = 1
#        if password == "":
#            password = "x"
#        if cpu == "":
#            cpu = 1
    except:
        os.system("@cls||clear")
        print("เกิดข้อผิดพลาดโปรดตั้งค่าใหม่!")
        time.sleep(3)
        os.system("edit-miner")

    push = {
        'status': True,
        'pool': pool,
        'wallet': wallet,
        'name': name,
        'pass': password,
        'cpu': cpu
    }
    with open("set-miner/offline.json", "w") as set:
        json.dump(push, set, indent=4)

    try:
        with open("set-miner/online.json", encoding="utf-8") as set:
            load = set.read()
            loads = json.loads(load)
            minerAPI = loads['miner']
            nameMiner = loads['name']
            cpuT = loads['cpu']

        push = {
        'status': False,
        'miner': minerAPI,
        'name': nameMiner,
        'cpu': cpuT
        }
        with open("set-miner/online.json", "w") as set:
            json.dump(push, set, indent=4)
    except:
        push = {
        'status': False,
        'miner': "",
        'name': "",
        'cpu': ""
        }
        with open("set-miner/online.json", "w") as set:
            json.dump(push, set, indent=4)








while True:
    banner()
    OffMiner()           
    break

