def cezar_cipher(message, key, mode):

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    message = message.upper().replace(" ", "")

    if not (1 <= key <= 25):
        raise ValueError("Ключ должен быть числом от 1 до 25")

    def get_letter_index(letter):
        return alphabet.index(letter)

    def get_letter_from_index(index):
        return alphabet[index % len(alphabet)]

    result = ""
    for letter in message:
        if letter in alphabet:
            index = get_letter_index(letter)
            if mode == "encrypt":
                index += key
            elif mode == "decrypt":
                index -= key
            else:
                raise ValueError("Режим должен быть 'encrypt' или 'decrypt'")
            result += get_letter_from_index(index)
        else:
            result += letter

    return result

# Ввод данных от пользователя через функции (для совместимости с ограничениями среды)
def get_input():
    return "KHOORZRUOG", 3, "decrypt"

try:
    message, key, mode = get_input()
    output = cezar_cipher(message, key, mode)
    print("Результат:", output)
except ValueError as error:
    print("Ошибка:", error)