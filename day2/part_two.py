class Password:
    def __init__(self, minimal, maximal, letter, password):
        self.minimal = int(minimal)
        self.maximal = int(maximal)
        self.letter = letter
        self.password = password


def main():
    data = read_input()
    passwords = split_data_into_objects(data)
    correct_passwords = check_passwords(passwords)
    print(correct_passwords)


def check_passwords(passwords):
    correct_passwords = 0
    for password in passwords:
        count = find_letters_in_position(password.minimal, password.maximal, password.password)
        if (count[0] == password.letter or count[1] == password.letter) and not (count[0] == password.letter and count[1] == password.letter):
            correct_passwords = correct_passwords + 1
    return correct_passwords


def split_data_into_objects(data):
    passwords = []
    for entry in data:
        entry = split(entry)
        jump = 0
        if entry[1] == '-':
            minimal = entry[0]
        else:
            minimal = entry[0] + entry[1]
            jump = jump + 1

        if entry[3 + jump] == ' ':
            maximal = entry[2 + jump]
        else:
            maximal = entry[2+jump] + entry[3+jump]
            jump = jump + 1

        letter = entry[4 + jump]
        password = entry[7+jump:]
        passwords.append(Password(minimal, maximal, letter, password))
    return passwords


def find_letters_in_position(letter1, letter2, password):
    offset = -1
    ret = [password[letter1+offset], password[letter2+offset]]
    return ret


def split(word):
    return [char for char in word]


def read_input():
    with open('input.txt', 'r') as f:
        file_content = f.read();
    return file_content.split('\n')[:-1]


if __name__ == "__main__":
    main()
