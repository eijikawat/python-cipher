import random

string = 'hello world and hello my foolish life'

def code(letter, base):
    return ord(letter) - ord(base)

def onetimePad(string):
    result = ''
    key = ''
    for i in string:
        letter_code = code(i, 'a')
        random_letter = random.randrange(97, 122) # 小文字アルファベットをランダムに取得する
        random_code = code(chr(random_letter), 'a')
        if(i == ' '): 
            result += ' '
            key += ' '
        else:
            result += '%s'%chr((letter_code + random_code) % 26 + ord('a'))
            key += '%s'%chr(random_code + ord('a'))
    return result, key # 暗号文と鍵をタプルとして返す

def decrypt(chiper, key):
    result = ''
    key = key
    key_index = 0
    for i in chiper:
        letter_code = code(i, 'a')
        key_code = code(key[key_index], 'a')
        if(i == ' '):
            result += ' '
            key_index += 1
        else:
            result += '%s'%chr((letter_code - key_code) % 26 + ord('a'))
            key_index += 1
    return result
'''
print('平文　：' + string)
# 暗号文と鍵を別々に取得するためにタプルで関数の値を取得する．
chiper, key = onetimePad(string) # 関数からタプルを取得
print('暗号文：' + chiper)
print('鍵　　：' + key)
print('復号化：' + decrypt(chiper, key))
'''