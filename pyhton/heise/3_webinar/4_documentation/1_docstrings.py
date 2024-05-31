class MyClass:
    """Example for docstrings.

    This class hows the use of docstrings.
    """
    pass


def my_function():
    """This function does nothing.
    
    Except that it retunrs 42.

    :return: 42
    """

    return 42


def main():
    print(MyClass.__doc__)
    print('-' * 100)
    print(my_function.__doc__)


if __name__ == '__main__':
    main()
