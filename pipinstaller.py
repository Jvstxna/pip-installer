import os
from site import addpackage
import time
from pystyle import Colorate, Colors, Center


#Libraries list

def LibrariesList():
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("╔══════════════════════════════════════════════════════════╗")))
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("║                       Python Libraries                   ║")))
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("╚══════════════════════════════════════════════════════════╝")))
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("╔══════════════════════════════════════════════════════════╗")))
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("║ [1.] Matplotilb                                          ║")))
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("║ [2.] Scipy                                               ║")))
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("║ [3.] PyTorch                                             ║")))
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("║ [4.] Theano                                              ║")))
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("║ [5.] SymPy                                               ║")))
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("║ [6.] Caffe2                                              ║")))
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("║ [7.] NuPIC                                               ║")))
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("║ [8.] Pandas                                              ║")))
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("║ [9.] Seaborn                                             ║")))
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("║ [10.] scikit-learn                                       ║")))
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("║ [11.] Requests                                           ║")))
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("║ [12.] urllib3                                            ║")))
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("║ [13.] NLKT                                               ║")))
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("║ [14.] pillow                                             ║")))
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("║ [15.] pytest                                             ║")))
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("║ [16.] pystyle                                            ║")))
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("║ [17.] Colorama                                           ║")))
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("╚══════════════════════════════════════════════════════════╝")))

#Welcoming

def Welcome():
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("╔══════════════════════════════════════════════════════════╗")))
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("║   _______     __  _____           _        _ _           ║")))
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("║  |  __ \ \   / / |_   _|         | |      | | |          ║")))
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("║  | |__) \ \_/ /    | |  _ __  ___| |_ __ _| | | ___ _ __ ║")))
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("║  |  ___/ \   /     | | | '_ \/ __| __/ _` | | |/ _ \ '__|║")))
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("║  | |      | |     _| |_| | | \__ \ || (_| | | |  __/ |   ║")))
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("║  |_|      |_|    |_____|_| |_|___/\__\__,_|_|_|\___|_|   ║")))
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("║                Python Libraries installer                ║")))
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("╚══════════════════════════════════════════════════════════╝")))
    print('''
    ''')

#Choosing which pip they want to be installing

def Ask():
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("Choose which command you want to use to install python libraries:")))
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("[1.] pip    ")))
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("[2.] pip3   ")))
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("[3.] Exit   "))) 



Welcome()
Ask()

while True: 


    method = input("Number: ")

    if method in ['1']:
        print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("You have chose first method (install with pip)")))
        print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("Choose which python library you want to install:")))
        LibrariesList()
        librarychoosen = input("Your choosen library: ")

        os.system(f"pip install {librarychoosen}")
    
    if method in ['2']:
        print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("You have chose first method (install with pip)")))
        print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter("Choose which python library you want to install:")))
        LibrariesList()
        librarychoosen = input("Your choosen library: ")

        os.system(f"pip3 install {librarychoosen}")


    if method in ['3']:
        asking = input('Are you sure you want to quit? (Y/N): ')
        if asking == "Y":
            break
        elif asking == "N":
            os.system('cls')       

