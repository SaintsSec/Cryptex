from cipher import Cipher

class AK(Cipher):

    name = 'Autokey Cipher'
    type = 'cipher'

    def encode(args):
        output = ''
        text = args.text
        key = args.key
        new_key = key + text 
        exclude = args.exclude if args.exclude else "\n\t .?!,/\\<>|[]{}@#$%^&*()-_=+`~:;\"'0123456789"

        if not text:
            return {'text': "No input text", 'success': False}

        if not key:
            return {'text': "No shift key", 'success': False}

        output = []
        i = 0
        for character in text:
            if character in exclude:
                output.append(character)
            else:
                x = ((ord(character) % 97) + (ord(new_key[i]) % 97)) % 26  
                x += ord('a')

            output.append(chr(x))
            i = i + 1

        return {'text': "".join(output), 'success': True}

    def decode(args):
        output = ''
        text = args.text
        key = args.key
        exclude = args.exclude if args.exclude else "\n\t .?!,/\\<>|[]{}@#$%^&*()-_=+`~:;\"'0123456789"

        if not text:
            return {'text': "No input text", 'success': False}

        if not key:
            return {'text': "No shift key", 'success': False}

        output = []

        i = 0
        for character in text:
            if character in exclude:
                output.append(character)
            else:
                x = ((ord(character) % 97) - (ord(key[i]) % 97)) % 26  
                x += ord('a')
            output.append(chr(x))
            key += chr(x)
            i += 1

        return {'text': "".join(output), 'success': True}


    def print_options():
        print(''' 
        ### Modes
        -d / --decode ---- decode
        -e / --encode ---- encode

        ### Input
        -t / --text ------ input text
        -k / --key ------- shift key
        -ex / --exclude -- exclude list

        ### Examples
        python main.py cc -e -t "hello" -k 10
        python main.py cc -d -t "hello" -k 10
        python main.py cc -e -t "hello" -k 10 -ex '123456789'
        python main.py cc -d -t "hello" -k 10 -ex '123456789'
       ''')
