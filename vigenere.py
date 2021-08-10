def code(letter, base_letter): # 文字をUnicodeの数字に変換する関数です
    return ord(letter) - ord(base_letter)

def vigenere(plain, key):
    #print(plain, key)
    result = ''
    for i in plain:
        if i == ' ': result += ' '
        else:
            key_index = len(result) % len(key)
            letter_code = code( i, 'a' )
            key_code = code( key[key_index], 'a' )
            result += "%s"%chr((letter_code + key_code) % 26 + ord('a'))
    return result


def decrypt(chiper, key): # 基本的にencrypt関数と一緒です．違うのは，一部の変数の名前と33行目が引き算になっている(復号化している)ことだけです．
    #print(chiper, key)
    result = ''
    for i in chiper:
        if i == ' ': result += ' '
        else:
            key_index = len(result) % len(key)
            letter_code = code( i, 'a' )
            key_code = code( key[key_index], 'a' )
            result += "%s"%chr((letter_code - key_code) % 26 + ord('a'))
    return result