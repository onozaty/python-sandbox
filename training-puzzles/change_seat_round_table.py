# https://twitter.com/kazuhirohat/status/1341179311642923008/photo/4

def main():

    count = slove(10)

    print(count)


def slove(n):

    # 生徒は1からの番号で識別
    students = list(range(1, n + 1))

    # テーブルは先頭に先生(0)、その他は未着席で
    # 未配置の状態で初期化 (-1: 未配置)
    table = [-1] * (n + 1)
    table[0] = 0

    return next(table, students)


def next(table, remaining_students):

    table_seat_num = len(table)
    max_student = table_seat_num - 1

    if len(remaining_students) == 0:
        # 全ての着席済みならば成功として終了
        return 1

    count = 0

    # 着席位置
    index = table.index(-1)
    for remaining_student in remaining_students:

        # 基準時の両隣
        baseRight = remaining_student - 1
        baseLeft = 0 if (remaining_student == max_student) else remaining_student + 1

        # 現在の両隣
        nowRight = table[index - 1]
        nowLeft = table[(index + 1)] if (index + 1) < len(table) else table[0]  # 末尾は先頭と比較

        # 両隣が基準時と異なること
        if nowRight != baseRight and nowRight != baseLeft and nowLeft != baseRight and nowLeft != baseLeft:
            # 次の座席のチェックへ
            next_table = table.copy()
            next_table[index] = remaining_student

            next_remaining_students = remaining_students.copy()
            next_remaining_students.remove(remaining_student)

            count += next(next_table, next_remaining_students)

    return count


if __name__ == '__main__':
    main()
