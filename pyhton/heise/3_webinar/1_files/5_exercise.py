from pathlib import Path

def get_file_paths(dir: Path) -> list[Path]:
    return list(Path.glob(dir, "*.py"))

def get_word_set(file_paths: list[Path]):
    word_set = set()

    for file_path in file_paths:
        with open(file_path, mode='rt') as file:
            for line in file:
                for word in line.split(" "):
                    word = word.strip()
                    if word:
                        word_set.add(word)

    return sorted(word_set);

def write_set_to_file(word_set):
    with open('5_exercise_output.txt', mode='wt') as file:
        for word in word_set:
            file.write(word + "\n")

def print_output_file():
    with open('5_exercise_output.txt', mode='rt') as file:
        for word in file:
            print(word, end='')


def main():
    dir_1 = Path.cwd()
    dir_2 = Path(Path.cwd(), "../3_rest/")
    file_paths = get_file_paths(dir_1)
    word_set = get_word_set(file_paths)
    print(word_set)
    write_set_to_file(word_set)
    print_output_file()

if __name__ == "__main__":
    main()
