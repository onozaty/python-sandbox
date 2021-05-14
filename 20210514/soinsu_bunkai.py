import sys


def main():

    argv = sys.argv
    num = int(argv[1])

    soinsu = slove(num)

    print(" x ".join([str(n) for n in soinsu]))


def slove(num):

    soinsu = []

    i = 2
    while num != 1:

        while num % i == 0:

            soinsu.append(i)
            num = num / i

        i += 1

    return soinsu


if __name__ == '__main__':
    main()
