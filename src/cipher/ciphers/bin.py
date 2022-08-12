"""
Author: Alex Kollar | Project Manager: The Cryptex Project
Description: Binary translation for Cryptex
"""
from cipher import Cipher

class bin(Cipher): #make sure you change this from text to your cipher

    name = 'Binary Translator' #change the name
    type = 'datatype'

    def encode(args):
        text = args.text

        if not text:
            return {'text': "No input text", 'success': False}

        # Here is where you put your encoding / encrypting code.
        output = ' '.join(format(ord(x), 'b') for x in text)
        return {'text': output, 'success': True}

    def decode(args):
        text = args.text

        if not text:
            return {'text': "No input text", 'success': False}

        #Here is where you put your decoding / decrypting code.
        binary_list = text.split(' ')
        output = ''
        for binary in binary_list:
            output += chr(int(binary, 2))
        return {'text': output, 'success': True}

    def print_options():
        #Edit this section as needed for your specific encoding / decoding.
        print(''' 
        ### Modes
        -d / --decode ---- decode
        -e / --encode ---- encode

        ### Input
        -t / --text ------ input text

        ### Examples
        python main.py text -e -t 'hello'
        python main.py text -d -t 'hello'
        ''')
