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

    # https://gist.github.com/dssstr/aedbb5e9f2185f366c6d6b50fad3e4a4?permalink_comment_id=4035102#gistcomment-4035102
    def vigenere(
        text: str, 
        key: str, 
        alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
        encrypt=True
    ):
        result = ''
        for i in range(len(text)):
            letter_n = alphabet.index(text[i])
            key_n = alphabet.index(key[i % len(key)])
            if encrypt:
                value = (letter_n + key_n) % len(alphabet)
            else:
                value = (letter_n - key_n) % len(alphabet)
            result += alphabet[value]
        return result


    def encode(args):
        text = args.text
        key = args.key

        if not text:
            return {'text': "No input text", 'success': False}

        if not key:
            return {'text': "No key", 'success': False}
        
        output = Vig.vigenere(text=text, key=key, encrypt=True)

        return {'text': output, 'success': True}

    def decode(args):
        text = args.text
        key = args.key

        if not text:
            return {'text': "No input text", 'success': False}
        if not key:
            return {'text': "No key", 'success': False}

        output = Vig.vigenere(text=text, key=key, encrypt=False)

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
        python main.py text -e -t "hello"
        python main.py text -d -t "hello"
        ''') 
