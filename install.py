#!/usr/bin/python
# -*- coding: utf-8 -*-

# Imports.
import sys # System stuff.
import os # Operating System functions.

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
    print("""
        - Debian
            (if below type 'Debian')
            - Parrot
            - Ubuntu
            - Kali
            - Mint
        - Arch
            (if bellow type 'Arch'
            - Garuda
            - Manjaro 
        - Void
        
        **Case sensitive**
        """)
    ans=input(">_ What is your operating system?: ").lower()

    if 'debian' in ans:
        return Distros.debian()
    elif 'arch' in ans:
        return Distros.arch()
    elif 'void' in ans:
        return Distros.void()
    
    print(f'Unsuported distro: {ans}')
    exit(1)

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
        print(f'Unsuported shell: {shell}')
        exit(1)

    if check_shell_config(path):
        print(f'\nAlias already exists in {path}\n')
        return ''

    return f'{command} >> {path}'
    
def main():
    commands = []

    commands += handle_distros()
    commands += [
        'pip install -r requirements.txt',
        'rm -rf ~/.Cryptex',
        'mkdir ~/.Cryptex',
        'cp -r . ~/.Cryptex',
    ]
    commands += [handle_shell()]

    for c in commands:
        print(f'RUNNING: {c}')
        os.system(c)
    
    print("Installation finished.\nRestart the terminal and type 'cryptex' to run the program")
    exit()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nYou interrupted the program.')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
