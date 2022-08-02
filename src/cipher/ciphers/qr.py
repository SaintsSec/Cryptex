"""
Author: Alex Kollar | Project Manager: The Cryptex Project.
Links: https://github.com/CryptexProject | https://twitter.com/ssgcythes
Description: A QR Generator for Cryptex
"""

from cipher import Cipher
import qrcode, image

class qr(Cipher):

    name = 'QR Code Generator'

    def encode(args):
        text = args.text
        filename = args.output

        if not filename:
            return {'text': "No output file", 'success': False}
        
        if not text:
            return {'text': "No input text", 'success': False}

        # Do stuff with input
        #Generate the QRCode:
        qr = qrcode.QRCode(
            version=1,
            box_size=20,
            border=1)
        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        img.save(filename)
        return {'text': filename, 'success': True}

    def print_options():
        print(''' 
        ### Modes
        -e / --encode ---- encode

        ### Input
        -t / --text ------ input text
        -o / --output ---- output file

        ### Examples
        python main.py qr -e -t "hello" -o "text.png"
        ''')
