#!/usr/local/bin python3


INPUT_FILE = "input.txt"


def main():
    content = read_content()
    needed_jolts = max(content) + 3
    content = [0] + content + [needed_jolts]
    total_options = process_content(content, 0)
    print(total_options)


def process_content(content, counter):
    total_options = 0
    addition = 1
    while content[counter] >= content[counter + addition] - 3:
        if counter + addition >= len(content) - 1:
            return 1
            break
        total_options = total_options + process_content(content, counter + addition)
        addition = addition + 1
    return total_options

def read_content():
    with open(INPUT_FILE) as f:
        file_content = f.read()
    file_content = file_content.split('\n')[:-1]
    content_int = []
    for number in file_content:
        content_int.append(int(number))
    return sorted(content_int)


if __name__ == "__main__":
    main()
