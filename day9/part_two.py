#!/usr/local/bin python3


INPUT_FILE = "input.txt"
PREAMBLE = 25


def main():
    content = read_input()
    #number = process_content(content)
    number = 14360655
    #number = 127
    new_content = []
    for foo in content:
        new_content.append(int(foo))
    new_number = calculate_answer(number, new_content)
    print(new_number)


def calculate_answer(number, content):
    remember_last_line = 0
    total_added = 0
    i = 0
    while i < len(content): 
        if total_added > number:
            total_added = total_added - content[remember_last_line]
            remember_last_line = remember_last_line + 1
        elif total_added < number:
            total_added = total_added + content[i]
            i = i + 1
        if total_added == number:
            nr = content[remember_last_line:i-1]
            return min(nr) + max(nr)
    return "fuck..."


def process_content(content):
    i = PREAMBLE
    while i < len(content):
        options = content[i-PREAMBLE:i]
        options_sum = calculate_all_options(options)
        if int(content[i]) not in options_sum:
            return content[i]
        i = i + 1
    return "Fuck..."


def calculate_all_options(options):
    foo = []
    for option in options:
        for option2 in options:
            if option != option2:
                foo.append(int(option) + int(option2))
    return foo


def read_input():
    with open(INPUT_FILE) as f:
        file_content = f.read()
    return file_content.split('\n')[:-1]


if __name__ == "__main__":
    main()
