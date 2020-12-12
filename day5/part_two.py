#!/usr/local/bin/python3


INPUT_FILE = "input.txt"


class Seat:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.seat_id = (row * 8) + column


def main():
    content = read_input()
    seats = []
    for seat_code in content:
        seats.append(create_seat_object(seat_code))
    find_missing_seat(seats)


def find_missing_seat(seats):
    rows = {}
    for seat in seats:
        try:
            rows[seat.row].append(seat)
        except KeyError:
            rows[seat.row] = [seat]
    for key, val in rows.items():
        if len(val) == 7:
            print(key)
            for seat in val:
                print(seat.column)


def create_seat_object(seat_code):
    seat_code = seat_code.replace("F", "0") \
                         .replace("B", "1") \
                         .replace("L", "0") \
                         .replace("R", "1")
                         
    seat = Seat(
        row=int(seat_code[:7], 2),
        column=int(seat_code[7:], 2)
    )

    return seat


def read_input():
    with open(INPUT_FILE, 'r') as f:
        file_content = f.read()
    return file_content.split('\n')[:-1]  # remove last empty line


if __name__ == "__main__":
    main()
