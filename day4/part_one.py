#!/usr/local/bin/python3


INPUT_FILE = "input.txt"


class Passport:
    def __init__(self, byr, iyr, eyr, hgt, hcl, ecl, pid, cid):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid


def main():
    data = read_input()
    passports = create_passport_objects(data)
    print(len(passports))
    

def create_passport_objects(data):
    passport_list = []
    for info in data:
        passport_dict = {}
        info_split = info.split('\n')
        for foo in info_split:
            if foo == '':
                continue
            bar = foo.split(' ')
            for baz in bar:
                last_split = baz.split(':')
                passport_dict[last_split[0]] = last_split[1]
        try:
            passport_list.append(Passport(
                byr=passport_dict['byr'], 
                iyr=passport_dict['iyr'], 
                eyr=passport_dict['eyr'], 
                hgt=passport_dict['hgt'], 
                hcl=passport_dict['hcl'], 
                ecl=passport_dict['ecl'], 
                pid=passport_dict['pid'], 
                cid=passport_dict['cid'] if 'cid' in passport_dict.keys() else "", 
            ))
        except KeyError:
            pass
    return passport_list


def read_input():
    with open(INPUT_FILE, 'r') as f:
        file_content = f.read()
    return file_content.split('\n\n')


if __name__ == "__main__":
    main()
