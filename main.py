#!/usr/bin/env python3

import sys
import vigenere, onetimePad

mode, text = sys.argv[1], sys.argv[2]

def open_file(file_name):
    file = open(file_name, 'r')
    result = file.read()
    file.close()
    return result

def write_file(file_name, content):
    file = open(file_name, 'w+')
    file.write(content)
    file.close()

# --- vigenere ---

# $./main --vigenere <text> <key>
if mode == '--vigenere':
    key = sys.argv[3]
    print('vigenere')
    if text and key:
        plain_text = open_file(text)
        write_file(text, vigenere.vigenere(plain_text, key))

    else: print('Syntax Error: $./main --vigenere <text> <key>')

# ./main --decrypt-vigenere <text file> <key>
elif mode == '--decrypt-vigenere':
    key = sys.argv[3]
    print('decrypt vigenere')
    if text and key:
        cipher = open_file(text)
        write_file(text, vigenere.decrypt(cipher, key))

    else: print('Syntax Error: $./main -Vd <cipher> <key>')

# --- onetime-pad ---

# ./main --onetimepad <text file>
elif mode == '--onetimepad':
    if text:
        plain_text = open_file(text)
        cipher, key  = onetimePad.onetimePad(plain_text)
        write_file(text, cipher)
        write_file('pre-share-key.txt', key)

    else: print('Syntax Error: $./main --onetimepad <text file>')

# ./main --decrypt-otp <text file> pre-share-key.txt
elif mode == '--decrypt-otp':
    key = sys.argv[3]
    if text and key:
        cipher = open_file(text)
        key_value = open_file(key)
        cipher = onetimePad.decrypt(cipher, key_value)
        write_file(text, cipher)
        import os
        os.remove('pre-share-key.txt')
else: print('Syntax Error: $./main --decrypt-otp <text file> pre-share-key.txt')