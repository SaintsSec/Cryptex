"""
Author: @marvhus
Instructions:
    Rename the "Text" class to whatever cipher you are working on.
    Edit the encode and decode defs as required to encode or decode your cipher.
    make sure you add the following to __init__.py: from cipherfile import *
    Doing this will link the code to main.py 
"""
from cipher import Cipher
from itertools import cycle

class Vig(Cipher): #make sure you change this from text to your cipher

    name = 'Vignere Cipher' #change the name
    type = 'cipher'

    alphabet = [chr(i).upper() for i in range(ord('a'), ord('z')+1)]

    def encode(args):
        text = args.text.upper()
        key = args.key.upper()

        if not text:
            return {'text': "No input text", 'success': False}

        if not key:
            return {'text': "No key", 'success': False}
       
        output = []
        for t,k in zip(text, cycle(key)):
            if t not in Vig.alphabet:
                output.append(t)
                continue
            x = ( ord(t) + ord(k) ) % 26
            x += ord('A')
            output.append( chr(x).lower() )

        return {'text': "".join(output), 'success': True}

    def decode(args):
        text = args.text.upper()
        key = args.key.upper()

        if not text:
            return {'text': "No input text", 'success': False}
        if not key:
            return {'text': "No key", 'success': False}

        output = []
        for t,k in zip(text, cycle(key)):
            if t not in Vig.alphabet:
                output.append(t)
                continue
            x = ( ord(t) - ord(k) + 26 ) % 26
            x += ord('A')
            output.append( chr(x).lower() )

        return {'text': "".join(output), 'success': True}

    def print_options():
        #Edit this section as needed for your specific encoding / decoding.
        print(''' 
        ### Modes
        -d / --decode ---- decode
        -e / --encode ---- encode

        ### Input
        -t / --text ------ input text

        ### Examples
        python main.py text -e -t "hello"
        python main.py text -d -t "hello"
        ''') 
