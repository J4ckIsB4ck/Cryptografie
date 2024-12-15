def caesar_cipher_with_keys(text, numeric_key, string_key, action):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    text = text.upper().replace(" ", "")

    if not (1 <= numeric_key <= 25):
        raise ValueError("Числовой ключ должен быть числом от 1 до 25")

    if len(string_key) < 7 or not all(c.isalpha() for c in string_key):
        raise ValueError("Строковый ключ должен содержать только буквы и быть длиной не менее 7 символов")

    string_key_shift = sum(ord(char) for char in string_key.upper()) % 26

    result = ""
    for char in text:
        if char in alphabet:
            char_index = alphabet.index(char)
            if action == "encrypt":
                new_index = (char_index + numeric_key + string_key_shift) % 26
            elif action == "decrypt":
                new_index = (char_index - numeric_key - string_key_shift) % 26
            else:
                raise ValueError("Действие должно быть 'encrypt' или 'decrypt'")
            result += alphabet[new_index]
        else:
            raise ValueError("Текст должен содержать только буквы алфавита")

    return result

# Основная функция для запуска программы
if __name__ == "__main__":
    def get_input():
        return "HELLO", 3, "SAMPLEKEY", "encrypt"

    try:
        print("Шифр Цезаря с двумя ключами")
        text, numeric_key, string_key, action = get_input()

        if action not in ["encrypt", "decrypt"]:
            raise ValueError("Выберите корректное действие: encrypt или decrypt")

        result = caesar_cipher_with_keys(text, numeric_key, string_key, action)
        print("Результат:", result)

    except ValueError as e:
        print("Ошибка:", e)
