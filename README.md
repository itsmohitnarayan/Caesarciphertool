---

# Caesar Cipher Encryption and Decryption

This Python script allows you to perform Caesar cipher encryption and decryption for both uppercase and lowercase text. The Caesar cipher is a simple substitution cipher that shifts characters in the alphabet by a fixed key value.

## Usage

1. Run the script and choose whether you want to encrypt or decrypt a message.

2. Enter the key (an integer between 1 and 26) that determines the shift amount.

3. Enter the text you want to encrypt or decrypt.

4. The script will display the result in the selected mode.

## Features

- Supports both encryption and decryption modes.
- Handles both uppercase and lowercase input and output.
- Preserves non-alphabetic characters in the input.

## Example

### Encryption Mode

```
$ python caesar_cipher.py
*** CAESAR CIPHER ENCRYPTION AND DECRYPTION

Do you want to encrypt or decrypt?
e/d: e

ENCRYPTION MODE SELECTED

Enter the key (1 through 26): 3
Enter the text to encrypt: Hello, World!
CIPHERTEXT: Khoor, Zruog!
```

### Decryption Mode

```
$ python caesar_cipher.py
*** CAESAR CIPHER ENCRYPTION AND DECRYPTION

Do you want to encrypt or decrypt?
e/d: d

DECRYPTION MODE SELECTED

Enter the key (1 through 26): 3
Enter the text to decrypt: Khoor, Zruog!
PLAINTEXT: Hello, World!
```

## License

This code is licensed under the MIT License. Feel free to use it and modify it as needed for your projects.

## Author

Kumar Mohit

---
