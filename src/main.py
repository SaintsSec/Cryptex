import sys

class Main:    
    def output(out, args):
        if not out['success']:
            sys.exit(f'Failed to run cipher "{args.cipher}"\nError: {out["text"]}')
   
        mode = ""
        if args.decode:
            mode = "Decode"
        elif args.encode:
            mode = "Encode"

        print(
        f'''
        ------ Cipher: {args.cipher} -- Mode: {mode} ------
        Input  | {args.text}
        output | {out['text']}
        ----
        ''')

    def parse_args():
        import argparse

        parser = argparse.ArgumentParser()
    
        parser.add_argument('cipher', type=str, help='The cipher name', nargs='?')
    
        # Modes
        parser.add_argument('-e', '--encode', dest='encode', action='store_true', help="Encode mode")
        parser.add_argument('-d', '--decode', dest='decode', action='store_true', help="Decode mode")
    
        # Input
        parser.add_argument('-t', '--text', dest='text', type=str, help="The input text")
        parser.add_argument('-k', '--key', dest='key', type=str, help="The key")
        parser.add_argument('-ex', '--exclude', dest='exclude', type=str, help="The exclude list")

        args = parser.parse_args()

        return args

    def run(args, cipher_list):
        
        if not args.cipher:
            sys.exit('No cipher selected.')

        try:
            if not args.cipher.lower() in cipher_list:
                raise
            module = cipher_list[args.cipher]
            
        except():
            sys.exit(f'Cipher "{args.cipher}" may not exist')
    
        func = None

        if args.encode:
            func = module.encode
        elif args.decode:
            func = module.decode
        else:
            module.print_options()
            sys.exit("Please select a mode\nTry --help or -h for more information")

        Main.output(func(args), args)

if __name__ == '__main__':
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

    # If there are no args, exit
    if not args_exist:
        print('List of ciphers:\n')
        for _, name in enumerate(cipher_list):
            print(f'  {name} \t- {cipher_list[name].name}')
        print()
        sys.exit("Please enter an argument when using this command.\nTry --help or -h for more information")

    args = Main.parse_args()

    # idk... just in case
    if not args:
        sys.exit("Something whent wrong...")

    Main.run(args, cipher_list)
    
