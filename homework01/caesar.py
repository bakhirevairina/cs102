def encrypt_caesar(plaintext: str) -> str:
    ciphertext = ''
    for char in plaintext:
        code = ord(char)
        if 97 <= code <= 122 or 65 <= code <= 90:
            code += 3
            if not (97 <= code <= 122 or 65 <= code <= 90):
                code -= 26
        ciphertext += chr(code)
    return ciphertext


def decrypt_caesar(ciphertext: str) -> str:
    plaintext = ''
    for char in ciphertext:
        code = ord(char)
        if 97 <= code <= 122 or 65 <= code <= 90:
            code -= 3
            if not (97 <= code <= 122 or 65 <= code <= 90):
                code += 26
        plaintext += chr(code)
    return plaintext
