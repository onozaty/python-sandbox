import sys


def main():
    argv = sys.argv
    start = int(argv[1])

    for i in range(start, -1, -1):
        print(i)


if __name__ == '__main__':
    main()
