# 7セグメントディスプレイをヨコに並べて複数桁を表示した時、点灯してる場所を数え、各桁での点灯数の「積」を求めます。
# そして、この積を同じディスプレイに表示するのを繰り返すことを考えます。
# 例: 718 -> 718,42,20,30の4種類
import sys
import math


def main():

    argv = sys.argv
    num = int(argv[1])

    pattern = solve(num)

    # 123456 -> [123456, 6000, 1296, 360, 180, 84, 28, 35, 25] の9種類
    print(len(pattern))
    print(pattern)


# 数字毎の点灯数
TENTO = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]


def solve(num):

    pattern = []

    # 既に登場した数があった場合、その後は同じ結果しか出てこないので打ち切り
    while not (num in pattern):

        pattern.append(num)

        # 文字列→各桁の数字→点灯数の積
        num = math.prod(map(lambda x: TENTO[int(x)], str(num)))

    return pattern


if __name__ == '__main__':
    main()
