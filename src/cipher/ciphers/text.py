from cipher import Cipher

class Text(Cipher):

    name = 'Plain text cipher'
    type = 'cipher'

    def encode(args):
        text = args.text

        if not text:
            return {'text': "No input text", 'success': False}

        # Do stuff with input

        return {'text': text, 'success': True}

    def decode(args):
        text = args.text

        if not text:
            return {'text': "No input text", 'success': False}

        # Do stuff with input

        return {'text': text, 'success': True}

    def print_options():
        print(''' 
        ### Modes
        -d / --decode ---- decode
        -e / --encode ---- encode

        ### Input
        -t / --text ------ input text

        ### Example
        python main.py text -t 'hello'
        ''')
