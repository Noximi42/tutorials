import math


def main():
    #root = lambda x: math.sqrt(x) # warning

    # math_functions = (root, square, cube) # functions objects
    math_functions = (lambda x: math.sqrt(x), lambda x: x *x, lambda x: x **3) # functions objects


    for current_function in math_functions:
        print(current_function(8))


# def root(value):
#    return math.sqrt(value)

def square(value):
    return value * value

def cube(value):
    return value ** 3

if __name__ == '__main__':
    main()
