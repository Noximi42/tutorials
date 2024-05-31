from pathlib import Path


def main():
    file_path = sorted(Path.cwd().glob('*.py'))[0]

    print(file_path)
    with open(file_path, mode="rt") as file: # mode="rt" is for Read Text
        content = file.read()
        print(content)
    

if __name__ == '__main__':
    main()
