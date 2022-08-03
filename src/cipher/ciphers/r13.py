"""
Author: @marvhus
Instructions:
    Rename the "Text" class to whatever cipher you are working on.
    Edit the encode and decode defs as required to encode or decode your cipher.
    make sure you add the following to __init__.py: from cipherfile import *
    Doing this will link the code to main.py 
"""
from cipher import Cipher

class R13(Cipher):

    name = "Rot 13"

    def encode(args):
        if not args.text:
            return {'text': "No input text", 'success': False}

        from cipher.ciphers import CC

        args.key = 13

        return CC.encode(args)

    def decode(args):
        if not args.text:
            return {'text': "No input text", 'success': False}

        from cipher.ciphers import CC

        args.key = 13

        return CC.decode(args)

    def print_options():
        print('''
        ### Modes
        -d / --decode ---- decode
        -e / --encode ---- encode

        ### Input
        -t / --text ------ input text

        ### Examples
        python main.py r13 -e -t "hello"
        python main.py r13 -d -t "hello"
        ''')
