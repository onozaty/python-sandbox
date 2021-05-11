# https://twitter.com/kazuhirohat/status/1340816426282622976/photo/1

def main():

    successBoard = slove(9)

    print(successBoard)
    print(successBoard.index(0) + 1)


def slove(n):
    # カードの枚数*2 + ジョーカーの1枚
    card_num = (n * 2 + 1)

    remaining_cards = list(range(1, n + 1))

    # 未配置の状態で初期化 (-1: 未配置、0: ジョーカー)
    init_board = [-1] * card_num

    # 一番右にジョーカーが置ける位置を探したいので
    # 右側からジョーカーの位置を固定して探す
    for joker_index in reversed(range(card_num)):
        board = init_board.copy()
        board[joker_index] = 0

        successBoard = next(board, remaining_cards)

        if successBoard is not None:
            return successBoard

    return None


def next(board, remaining_cards):

    if len(remaining_cards) == 0:
        # 全てのカードが配置済みの場合は成功として終了
        return board

    # 配置位置
    index = board.index(-1)
    for remaining_card in remaining_cards:
        # 2枚目の位置
        pair_index = index + remaining_card + 1

        if pair_index < len(board) and board[pair_index] == -1:

            # 2枚目も置けた場合は、次のチェックへ
            next_board = board.copy()
            next_board[index] = remaining_card
            next_board[pair_index] = remaining_card

            next_remaining_cards = remaining_cards.copy()
            next_remaining_cards.remove(remaining_card)

            successBoard = next(next_board, next_remaining_cards)
            if successBoard is not None:
                return successBoard

    return None


if __name__ == '__main__':
    main()
