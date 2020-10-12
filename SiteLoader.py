import os
import http.server
import sys

flag = True
endc = '\033[0m'
black = '\033[30m'
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
magneto = '\033[36m'
os.system("clear")

while True:
    print(red + "▒▄█▀▀█░▐██▒█▀█▀█░▐█▀▀▒██░░░▒▐█▀▀█▌─░▄█▀▄─░▐█▀█▄░▐█▀▀▒▐█▀▀▄")
    print(red + "▒▀▀█▄▄─░█▌░░▒█░░░▐█▀▀▒██░░░▒▐█▄▒█▌░▐█▄▄▐█░▐█▌▐█░▐█▀▀▒▐█▒▐█")
    print(red + "▒█▄▄█▀░▐██░▒▄█▄░░▐█▄▄▒██▄▄█▒▐██▄█▌░▐█─░▐█░▐█▄█▀░▐█▄▄▒▐█▀▄▄")
    print(endc + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~by KuliSworm")
    print(red + "Select" + endc + " number")
    print(red + "[" + yellow + "1" + red + "]" + endc + "Launch SiteLoader")
    print(red + "[" + yellow + "2" + red + "]" + endc + "Update packets")
    print(red + "[" + yellow + "3" + red + "]" + endc + "Exit SiteLoader")
    main_select = input(green + "Number:")
    if main_select == "1":
        os.system("clear")
        print("Starting SiteLoader v1.0")
        print(blue + "Loading user config")
        html_name = input(red + "Select html name:"+ endc)
        port = input(red + "Port:" + endc)
        os.system("clear")
        print(red + "▒▄█▀▀█░▐██▒█▀█▀█░▐█▀▀▒██░░░▒▐█▀▀█▌─░▄█▀▄─░▐█▀█▄░▐█▀▀▒▐█▀▀▄")
        print(red + "▒▀▀█▄▄─░█▌░░▒█░░░▐█▀▀▒██░░░▒▐█▄▒█▌░▐█▄▄▐█░▐█▌▐█░▐█▀▀▒▐█▒▐█")
        print(red + "▒█▄▄█▀░▐██░▒▄█▄░░▐█▄▄▒██▄▄█▒▐██▄█▌░▐█─░▐█░▐█▄█▀░▐█▄▄▒▐█▀▄▄")
        print(yellow + "Your host adress:")
        print(red + "http://0.0.0.0:" + port + "/" + html_name)
        print(endc + "to stop server ,use " + green + "CTRL+C")
        os.system("python3 -m http.server " + port)
    elif main_select == "2":
        print(endc + "Update packets ,please wait...")
        os.system("apt update -y")
    elif main_select == "3":
        print(blue + "Closing SiteLoader")
        os.system("clear")
        sys.exit()
    else:
        print("Wrong number")
        os.system("clear")
