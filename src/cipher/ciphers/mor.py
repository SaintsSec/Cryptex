"""
Author: @marvhus
Instructions:
    Rename the "Text" class to whatever cipher you are working on.
    Edit the encode and decode defs as required to encode or decode your cipher.
    make sure you add the following to __init__.py: from cipherfile import *
    Doing this will link the code to main.py 
"""
from cipher import Cipher

class Mor(Cipher): #make sure you change this from text to your cipher

    name = 'Morse code' #change the name
    type = 'cipher'

    morse_alphabet = {
        # Letters
        "A" : ".-",
        "B" : "-...",
        "C" : "-.-.",
        "D" : "-..",
        "E" : ".",
        "F" : "..-.",
        "G" : "--.",
        "H" : "....",
        "I" : "..",
        "J" : ".---",
        "K" : "-.-",
        "L" : ".-..",
        "M" : "--",
        "N" : "-.",
        "O" : "---",
        "P" : ".--.",
        "Q" : "--.-",
        "R" : ".-.",
        "S" : "...",
        "T" : "-",
        "U" : "..-",
        "V" : "...-",
        "W" : ".--",
        "X" : "-..-",
        "Y" : "-.--",
        "Z" : "--..",
        # Numbers
        "0" : "-----",
        "1" : ".----",
        "2" : "..---",
        "3" : "...--",
        "4" : "....-",
        "5" : ".....",
        "6" : "-....",
        "7" : "--...",
        "8" : "---..",
        "9" : "----.",
        # Punctuation
        "." : ".-.-.-",
        "," : "--..--",
        "?" : "..--..",
        "'" : ".----.",
        "!" : "-.-.--",
        "/" : "-..-.",
        "(" : "-.--.",
        ")" : "-.--.-",
        "&" : ".-...",
        ":" : "---...",
        ";" : "-.-.-.",
        "=" : "-...-",
        "+" : ".-.-.",
        "-" : "-....-",
        "_" : "..--.-",
        '"' : ".-..-.",
        "$" : "...-..-",
        "@" : ".--.-.",
        # non-Latin extensions
        # todo: add non-Latin stuff
        # space
        " " : "/" # custom seperator to make it easier to read
    }
    # https://en.wikipedia.org/wiki/Morse_code#Mnemonics

    inverse_morse_alphabet = dict((var, key) for (key, var) in morse_alphabet.items())

    def encode(args):
        text = args.text

        if not text:
            return {'text': "No input text", 'success': False}

        output = []

        for character in text:
            character = character.upper()
            if character in Mor.morse_alphabet:
                output.append(Mor.morse_alphabet[character])
            else:
                output.append(character)


        return {'text': " ".join(output), 'success': True}

    def decode(args):
        text = args.text

        if not text:
            return {'text': "No input text", 'success': False}

        text = text.split(' ')

        output = ''
        for item in text:
            if item in Mor.inverse_morse_alphabet:
                output += Mor.inverse_morse_alphabet[item]
            else:
                output += item

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
        python main.py mor -e -t "hello"
        python main.py mor -d -t "hello"
        ''') 
