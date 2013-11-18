from tkinter import *
from random import choice


class Cell(Canvas):
    _cell_status = {'EMPTY': 0, 'FULL': 1}
    def __init__(self, master, row_index, column_index, size, stat='EMPTY'):
        super(Cell, self).__init__(master, height=size, width=size)
        self._size = size
        self.grid(row=row_index, column=column_index, sticky=N+W)
        self._status = self._cell_status.get(stat, 0)
        self.create_rectangle(0, 0, self._size, self._size, fill=self.get_fill())



    @property
    def status(self):
        return self._status

    def fill(self):
        self._status = self._cell_status['FULL']

    def empty(self):
        self._status = self._cell_status['EMPTY']

    def get_fill(self):
        return 'black' if self.status == self._cell_status['EMPTY'] else 'green'


class SnakeBoard(object):
    directions = {'UP': [0, -1], 'DOWN': [0, 1], 'LEFT': [-1, 0], 'RIGHT': [1, 0]}
    cell_count = 10
    board_size = 500
    cell_dim = board_size // cell_count

    def __init__(self, master):
        self._master = master
        self._master.geometry('{0}x{0}'.format(self.board_size))
        self._board = []
        self._pos = (choice(range(self.cell_count//4, self.cell_count//2)), choice(range(self.cell_count//4, self.cell_count//2)))
        self._snake_cells = [self._pos]
        for r in range(self.cell_count):
            self._board.append([])
            for c in range(self.cell_count):
                self._board[r].append(Cell(self._master, r, c, self.cell_dim, 'FULL' if self._pos[0] == r and self._pos[1] == c else 'EMPTY'))

        print(self._pos)
        self._board[self._pos[0]][self._pos[1]].fill()
        self._direction = choice(list(self.directions.keys()))

    def advance(self):
        self._pos = (self._pos[0] + self.directions[self._direction][0], self._pos[2] + self.directions[self._direction][1])
        self._snake_cells.pop(0)
        self._snake_cells.append(self._pos)

    def _draw_board(self):
        for ri, row in enumerate(self._board):
            for ci, cell in enumerate(row):
                cnvs = Canvas(self._master, width=self.cell_dim, height=self.cell_dim)
                cnvs.grid(row=ri, column=ci, sticky=N+W)
                #cnvs.pack()
                cnvs.create_rectangle(0, 0, self.cell_dim, self.cell_dim, fill=cell.get_fill())

    def __str__(self):
        return 'board size: {0}, pos: {1}, dir: {2}'.format(self.cell_count, self._pos, self._direction)


root = Tk()
root.title('PySnake!')
snake = SnakeBoard(root)
root.mainloop()
