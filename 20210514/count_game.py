# 1から3まで数えて、後手が0を言ったら勝ち
# 5 だと 7パターン

import sys


def main():

    argv = sys.argv
    num = int(argv[1])

    win_count = solve(num)

    print(win_count)


def solve(num):

    return count(num, True, {True: {}, False: {}})


def count(current, is_first, cache):

    # まずはキャッシュから
    if current in cache[is_first]:
        return cache[is_first][current]

    if current == 0:
        if not is_first:
            return 1  # 後手に0を言わせたので勝ち
        else:
            return 0

    win_count = 0

    # 1から3まで数える
    for i in range(1, 4):
        if current < i:
            # 残りより多い場合は数えられないので終わり
            break

        win_count += count(current - i, not is_first, cache)

    # 結果をキャッシュに保存
    cache[is_first][current] = win_count

    return win_count


if __name__ == '__main__':
    main()
