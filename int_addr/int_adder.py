import sys


def adder(integers):
    for i in integers:
        if not i.isdigit():
            return ValueError(f'input {repr(i)} is not an integer!')
    return sum(map(int, integers))


def main():
    print(adder(sys.argv[1:]))


if __name__ == '__main__':
    main()
