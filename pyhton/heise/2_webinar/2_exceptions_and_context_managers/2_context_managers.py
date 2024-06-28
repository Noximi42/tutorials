def main():
    text_file = open('file.txt')
    for line in text_file:
        print(line, end='')
    print()
    print("Success")
    print("Text file closed?", text_file.closed)
    text_file.close()
    print("Text file closed?", text_file.closed)

    print('-' * 100)

    with open('file.txt') as text_file:
        for line in text_file:
            print(line, end='')
        print()
        print("Success")
    print("Text file closed?", text_file.closed)


if __name__ == '__main__':
    main()
