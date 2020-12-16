#!/usr/local/bin/python3


INPUT_FILE = "input.txt"


bags_that_could_contain_gold_bag = []
all_different_bags = []


class Bag:
    def __init__(self, name, contains):
        self.name = name
        self.contains = contains


def main():
    content = read_input()
    for line in content:
        bag_color = line.split(' bags contain ')[0]
        contains_bags = []
        bags_1 = line.split(' bags contain ')[1][:-1]
        bags_2 = bags_1.split(',')
        for bag in bags_2:
            bag = bag.strip()
            if bag != 'no other bags':
                contains_bags.append(bag[2:-4].strip())
        all_different_bags.append(Bag(bag_color, contains_bags))
    for bag in all_different_bags:
        if could_contain_gold_bag(bag):
            bags_that_could_contain_gold_bag.append(bag.name)
    print(len(bags_that_could_contain_gold_bag))


def could_contain_gold_bag(bag):
    if bag.name in bags_that_could_contain_gold_bag:
        return True
    elif "shiny gold" in bag.contains:
        return True
    else:
        for inner_bag in bag.contains:
            for bag in all_different_bags:
                if bag.name == inner_bag:
                    if could_contain_gold_bag(bag):
                        return True
        return False


def read_input():
    with open(INPUT_FILE) as f:
        file_content = f.read()
    return file_content.split('\n')[:-1]


if __name__ == "__main__":
    main()
