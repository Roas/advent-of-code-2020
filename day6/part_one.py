#!/usr/local/bin/python3


INPUT_FILE = "input.txt"


class Group:
    def __init__(self):
        pass


def main():
    input_list = read_input()
    sensable_list = make_sense_of_input(input_list)
    total_yes = 0
    for answers in sensable_list:
        total_yes = total_yes + len(answers)
    print(total_yes)


def make_sense_of_input(input_list):
    sensable_list = []
    for il in input_list:
        answers = ""
        list_in_parts = il.split('\n')
        for part in list_in_parts:
            answers = "{}{}".format(answers, part)
        answers = "".join(dict.fromkeys(answers))
        sensable_list.append(answers)
    return sensable_list


def read_input():
    with open(INPUT_FILE, 'r') as f:
        file_content = f.read()
    return file_content.split('\n\n')


if __name__ == "__main__":
    main()
