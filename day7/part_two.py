#!/usr/local/bin/python3


INPUT_FILE = "input.txt"


all_different_bags = []


class Bag:
    def __init__(self, name, contains):
        self.name = name
        self.contains = contains


def main():
    content = read_input()
    shiny_gold_bag = None
    for line in content:
        bag_color = line.split(' bags contain ')[0]
        contains_bags = []
        bags_1 = line.split(' bags contain ')[1][:-1]
        bags_2 = bags_1.split(',')
        for bag in bags_2:
            bag = bag.strip()
            if bag != 'no other bags':
                contains_bags.append(bag[:-4].strip())
        bag = Bag(bag_color, contains_bags)
        all_different_bags.append(bag)
        if bag_color == "shiny gold":
            shiny_gold_bag = bag
    bags_in_bag = contained_in_gold_bag(shiny_gold_bag)
    print(bags_in_bag)


def contained_in_gold_bag(bag):
    bags_in_bag = 0
    for inner_bag in bag.contains:
        bags_in_bag = bags_in_bag + int(inner_bag[:1])
        for bag in all_different_bags:
            if bag.name == inner_bag[2:]:
                bags_in_bag = bags_in_bag + (contained_in_gold_bag(bag) * int(inner_bag[:1]))
    return bags_in_bag 


def read_input():
    with open(INPUT_FILE) as f:
        file_content = f.read()
    return file_content.split('\n')[:-1]


if __name__ == "__main__":
    main()
