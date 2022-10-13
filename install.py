#!/usr/bin/python
# -*- coding: utf-8 -*-

# Imports.
import sys # System stuff.
import os # Operating System functions.
from colorama import Fore

class Distros:
    @staticmethod
    def debian():
        return [
            'sudo apt update',
            'sudo apt-get install -y python3 python3-pip python-dev',
        ]
    @staticmethod
    def arch():
        return [
            'sudo packman -Syu',
            'sudo packman -S python python-pip',
        ]
    @staticmethod
    def void():
        return Distros.debian()

def handle_distros():
    ans=input(f"{Fore.YELLOW}>_ {Fore.CYAN}What is your operating system?: {Fore.WHITE}").lower()
    if 'debian' in ans:
        return Distros.debian()
    elif 'arch' in ans:
        return Distros.arch()
    elif 'void' in ans:
        return Distros.void()
    
    print(f'\n\t{Fore.RED}Unsuported distro: {Fore.WHITE}{ans}\n')
    return None

def check_shell_config(location):
    with open(location, 'rt') as f:
        check = 'alias cryptex' in f.read()
    return check
    
def handle_shell():
    shell = os.environ['SHELL']
    command = 'echo \'alias cryptex="python3 ~/.Cryptex/src/main.py"\'' 
    path = ''
    user = os.environ['HOME']
    if 'bash' in shell:
        path = f'{user}/.bashrc'
    elif 'zsh' in shell:
        path = f'{user}/.zshrc'
    else:
        print(f'\n\t{Fore.RED}Unsuported shell: {Fore.WHITE}{shell}\n')
        exit(1)

    if check_shell_config(path):
        print(f'\n\t{Fore.BLUE}Alias already exists in config: {Fore.WHITE}{path}\n')
        return ''

    return f'{command} >> {path}'
    
def main():
    print(f"""
        {Fore.GREEN}- Debian
            {Fore.WHITE}(if below type 'Debian')
            {Fore.YELLOW}- Parrot
            {Fore.YELLOW}- Ubuntu
            {Fore.YELLOW}- Kali
            {Fore.YELLOW}- Mint
        {Fore.GREEN}- Arch
            {Fore.WHITE}(if bellow type 'Arch'
            {Fore.YELLOW}- Garuda
            {Fore.YELLOW}- Manjaro 
        {Fore.GREEN}- Void{Fore.WHITE}
        """)

    commands = []

    distro_cmds = None
    while distro_cmds == None:
        distro_cmds = handle_distros()
    commands += distro_cmds
    commands += [
        'pip install -r requirements.txt',
        'rm -rf ~/.Cryptex',
        'mkdir ~/.Cryptex',
        'cp -r . ~/.Cryptex',
    ]
    commands += [handle_shell()]

    for c in commands:
        if len(c) <= 0: continue
        print(f'\n\t{Fore.GREEN}RUNNING: {Fore.WHITE}{c}\n')
        os.system(c)
    
    print(f"""
    {Fore.GREEN}Installation finished.
    Restart the terminal and type {Fore.YELLOW}cryptex {Fore.GREEN}to run the program{Fore.WHITE}
    """)
    exit()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n{Fore.YELLOW}You interrupted the program.{Fore.WHITE}')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
