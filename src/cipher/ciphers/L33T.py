"""
Author: @marvhus
"""
from cipher import Cipher

class L33T(Cipher): #make sure you change this from text to your cipher

    name = 'L33t Sp34k' #change the name
    type = 'cipher'

    leet_speak = {
        'a': '4',
        'b': '8',
        'c': '(',
        'e': '3',
        'g': '6',
        'h': '#',
        'i': '¡',
        'k': 'X',
        'l': '1',
        'o': '0',
        'p': '9',
        's': '5',
        't': '7',
        'x': '*',
        'z': '2',
        '0': 'O',
        '1': 'L',
        '2': 'Z',
        '3': 'E',
        '4': 'A',
        '5': 'S',
        '6': 'G',
        '7': 'T',
        '8': 'B',
        '9': 'P',
    }
    inverse_leet_speak = dict((v, k) for k,v in leet_speak.items())

    convertWithDict = lambda dict, char : dict[char] if char in dict else char     

    @staticmethod
    def encode(args):
        text = args.text.lower()

        if not text:
            return {'text': "No input text", 'success': False}

        output = ''.join(L33T.convertWithDict(L33T.leet_speak, char) for char in text)

        return {'text': output, 'success': True}

    @staticmethod
    def decode(args):
        text = args.text

        if not text:
            return {'text': "No input text", 'success': False}

        output = ''.join(L33T.convertWithDict(L33T.inverse_leet_speak, char) for char in text)

        return {'text': output, 'success': True}

    @staticmethod
    def print_options():
        #Edit this section as needed for your specific encoding / decoding.
        print(''' 
        ### Modes
        -d / --decode ---- decode
        -e / --encode ---- encode

        ### Input
        -t / --text ------ input text

        ### Examples
        python main.py l33t -e -t 'hello'
        python main.py l33t -d -t 'h3llo'
        ''')
