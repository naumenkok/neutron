from class_color import Color


class Piece:
    IMG = ("🔴", "⚪", "⭐")

    def __init__(self, color):
        self.color = color

    def check_start_position(self, moves, x, y):
        start_position = [x, y]
        while start_position in moves:
            moves.remove(start_position)
        return moves

    def variants_of_moving_diagonal(self, board, x, y):
        moves = []
        for i in (-1, 1):
            for j in (-1, 1):
                moves_diag = self.loop_for_variants(board, moves, x, y, i, j)
        return moves_diag

    def variants_of_moving_all(self, board, x, y):
        moves_diag = self.variants_of_moving_diagonal(board, x, y)
        for j in (-1, 1):
            i = 0
            moves_ver_diag = self.loop_for_variants(board, moves_diag, x, y, i, j)
            moves_hor_ver_diag = self.loop_for_variants(
                board, moves_ver_diag, x, y, j, i
            )
        moves_all = moves_hor_ver_diag
        self.check_start_position(moves_all, x, y)
        return moves_all

    def loop_for_variants(self, board, moves, x, y, i, j):
        x_i = x + i
        y_j = y + j
        while (0 <= x_i <= 4) and (0 <= y_j <= 4):
            color = board.get_color(x_i, y_j)
            if color != Color.empty:
                break
            x_i += i
            y_j += j
        moves.append([x_i - i, y_j - j])
        return moves

    def __str__(self):
        pict = (
            self.IMG[0]
            if self.color == Color.red
            else self.IMG[1]
            if self.color == Color.white
            else self.IMG[2]
        )
        return pict
