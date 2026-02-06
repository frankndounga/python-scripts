def ceasar_cypher(message, shifted=1):
    ''' Improved version of a ceasar_cypher algorithm '''
    
    MAX_SHIFT = 20
    if shifted < 1 or shifted > MAX_SHIFT:
        print(f'the shifted value cannot be less than 1 or greater tha {MAX_SHIFT} it default to 1.')
        shifted = 1
    encrypted_message = ''
    for letter in message:
        if letter.isalpha():
            code = ord(letter) + shifted
            if letter.isupper() and code >= ord('Z'):
                code = ord('A')
            if letter.islower() and code >= ord('z'):
                code = ord('a')
            encrypted_message += chr(code)
        else:
            encrypted_message += letter
    return encrypted_message

def decrypt_ceasar_cypher(encrypted_message, shifted=1):
    MAX_SHIFT = 20
    if shifted < 1 or shifted > 20:
        print(f'the shifted value cannot be less than 1 or greater tha {MAX_SHIFT} it default to 1.')
        shifted = 1
    decrypted_message = ''
    for letter in encrypted_message:
        if not letter.isalpha():
            decrypted_message += letter
            continue
        code = ord(letter) - shifted
        if letter.isupper() and code < ord('A'):
            code = ord('Z')
        if letter.islower() and code < ord('a'):
            code = ord('z')
        decrypted_message += chr(code)
    return decrypted_message

if __name__ == '__main__':
    
    message = input('Enter the message you want to encrypted: ')
    while True:
        try:
            shifted_number = int(input('Enter a shifted value: '))
        except ValueError:
            print('You cannot enter non digit value.')
        else:
            encrypted_message = ceasar_cypher(message, shifted_number)
            print('The encrypted message is: ', encrypted_message)
            decrypted_message = decrypt_ceasar_cypher(encrypted_message, shifted_number) 
            print('The decrypted message is: ', decrypted_message)
            break