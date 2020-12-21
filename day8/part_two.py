#!/usr/local/bin python3


import copy


INPUT_FILE = "input.txt"


def main():
    content = read_input()
    code = content_to_code(content)
    counter = 0
    for line in code:
        code_mod = copy.deepcopy(code)
        if line[0] == "jmp":
            code_mod[counter] = ["nop", line[1]]
        elif line[0] == "nop":
            code_mod[counter] = ["jmp", line[1]]
        else:
            counter = counter + 1
            continue
        accumulator, found_it = run_code(code_mod)
        if found_it:
            print(counter)
            print(accumulator)
            break
        counter = counter + 1


def run_code(code):
    accumulator = 0
    lines_touched = []
    line_number = 0
    len_code = len(code)
    found_it = False
    while line_number not in lines_touched:
        if line_number == len_code:
            found_it = True
            break
        lines_touched.append(line_number)
        action = code[line_number]
        if action[0] == "acc":
            accumulator = accumulator + action[1]
            line_number = line_number + 1
        elif action[0] == "jmp":
            line_number = line_number + action[1]
        else:
            line_number = line_number + 1
    return accumulator, found_it


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
