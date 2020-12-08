#!/usr/local/bin/python3


INPUT_FILE = "input.txt"


class Passport:
    def __init__(self, byr, iyr, eyr, hgt, hcl, ecl, pid, cid):
        self.byr = self.validate_byr(byr)
        self.iyr = self.validate_iyr(iyr)
        self.eyr = self.validate_eyr(eyr)
        self.hgt = self.validate_hgt(hgt)
        self.hcl = self.validate_hcl(hcl)
        self.ecl = self.validate_ecl(ecl)
        self.pid = self.validate_pid(pid)
        self.cid = self.validate_cid(cid)

    def validate_byr(self, byr):
        if 1920 <= int(byr) and int(byr) <= 2002:
            return byr
        raise PassportInvalid

    def validate_iyr(self, iyr):
        if 2010 <= int(iyr) and int(iyr) <= 2020:
            return iyr
        raise PassportInvalid

    def validate_eyr(self, eyr):
        if 2020 <= int(eyr) and int(eyr) <= 2030:
            return eyr
        raise PassportInvalid

    def validate_hgt(self, hgt):
        try:
            unit = hgt[-2:]
            value = int(hgt[:-2])
        except ValueError:
            raise PassportInvalid
        if (unit == "cm" and 150 <= value and value <= 193) or (unit == "in" and 59 <= value and value <= 76):
            return hgt
        raise PassportInvalid

    def validate_hcl(self, hcl):
        if hcl[:1] != '#':
            raise PassportInvalid
        if len(hcl) != 7:
            raise PassportInvalid
        for char in hcl[1:]:
            if char not in "1234567890abcdef":
                raise PassportInvalid
        return hcl

    def validate_ecl(self, ecl):
        accepted_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if ecl in accepted_colors:
            return ecl
        raise PassportInvalid

    def validate_pid(self, pid):
        if len(pid) == 9:
            return pid
        raise PassportInvalid

    def validate_cid(this, cid):
        pass


class PassportInvalid(BaseException):
    pass


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
        except (KeyError, PassportInvalid):
            pass
    return passport_list


def read_input():
    with open(INPUT_FILE, 'r') as f:
        file_content = f.read()
    return file_content.split('\n\n')


if __name__ == "__main__":
    main()
