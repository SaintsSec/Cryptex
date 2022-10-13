import sys
from vars import banner

class Main:    
    def output(out, args):

        if 'languages' in out:
            return

        if not out['success']:
            sys.exit(f'Failed to run cipher "{args.cipher}"\nError: {out["text"]}')
   
        mode = ""
        if args.decode:
            mode = "Decode"
        elif args.encode:
            mode = "Encode"
        
        banner()
        if args.cipher == 'pswd':
            print(
            f'''
        ------ Cipher: {args.cipher} -- Mode: {mode} ------
        Length   | {args.length}
        Password | {out['text']}
        ----
        ''')
            return

        print(
        f'''
        ------ Cipher: {args.cipher} -- Mode: {mode} ------
        Input      | {args.text}
        Output     | {out['text']}

        Read File  | {args.input if args.input else "N/A"}
        Wrote File | {args.output if args.output else "N/A"}
        ''')

        # If output then output.
        if args.output:
            with open(args.output, "w") as f:
                f.write(f"{out['text']}")

    def parse_args():
        import argparse

        parser = argparse.ArgumentParser()
    
        parser.add_argument('cipher', type=str, help='The cipher name', nargs='?')
    
        # Modes.
        parser.add_argument('-e', '--encode', dest='encode', action='store_true', help="Encode mode")
        parser.add_argument('-d', '--decode', dest='decode', action='store_true', help="Decode mode")
    
        # Input.
        parser.add_argument('-t', '--text', dest='text', type=str, help="The input text")
        parser.add_argument('-k', '--key', dest='key', type=str, help="The key")
        parser.add_argument('-ex', '--exclude', dest='exclude', type=str, help="The exclude list")
        parser.add_argument('-o', '--output', dest='output', type=str, help='output file')
        parser.add_argument('-i', '--input', dest='input', type=str, help='input file')
        parser.add_argument('-iw', '--imageWidth', dest='imageWidth', type=int, help='image width')
        parser.add_argument('-m', '--monocromatic', dest='monocromatic', action='store_true', help='monocromatic')
        parser.add_argument('-lang', dest='languages', action='store_true', help='show languages')
        parser.add_argument('-src', dest='src_lang', type=str, help='source language')
        parser.add_argument('-dest', dest='dest_lang', type=str, help='destination language')
        parser.add_argument('-len', dest='length', type=int, help='length')

        args = parser.parse_args()

        return args

    def run(args, cipher_list):
        
        if not args.cipher:
            sys.exit('No cipher selected.')

        try:
            if not args.cipher.lower() in cipher_list:
                raise
            module = cipher_list[args.cipher]
            
        except:
            sys.exit(f'Cipher "{args.cipher}" may not exist')
    
        func = None

        if args.input:
            with open(args.input, "r") as f:
                data = f.readlines()
                data = "".join(data)
                args.text = data


        if args.encode:
            func = module.encode
        elif args.decode:
            func = module.decode
        else:
            module.print_options()
            sys.exit("Please select a mode\nTry --help or -h for more information")

        Main.output(func(args), args)

# Function to help with printing the list of ciphers.
def add_extra(str, max, char):
    ammount = max - len(str)
    if ammount <= 0:
        str = str[:ammount - 1]
        return str
    str = str + char * ammount
    return str

def print_ciphers(cipher_list):
    # Dictionary of all the types.
    cipher_types = {}

    # Loop over all the ciphers.
    for name in cipher_list:
        # Get the cipher type.
        type = cipher_list[name].type
        # Check if type is in dict, if not then add it.
        if not type in cipher_types:
            cipher_types[type] = []
        # Add cipher long name and short name to list of that ciphers type.
        cipher_types[type].append([cipher_list[name].name, name])
            
    # Print cryptex banner.
    banner()

    # Printing magic.
    line = add_extra('', 37, '-')
    for key in cipher_types:
        print('|' + add_extra(f'-- {key}s', len(line), '-') + "|-- short name ------|")
        for item in cipher_types[key]:
            print('|      ' + add_extra(item[0], 30, ' ') + f' |      {item[1]} \t   |')
    print('|' + line + '|' + add_extra('', 20, '-') +'|')

if __name__ == '__main__':
    # Check if there are args.
    try:
        sys.argv[1]
    except IndexError:
        args_exist = False
    else:
        args_exist = True

    import cipher.ciphers
    import cipher
    cipher_list = {cls.__name__.lower(): cls for cls in cipher.Cipher.__subclasses__()}

    # If there are no args, exit.
    if not args_exist:
        print_ciphers(cipher_list)
        # print('List of ciphers:\n')
        # for _, name in enumerate(cipher_list):
            # print(f'  {name} \t- {cipher_list[name].name}')
        # print()
        sys.exit("Please enter an argument when using this command.\nTry --help or -h for more information")

    args = Main.parse_args()

    # idk... just in case?
    if not args:
        sys.exit("Something went wrong...")

    Main.run(args, cipher_list)
    
