from src.piece import Piece
from src.color import Color


class Pawn(Piece):
    def char(self):
        return 'P'

    def can_move(self, board, row: int, col: int, row_1: int, col_1: int) -> bool:
        if col != col_1:
            return False
        if self.color == Color.WHITE:
            start_row = 2
            direction = 1
        else:
            start_row = 7
            direction = -1
        if row + direction == row_1:
            return True
        if row == start_row \
                and row + 2 * direction == row_1 \
                and board.get_piece(row + direction, col) is None:
            return True
        return False

    def can_attack(self, board, row: int, col: int, row_1: int, col_1: int) -> bool:
        if self.color == Color.WHITE:
            direction = 1
        else:
            direction = -1
        return row + direction == row_1 and abs(col - col_1) == 1

