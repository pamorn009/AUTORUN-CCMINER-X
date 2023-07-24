import os, json, requests




def versionApp():
    with open("version.json", encoding="utf-8") as read:
        load = read.read()
        loads = json.loads(load)
        return loads['version']

# banner function
def banner():
    with open("active.json", encoding="utf-8") as read:
        load = read.read()
        loads = json.loads(load)
        active = loads['status']
        

    os.system("@cls||clear")
    print(f"Created by.mobile-mining V{versionApp()}")
    print("-----------------------------------------")
    print("\033[96m███╗    ███╗███████╗██████╗ ██╗   ██╗███████╗\033[00m")
    print("\033[96m ██║    ██╔╝██╔════╝██╔══██╗██║   ██║██╔════╝\033[00m")   
    print("\033[96m  ██╗  ██╔╝ █████╗  ██████╔╝██║   ██║███████╗\033[00m")
    print("\033[96m   ██╗██╔╝  ██╔══╝  ██╔══██╗██║   ██║╚════██║\033[00m")
    print("\033[96m    ███╔╝   ███████╗██║  ██║ ██████╔╝███████║\033[00m")
    print("\033[96m    ╚══╝    ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝\033[00m") 
    print("\033[35mEDIT Setup File by PICHET SAENGTAWAN\033[0m")
    print("\033[35mDebug Colors by AMARIN PRAPRIWIT\033[0m")
    if active == "on":
        err = 0
        try:
            url = "https://nutders.com/api/app_update/versionApp.php"
            receive = requests.get(url)
            s = receive.json()
        except:
            err += 1

        if err == 0:
            print(f"\n\033[1;31;40mกำลังใช้งานแบบ online!\033[0m\n")

            if versionApp() != s[0]:
                print(f"\n\033[1;31;40mมีเวอร์ชั่นใหม่กว่าคือ {s[0]} กรุณาอัพเดท!\033[0m\n")
            
        else:
            print(f"\n\033[1;31;40mไม่สามารถเชื่อมต่อกับ server กรุณาใช้งานแบบ offline!\033[0m\n")
            

    if active == "off":
        print(f"\n\033[96mกำลัง Run Mining\033[0m\n")
