#!/usr/local/bin python3


INPUT_FILE = "input.txt"


def main():
    content = read_content()
    content = [0] + content
    process_content(content)


def process_content(content):
    three_jolts = 1
    one_jolt = 0
    i = 0
    while i < len(content) - 1:
        sum_jolt = content[i+1] - content[i]
        if sum_jolt == 1:
            one_jolt = one_jolt + 1
        elif sum_jolt == 3:
            three_jolts = three_jolts + 1
        i = i + 1
    print(three_jolts*one_jolt)


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
