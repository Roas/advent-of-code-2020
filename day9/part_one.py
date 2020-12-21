#!/usr/local/bin python3


INPUT_FILE = "input.txt"


def main():
    content = read_input()


def read_input():
    with open(INPUT_FILE) as f:
        file_content = f.read()
    return file_content.split('\n')[:-1]


if __name__ == "__main__":
    main()
