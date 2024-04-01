from src.piece import Piece


class Knight(Piece):
    def char(self):
        return 'N'

    def can_move(self, board, row: int, col: int, row_1: int, col_1: int) -> bool:
        diff_row = abs(row - row_1)
        diff_col = abs(col - col_1)
        return diff_row == 2 and diff_col == 1 or\
            diff_row == 1 and diff_col == 2

    def can_attack(self, board, row: int, col: int, row_1: int, col_1: int) -> bool:
        return self.can_move(board, row, col, row_1, col_1)