import sys


def main():
    argv = sys.argv
    limit = int(argv[1])

    for i in range(1, limit + 1):

        s = ""

        if i % 3 == 0:
            s += "Fizz"
        if i % 5 == 0:
            s += "Buzz"
        if s == "":
            s = str(i)

        print(s)


if __name__ == '__main__':
    main()
