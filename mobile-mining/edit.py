import os, time, json
from config import banner
from multiprocessing import cpu_count


cpu_thread = cpu_count()

def OffMiner():


    # no connect server
    push = {
        'status': "off"
    }
    with open("active.json", "w") as set:
        json.dump(push, set, indent=4)

 
    banner()
    try:
       print("ตัวอย่าง:")
       print(" \033[93mstratum+tcp://ap.luckpool.net:3956\033[00m")
       print(" \033[93mstratum+tcp://verushash.asia.mine.zergpool.com:3300\033[00m")
       pool = input(" pool : ")
       print("\033[35m-----------------------------------------------\033[0m")
        
       print("ตัวอย่าง: \033[93mRQpWNdNZ4LQ5yHUM3VAVuhUmMMiMuGLUhT\033[00m")
       wallet = input("wallet: ")
       print("\033[35m-----------------------------------------------\033[0m")
        
       print("ชื่อคนงานขุด เช่น \033[93mMiner01\033[00m")
       name = input("[-n]: ")
       print("\033[35m-----------------------------------------------\033[0m")
        
       print("ตัวอย่าง:")
       print("  \033[93mx หรือ ( hybrid เฉพาะ luckpool )\033[00m")
       print("  \033[93mc=DOGE,mc=VRSC (ไม่ต้องใส่ id=ชื่อ ระบบจะเพิ่มให้เอง)\033[00m")
       password = input("password : ")
       print("\033[35m-----------------------------------------------\033[0m")
        
       print(f"จำนวนthread \033[93mค่าที่ใส่ได้คือ 0 ถึง {cpu_thread}\033[00m")
       cpu = int(input("[-t]: "))
       print("\033[35m-----------------------------------------------\033[0m")
        
       if pool == "" or wallet == "":
            raise Exception()
       if name == "":
            raise Exception()
       if password == "":
            password = "x"
       if cpu == "":
            cpu = 1
    except:
            os.system("@cls||clear")
            print("\033[35mเกิดข้อผิดพลาดโปรดตั้งค่าใหม่\033[0m")
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
