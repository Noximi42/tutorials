def average(*values: float, ignore_negative_values: bool = False):
    if 0 in values:
        raise ValueError("No zero values allowed")

    if ignore_negative_values:
        values = tuple(filter(lambda x: x > 0, values))

    return sum(values) / len(values)

def main():
    print(average(1,2,3,4,-5, ignore_negative_values = True))

if __name__ == "__main__":
    main()
