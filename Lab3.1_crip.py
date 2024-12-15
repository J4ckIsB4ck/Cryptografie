def vigenere_cipher(key, message, action='encrypt'):

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    key = key.upper()
    message = message.upper().replace(' ', '')


    def char_to_index(char):
        return ord(char) - ord('A')


    def index_to_char(index):
        return alphabet[index % len(alphabet)]  

    result = ''
    key_index = 0

    for char in message:
        char_index = char_to_index(char)
        key_char = key[key_index]
        key_index_value = char_to_index(key_char)

        if action == 'encrypt':
            new_index = (char_index + key_index_value) % len(alphabet)
        elif action == 'decrypt':
            new_index = (char_index - key_index_value + len(alphabet)) % len(alphabet)
        else:
            raise ValueError("Действие должно быть 'encrypt' или 'decrypt'")

        result += index_to_char(new_index)
        key_index = (key_index + 1) % len(key)

    return result

if __name__ == "__main__":
    key = "SHIFR"
    message = "ZAVTRA BUDET SOLNECHNO"

    encrypted_message = vigenere_cipher(key, message, action='encrypt')
    print("Зашифрованное сообщение:", encrypted_message)

    decrypted_message = vigenere_cipher(key, encrypted_message, action='decrypt')
    print("Расшифрованное сообщение:", decrypted_message)
