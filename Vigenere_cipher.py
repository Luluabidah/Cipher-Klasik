def vigenere_encrypt(plain, key):
    key=key.upper()
    result=""
    for i, char in enumerate(plain.upper()):
        if char.isalpha():
            shift = ord(key[i % len(key)])-65
            result += chr((ord(char)-65+shift)%26+65)
        else:
            result += char
    return result

print(vigenere_encrypt('HELLOWORLD','READY'))