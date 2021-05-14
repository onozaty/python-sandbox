# 1から3まで数えて、後手が0を言ったら勝ち
# 5 だと 7パターン

import sys


def main():

    argv = sys.argv
    num = int(argv[1])

    win_count = solve(num)

    print(win_count)


def solve(num):

    return count(num, True, {}, {})


def count(current, is_first, first_cache, second_cache):

    # まずはキャッシュから
    if is_first and (current in first_cache):
        return first_cache[current]

    if not is_first and (current in second_cache):
        return second_cache[current]

    if current == 0:
        if not is_first:
            return 1  # 後手
        else:
            return 0  # 先手

    win_count = 0

    for i in range(1, 4):
        if current < i:
            break

        win_count += count(current - i, not is_first, first_cache, second_cache)

    # 結果をキャッシュに保存
    if is_first:
        first_cache[current] = win_count
    else:
        second_cache[current] = win_count

    return win_count


if __name__ == '__main__':
    main()
