LINE_LENGTH = 31
GO_RIGHT = 3
INPUT_FILE = 'input.txt'

def main():
    map = read_input()
    trees = 0
    horizontal_position = 0
    for line_current in map:
        if line_current[horizontal_position] == '#':
            trees = trees + 1
        horizontal_position = horizontal_position + GO_RIGHT
        if horizontal_position > LINE_LENGTH - 1:
            horizontal_position = horizontal_position - LINE_LENGTH
    print(trees)


def read_input():
    with open(INPUT_FILE, 'r') as f:
        file_content = f.read()
    return file_content.split('\n')[:-1] # -1 to kill newline at the end of the file that atom won't let me remove


if __name__ == "__main__":
    main()
