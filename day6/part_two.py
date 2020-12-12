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
        all_yes_answers = ""
        list_in_parts = il.split('\n')
        people_in_group = len([x for x in list_in_parts if x])
        for part in list_in_parts:
            all_yes_answers = "{}{}".format(all_yes_answers, part)
        occurences = dict((x, all_yes_answers.count(x)) for x in set(all_yes_answers))
        all_answered_yes = ""
        for key, val in occurences.items():
            if val == people_in_group:
                all_answered_yes = "{}{}".format(all_answered_yes, key)
        sensable_list.append(all_answered_yes)
    return sensable_list


def read_input():
    with open(INPUT_FILE, 'r') as f:
        file_content = f.read()
    return file_content.split('\n\n')


if __name__ == "__main__":
    main()
