from .color import Color
from .pawn import Pawn
from .knight import Knight


class Board:
    def __init__(self):
        self.__field = []
        self.__color = Color.WHITE
        for _ in range(8):
            self.__field.append([None] * 8)
        self.__fill()

    def __fill(self):
        for col in range(8):
            self.__field[1][col] = Pawn(Color.WHITE)
            self.__field[6][col] = Pawn(Color.BLACK)
        for col in [1, 6]:
            self.__field[0][col] = Knight(Color.WHITE)
            self.__field[7][col] = Knight(Color.BLACK)

    @property
    def current_player(self):
        return self.__color

    @property
    def field(self):
        return tuple([tuple(row) for row in self.__field])

    @staticmethod
    def __validate_coord(row: int, col: int) -> bool:
        return 1 <= row <= 9 and 1 <= col <= 9

    def get_piece(self, row: int, col: int):
        if self.__validate_coord(row, col):
            return self.field[row - 1][col - 1]
        return None

    def move_piece(self, row: int, col: int, row_1: int, col_1: int) -> bool:
        piece = self.get_piece(row, col)
        if piece is None:
            return False
        if piece.color != self.current_player:
            return False
        if not self.__validate_coord(row_1, col_1):
            return False
        if self.get_piece(row_1, col_1) is None:
            if not piece.can_move(self, row, col, row_1, col_1):
                return False
        elif self.get_piece(row_1, col_1).color != self.current_player:
            if not piece.can_attack(self, row, col, row_1, col_1):
                return False
        else:
            return False
        self.__field[row - 1][col - 1] = None
        self.__field[row_1 - 1][col_1 - 1] = piece
        self.__color = Color.WHITE if self.__color == Color.BLACK else Color.BLACK
        return True
