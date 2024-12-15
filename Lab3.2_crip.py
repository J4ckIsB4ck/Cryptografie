def playfair_cipher(key, message, mode='encrypt'):

    def create_matrix(key):
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        matrix = []
        used_chars = set()

        for char in key.upper():
            if char not in used_chars and char in alphabet:
                matrix.append(char)
                used_chars.add(char)

        for char in alphabet:
            if char not in used_chars:
                matrix.append(char)

        return [matrix[i:i + 5] for i in range(0, 25, 5)]

    def find_position(matrix, char):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == char:
                    return row, col
        return None, None

    def prepare_text(text):
        text = text.upper().replace(' ', '').replace('J', 'I')
        prepared = ""
        i = 0
        while i < len(text):
            char1 = text[i]
            char2 = text[i + 1] if i + 1 < len(text) else 'X'
            if char1 == char2:
                prepared += char1 + 'X'
                i += 1
            else:
                prepared += char1 + char2
                i += 2
        if len(prepared) % 2 != 0:
            prepared += 'X'
        return prepared

    def process_pair(matrix, char1, char2, mode):
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:
            if mode == 'encrypt':
                return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            else:
                return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            if mode == 'encrypt':
                return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            return matrix[row1][col2] + matrix[row2][col1]

    matrix = create_matrix(key)
    prepared_text = prepare_text(message)
    result = ""

    for i in range(0, len(prepared_text), 2):
        char1, char2 = prepared_text[i], prepared_text[i + 1]
        result += process_pair(matrix, char1, char2, mode)

    return result

if __name__ == "__main__":
    key = "KEY"
    message = "LUCREAZA"

    encrypted_message = playfair_cipher(key, message, mode='encrypt')
    print("Зашифрованное сообщение:", encrypted_message)

    decrypted_message = playfair_cipher(key, encrypted_message, mode='decrypt')
    print("Расшифрованное сообщение:", decrypted_message)
