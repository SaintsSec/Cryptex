"""
Author: @marvhus
Description: Reverse Cipher Cryptex Implementation
"""
from cipher import Cipher

class RC(Cipher):

    name = 'Reverse cipher'
    type = 'cipher'

    def encode(args):
        text = args.text

        if not text:
            return {'text': "No input text", 'success': False}

        output = text[::-1]

        return {'text': output, 'success': True}

    def decode(args):
        text = args.text

        if not text:
            return {'text': "No input text", 'success': False}

        output = text[::-1]

        return {'text': output, 'success': True}
    
    def print_options():
        print('''
        ### Modes
        -d / --decode ---- decode
        -e / --encode ---- encode

        ### Input
        -t / --text ------ input text

        ### Examples
        python main.py rc -e -t 'hello'
        python main.py rc -d -t 'hello'
        ''')
