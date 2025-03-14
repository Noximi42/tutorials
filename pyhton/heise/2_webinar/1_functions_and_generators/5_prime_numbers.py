NEXT_PRIME_NUMBER_LABEL = 'Next prime number:'
RANGE_START = 50_000_000
RANGE_END = 50_000_100


def main():
    print('Creating prime number list ...')
    created_prime_number_list = create_prime_number_list(RANGE_START, RANGE_END)
    print(created_prime_number_list)
    print(NEXT_PRIME_NUMBER_LABEL, end=' ')
    for current_prime_number in created_prime_number_list:
        print(current_prime_number, end='')
        input()
        print(NEXT_PRIME_NUMBER_LABEL, end=' ')

    print('\b' * 21, '-' * 100, sep='')

    print('Using prime number generator')
    print(NEXT_PRIME_NUMBER_LABEL, end=' ')
    for current_prime_number in prime_number_generator(RANGE_START, RANGE_END):
        print(current_prime_number, end='')
        input()
        print(NEXT_PRIME_NUMBER_LABEL, end=' ')

    print('\b' * 21, '-' * 100, sep='')


def create_prime_number_list(start, end):
    prime_number_list =[]
    for i in range(start, end):
        if is_prime(i):
            prime_number_list.append(i)
    return prime_number_list


def create_prime_number_list_comprehensions(start, end): 
    return [i for i in range(start, end) if is_prime(i)]


def prime_number_generator(start, end):
     for i in range(start, end):
        if is_prime(i):
            yield i

def prime_number_generator_comprehensions(start, end):
    return (i for i in range(start, end) if is_prime(i))

# stupid and slow prime number checker
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    main()
