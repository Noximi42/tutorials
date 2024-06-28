def main():
    try:
        text_file = open("file.txt")
        for line in text_file:
            print(line, end='')
    except FileNotFoundError as fnfe:
        print('File could not be found.')
        print('Error message:', fnfe)
    else:
        print('Success')
    finally:
        print('Trying to closing ...')
        # noinspection PyUnboundLocalVariable
        if 'text_file' in locals() and text_file:
            print('Really closing ...')
            text_file.close()


if __name__ == '__main__':
    main()
