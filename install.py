#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():

# Imports.
    import sys # System stuff.
import os # Operating System functions.

menu=True
while menu: # Prints the menu.
    print("""
        - Debian
            (if below type 'Debian')
            - Parrot
            - Ubuntu
            - Kali
            - Mint
        - Arch
        - Garuda
        - Void
        
        **Case sensitive**
        """)
    ans=input(">_ What is your operating system?: ")
    
    # Migrating from os.system once foundation has been built.
    if ans=="Debian": # Installs for Debian.
        os.system("sudo apt update")
        os.system("sudo apt-get install -y python3 python3-pip python-dev")
        os.system("pip install -r requirements.txt")
        os.system('alias cryptex="python3 /home/$USER/\Cryptex/src/main.py"')
        print("Installation finished.")
        exit()
    elif ans=="Arch": # Installs for Arch.
        os.system("sudo pacman -Syu")
        os.system("sudo pacman -S python python-pip")
        os.system("python3 -m pip install -r requirements.txt")
        os.system('alias cryptex="python3 /home/$USER/\Cryptex/src/main.py"')
        print("Installation finished.")
        exit()
    elif ans=="Garuda": # Installs for Garuda.
        os.system("sudo pacman -Syu")
        os.system("sudo pacman -S python python-pip")
        os.system("python3 -m pip install -r requirements.txt")
        os.system('alias cryptex="python3 /home/$USER/\Cryptex/src/main.py"')
        print("Installation finished.")
        exit()
    elif ans=="Void": # Installs for Void.
        os.system("sudo apt update")
        os.system("sudo apt-get install -y python3 python3-pip python-dev")
        os.system("sudo apt update")
        os.system("sudo apt-get install -y python3 python3-pip python-dev")
        os.system("pip install -r requirements.txt")
        os.system('alias cryptex="python3 /home/$USER/\Cryptex/src/main.py"')
        print("Installation finished.")
        exit()
    ans = None
else:
   print("\n Not Valid Choice Try again...")
if __name__ == '__main__':
    import sys # System stuff.
    import os # Operating System functions.
    try:
        main()
    except KeyboardInterrupt:
        print('\nYou interrupted the program.')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)