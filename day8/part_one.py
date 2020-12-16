#!/usr/local/bin python3


INPUT_FILE = "input.txt"


def main():
    content = read_input()
    code = content_to_code(content)
    accumulator = run_code(code)
    print(accumulator)


def run_code(code):
    accumulator = 0
    lines_touched = []
    line_number = 0
    while line_number not in lines_touched:
        lines_touched.append(line_number)
        action = code[line_number]
        if action[0] == "acc":
            accumulator = accumulator + action[1]
            line_number = line_number + 1
        elif action[0] == "jmp":
            line_number = line_number + action[1]
        else:
            line_number = line_number + 1
    return accumulator


def content_to_code(content):
    code_formatted = []
    for line in content:
        code_unformatted = line.split(" ")
        code_formatted.append([code_unformatted[0], int(code_unformatted[1])])
    return code_formatted


def read_input():
    with open(INPUT_FILE) as f:
        file_content = f.read()
    return file_content.split('\n')[:-1]


if __name__ == "__main__":
    main()
