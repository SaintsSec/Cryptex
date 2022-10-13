#!/usr/bin/python
# -*- coding: utf-8 -*-

# Imports.
import sys # System stuff.
import os # Operating System functions.
from colorama import Fore

# Distro package manager commands
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
    # distro selector
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
    # check if the cryptex alias is in the given file
    with open(location, 'rt') as f:
        check = 'alias cryptex' in f.read()
    return check
    
def handle_shell():
    shell = os.readlink(f'/proc/{os.getppid()}/exe')

    # Display a unsuported shell message if the shell isn't suported
    message = f'\n\t\t{Fore.RED}Unsuported shell'
    supported = ['bash', 'zsh', 'fish']
    for s in supported:
        if s in shell:
            message = ''
            break

    # Auto generate the list of shels
    shells = ''
    for s in supported:
        shells += f'\n\t{Fore.GREEN}- {s}'
    print(f"""
        {Fore.GREEN}- auto
            {Fore.YELLOW}- {shell}{message}{shells}
    {Fore.WHITE}""")

    # Check for input
    ans = ''
    options = ['auto'] + supported
    while ans not in options:
        ans=input(f"{Fore.YELLOW}>_ {Fore.CYAN}What is your shell?: {Fore.WHITE}").lower()

    # If the input was not 'auto' then set the shell to what the user entered
    if 'auto' not in ans:
        shell = ans

    # set the path to the config based on what shell you are setting it up for
    user = os.environ['HOME']
    path = ''
    if 'bash' in shell:
        path = f'{user}/.bashrc'
    elif 'zsh' in shell:
        path = f'{user}/.zshrc'
    elif 'fish' in shell:
        path = f'{user}/.config/fish/config.fish'
    else:
        print(f'\n\t{Fore.RED}Unsuported shell: {Fore.WHITE}{shell}\n')
        exit(1)

    # Check if the cyrptex alias already exists in the given shell
    if check_shell_config(path):
        print(f'\n\t{Fore.BLUE}Alias already exists in config: {Fore.WHITE}{path}\n')
        return ''

    command = 'echo \'alias cryptex="python3 ~/.Cryptex/src/main.py"\'' 
    return f'{command} >> {path}'
    
def main():
    # Distro list
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

    # List over commands to run
    commands = []

    # The distro spesific commands
    distro_cmds = None
    while distro_cmds == None:
        distro_cmds = handle_distros()
    commands += distro_cmds

    # Cryptex related commands
    commands += [
        'pip install -r requirements.txt',
        'rm -rf ~/.Cryptex',
        'mkdir ~/.Cryptex',
        'cp -r . ~/.Cryptex',
    ]

    # Shell related commands
    commands += [handle_shell()]

    # Run the commands
    for c in commands:
        if len(c) <= 0: continue
        print(f'\n\t{Fore.GREEN}RUNNING: {Fore.WHITE}{c}\n')
        os.system(c)

    # End message
    print(f"""
    {Fore.GREEN}Installation finished.
    Restart the terminal and type {Fore.YELLOW}cryptex {Fore.GREEN}to run the program{Fore.WHITE}
    """)
    exit()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f'\n{Fore.YELLOW}You interrupted the program.{Fore.WHITE}')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
