from pathlib import Path


def main():
    file_list_1 = sorted(Path.cwd().parent.glob('*'))
    for f in file_list_1:
        print(f)

    print()
    
    file_list_2 = sorted(Path.cwd().parent.glob('**/*.py'))
    for f in file_list_2:
        print(f)

    print()

    file_list_3 = sorted(Path.cwd().parent.rglob('*.py'))
    for f in file_list_3:
        print(f)


if __name__ == '__main__':
    main()
