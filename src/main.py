import sys
from controller import Controller


if __name__ == "__main__":
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

    # If there are no args, exit
    if not args_exist:
        controller.cli.print_ciphers()
        sys.exit("Please enter an argument when using this command.\nTry --help or -h for more information")

    controller.run()
