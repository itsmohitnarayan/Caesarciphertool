letters= 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)


def encrypt_decrypt(text, mode, key):
    result = ''
    if mode == 'd':
        key = -key

    for letter in text:
        if letter.isalpha(): 
            is_upper = letter.isupper()  
            letter = letter.lower()  

            index = letters.find(letter)
            if index == -1:
                result += letter
            else:
                new_index = index + key
                if new_index >= num_letters:
                    new_index -= num_letters
                elif new_index < 0:
                    new_index += num_letters
                new_letter = letters[new_index]
                if is_upper:
                    new_letter = new_letter.upper()  
                result += new_letter
        else:
            result += letter  

    return result

            


print()
print('*** CAESAR CIPHER ENCRYPTION AND DECRYPTION')
print()

print('Do you want to encrypt or decrypt?')
user_input = input('e/d: ').lower()
print()

if user_input == 'e':
    print('ENCRYPTION MODE SELECTED')
    print()
    key = int(input('Enter the key (1 through 26): '))
    text = input('Enter the text to encrypt: ')
    ciphertext = encrypt_decrypt(text, user_input, key)
    print(f'CIPHERTEXT: {ciphertext}')

elif user_input == 'd':
    print('DECRYPTION MODE SELECTED')
    print()
    key = int(input('Enter the key (1 through 26): '))
    text = input('Enter the text to decrypt: ')
    plaintext = encrypt_decrypt(text, user_input, key)
    print(f'PLAINTEXT: {plaintext}')