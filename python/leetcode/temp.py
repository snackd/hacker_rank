import random


class TetrisBot:

    def __init__(self):
        self.board = [[0] * 10 for _ in range(20)]
        self.shapes = [
            [[1, 1, 1, 1]],
            [[1, 1, 0], [0, 1, 1]],
            [[0, 1, 1], [1, 1, 0]],
            [[1, 1], [1, 1]],
            [[1, 0, 0], [1, 1, 1]],
            [[0, 0, 1], [1, 1, 1]],
            [[1, 1], [0, 1], [0, 1]],
        ]
        self.current_shape = self.new_shape()
        self.current_x = 3
        self.current_y = 0
        self.score = 0

    def new_shape(self):
        return random.choice(self.shapes)

    def rotate(self, shape):
        return [list(x[::-1]) for x in zip(*shape)]

    def can_move(self, shape, x, y):
        for i in range(len(shape)):
            for j in range(len(shape[i])):
                if shape[i][j] and (y + i >= 20 or x + j < 0 or x + j >= 10
                                    or self.board[y + i][x + j]):
                    return False
        return True

    def place_shape(self):
        for i in range(len(self.current_shape)):
            for j in range(len(self.current_shape[i])):
                if self.current_shape[i][j]:
                    self.board[self.current_y + i][self.current_x + j] = 1

    def remove_lines(self):
        lines_removed = 0
        for i in range(len(self.board)):
            if all(self.board[i]):
                self.board.pop(i)
                self.board.insert(0, [0] * 10)
                lines_removed += 1
        self.score += lines_removed**2

    def move_left(self):
        if self.can_move(self.current_shape, self.current_x - 1,
                         self.current_y):
            self.current_x -= 1

    def move_right(self):
        if self.can_move(self.current_shape, self.current_x + 1,
                         self.current_y):
            self.current_x += 1

    def move_down(self):
        if self.can_move(self.current_shape, self.current_x,
                         self.current_y + 1):
            self.current_y += 1
        else:
            self.place_shape()
            self.remove_lines()
            self.current_shape = self.new_shape()
            self.current_x = 3
            self.current_y = 0
            if not self.can_move(self.current_shape, self.current_x,
                                 self.current_y):
                return False
        return True

    def drop(self):
        while self.move_down():
            pass

    def play(self):
        while True:
            self.move_down()
            if not self.can_move(self.current_shape, self.current_x,
                                 self.current_y):
                break
        return self.score


if __name__ == '__main__':
    i = TetrisBot()
    TetrisBot()
