max_bits = 8  # the register al has 8 bits
rol = lambda val, r_bits: \
    (val << r_bits % max_bits) & (2 ** max_bits - 1) | \
    ((val & (2 ** max_bits - 1)) >> (max_bits - (r_bits % max_bits)))


def main():
    file_data = read_file()
    after_data = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index = 0
    # All possible combinations of the password
    ascii_chars = [i for i in range(256)]
    password = ""

    for i in range(len(file_data)):
        for j in range(len(ascii_chars)):
            decrypt_char = decrypt_algorithm(index, ascii_chars[j], file_data[i])
            if decrypt_char == ord(after_data[index]):
                password += chr(ascii_chars[j])
        index += 1
        if index == 8:
            # The password is 8 characters long.
            break
    print(password)  # The password is: No1Trust


def decrypt_algorithm(index, password_data, file_data):
    data = password_data ^ file_data
    data = rol(data, index)
    data = data - index
    return data


def read_file():
    # We take this file [latin_alphabet.txt] because it can be guessed easily.
    # It could be ABCD... or abcd...
    path = "C:\\Users\\dolev\\OneDrive\\Desktop\\ctf\\flare-on challenges\\2021\\2\\Files" \
           "\\latin_alphabet.txt.encrypted"
    with open(path, "rb") as f:
        return f.read()


if __name__ == '__main__':
    main()
