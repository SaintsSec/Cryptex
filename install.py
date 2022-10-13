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
        os.system('rm -rf ~/$USERNAME/.Cryptex')
        os.system('mkdir ~/$USERNAME/.Cryptex')
        os.system('cp -r . ~/$USERNAME/.Cryptex')
        os.system('echo "alias cryptex="python3 ~/$USERNAME/.Cryptex/src/main.py"" >> ~/$USERNAME/.zshrc')
        print("Installation finished.\nRestart the terminal and type 'cryptex' to run the program")
        exit()
    elif ans=="Arch": # Installs for Arch.
        os.system("sudo pacman -Syu")
        os.system("sudo pacman -S python python-pip")
        os.system("python3 -m pip install -r requirements.txt")
        os.system('rm -rf ~/$USERNAME/.Cryptex')
        os.system('mkdir ~/$USERNAME/.Cryptex')
        os.system('cp -r . ~/$USERNAME/.Cryptex')
        os.system('echo "alias cryptex="python3 ~/$USERNAME/.Cryptex/src/main.py"" >> ~/$USERNAME/.zshrc')
        print("Installation finished.\nRestart the terminal and type 'cryptex' to run the program")
        exit()
    elif ans=="Garuda": # Installs for Garuda.
        os.system("sudo pacman -Syu")
        os.system("sudo pacman -S python python-pip")
        os.system("python3 -m pip install -r requirements.txt")
        os.system('rm -rf ~/$USERNAME/.Cryptex')
        os.system('mkdir ~/$USERNAME/.Cryptex')
        os.system('cp -r . ~/$USERNAME/.Cryptex')
        os.system('echo "alias cryptex="python3 ~/$USERNAME/.Cryptex/src/main.py"" >> ~/$USERNAME/.zshrc')
        print("Installation finished.\nRestart the terminal and type 'cryptex' to run the program")
        exit()
    elif ans=="Void": # Installs for Void.
        os.system("sudo apt update")
        os.system("sudo apt-get install -y python3 python3-pip python-dev")
        os.system("sudo apt update")
        os.system("sudo apt-get install -y python3 python3-pip python-dev")
        os.system("pip install -r requirements.txt")
        os.system('rm -rf ~/$USERNAME/.Cryptex')
        os.system('mkdir ~/$USERNAME/.Cryptex')
        os.system('cp -r . ~/$USERNAME/.Cryptex')
        os.system('echo "alias cryptex="python3 ~/$USERNAME/.Cryptex/src/main.py"" >> ~/$USERNAME/.zshrc')
        print("Installation finished.\nRestart the terminal and type 'cryptex' to run the program")
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