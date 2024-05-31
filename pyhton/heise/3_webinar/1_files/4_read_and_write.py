from pathlib import Path


def main():
    file_path = sorted(Path.cwd().glob('*.py'))[0]

    with open(file_path, mode='rt') as file:
        line = file.readline()
        while line:
            print(line, end='')
            line = file.readline()

    print('-' * 100)
   
    with open(file_path, mode='rt') as file:
        for line in file:
            print(line, end='')

    print('-' * 100)

    with open(file_path, mode='rt') as file:
        lines = file.readlines()
        # lines = [line.strip() for line in lines] # Remove all preceding and trailing whitespaces
        # lines = [line[:-1] for line in lines] # Remove the last (hopefully newline) character. Be carful!
        lines = [line.rstrip() for line in lines] 

        for line in reversed(lines):
            print(line)


if __name__ == '__main__':
    main()
