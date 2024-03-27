from enum import Enum


class Color(Enum):
    BLACK = 0
    WHITE = 1


class Board:
    def __init__(self):
        self.__field = []
        self.__color = Color.WHITE
        for _ in range(8):
            self.__field.append([None] * 8)

    @property
    def current_player(self):
        return self.__color

    @property
    def field(self):
        return tuple([tuple(row) for row in self.__field])

    def get_piece(self, row: int, col: int):
        if 1 <= row <= 9 and 1 <= col <= 9:
            return self.field[row - 1][col - 1]
        return None



def convert_step(step: str) -> tuple | Exception:
    if len(step) != 2:
        raise Exception('Неверный формат шага (пример A8')
    s, n = step[0], step[1]
    if ord(s) < ord('A') or ord(s) > ord('H'):
        raise Exception('Допустимые символы: A-H')
    if ord(n) < ord('1') or ord(n) > ord('8'):
        raise Exception('Допустимые цифры: 1-8')
    return int(n), ord(s) - 64


def print_board(board: Board):
    print('     +' + '----+' * 8)
    for y in range(8, 0, -1):
        print(f'  {y}  |', end='')
        for x in range(1, 9):
            print(' ', end='')
            piece = board.get_piece(y, x)
            if piece is None:
                print('  ', end='')
            else:
                print(piece, end='')
            print(' |', end='')
        print()
        print('     +' + '----+' * 8)
    print(' ' * 5, end='')
    for x in range(8):
        print(f'  {chr(65 + x)}  ', end='')
    print()


def main():
    board = Board()
    while True:
        print_board(board)
        print('Команды:')
        print('    exit                 --выход')
        print('    move <from> <to>     --ход из клетки <from> в клетку <to>')
        if board.current_player == Color.WHITE:
            print('Ходят белые')
        else:
            print('Ходят черные')
        command = input('Введите команду: ')
        if command == 'exit':
            break
        command = command.split()
        if len(command) == 3 and command[0] == 'move':
            try:
                start = convert_step(command[1])
                end = convert_step(command[2])
                print(start, end)
                # ход
            except Exception as e:
                print('Ошибка:', e)
            finally:
                continue
        print('Неверная команда!')


main()
