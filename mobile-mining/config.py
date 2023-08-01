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
        

    os.system("clear")
    print("\033[1;34;40m")
    os.system("figlet -f big VERUS")
    print("\033[00m\n")
    print("\033[35mEdit by PICHET SAENGTEWAN\033[0m")
    print("\033[35mDebug Colors by AMARIN PRAPRIWIT\033[0m")
    print("\033[36m\033[0m")
    
    print(f"\n\033[96mกำลัง Run Mining\033[0m\n")
