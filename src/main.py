import sys
from controller import Controller
import os
from vars import banner
import update
from colorama import Fore

def run():
    update.Update()
    
    # Check if there are args
    try:
        sys.argv[1]
    except IndexError:
        args_exist = False
    else:
        args_exist = True

    import cipher.ciphers
    import cipher

    cipher_list = {cls.__name__.lower(): cls for cls in cipher.Cipher.__subclasses__()}
    controller = Controller(cipher_list)
    # If there are no args, exit.
    if not args_exist:
        controller.cli.print_ciphers()
        sys.exit("Please enter an argument when using this command.\nTry --help or -h for more information")
    controller.run()

if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        print(f'\n{Fore.YELLOW}You interrupted the program.{Fore.WHITE}')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
