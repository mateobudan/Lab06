# Mateo Budan encode() method
# Agustin Zurlo Redi decode() method
def encode(password):
    encoded_pass = ''
    for num in password:
        new_num = str((int(num)+3) % 10)
        encoded_pass += new_num
    return encoded_pass


def decode(encoded_pass):
    decoded_pass = ''
    for num in encoded_pass:
        new_num = str((int(num) + 7) % 10)
        decoded_pass += new_num
    return decoded_pass


if __name__ == '__main__':
    stored_password = ''
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print('')
        choice = int(input('Please enter an option: '))
        if choice == 1:
            password = input('Please enter your password to encode: ')
            stored_password = encode(password)
            print('Your password has been encoded and stored!\n')
        if choice == 2:
            if stored_password == "":
                print("No password available to decode.\n")
                continue
            else:
                decoded_password = decode(stored_password)
                print("The encoded password is", stored_password, "and the original password is", decoded_password, end=".\n\n")
        if choice == 3:
            break



