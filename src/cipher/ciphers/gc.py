from cipher import Cipher


class GC(Cipher):

    name = 'Gaderypoluki Cipher'
    type = 'cipher'
    
    def code(self,args):

        text = args.text

        if not text:
            return {'text': "No input text", 'success': False}

        self.encode_lower = {'g': 'a', 'a': 'g', 'd': 'e', 'e': 'd', 'r': 'y',
                        'y': 'r', 'p': 'o', 'o': 'p', 'l': 'u', 'u': 'l', 'k': 'i', 'i': 'k'}
        self.encode_upper = {'G': 'A', 'A': 'G', 'D': 'E', 'E': 'D', 'R': 'Y',
                         'Y': 'R', 'P': 'O', 'O': 'P', 'L': 'U', 'U': 'L', 'K': 'I', 'I': 'K'}

        encode_text = ''

        for char in text:
            if char.isupper():
                char = self.encode_upper.get(char, char)
                encode_text += char
            elif char.islower():
                char = self.encode_lower.get(char, char)
                encode_text += char
            else:
                encode_text += char
        return encode_text

    def encode(self, args):
        output = self.code(args)
        return {'text': output, 'success': True}

    def decode(self, args):
        output = self.code(args)
        return {'text': output, 'succes': True}


    def print_options():
        print(''' 
        ### Modes
        -d / --decode ---- decode
        -e / --encode ---- encode

        ### Input
        -t / --text ------ input text

        ### Examples
        python main.py text -e -t 'hello'
        python main.py text -d -t 'hduup'
        ''')
