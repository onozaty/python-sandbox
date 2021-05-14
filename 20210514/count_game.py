# 1から3まで数えて、後手が0を言ったら勝ち
# 5 だと 7パターン

import sys


def main():

    argv = sys.argv
    num = int(argv[1])

    win_count = solve(num)

    print(win_count)


def solve(num):

    return count(num, True)


def count(current, is_first):

    if current == 0:
        if not is_first:
            return 1  # 後手
        else:
            return 0  # 先手

    win_count = 0

    for i in range(1, 4):
        if current < i:
            break

        win_count += count(current - i, not is_first)

    return win_count


if __name__ == '__main__':
    main()
