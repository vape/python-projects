from tkinter import *
from random import choice


class Cell(Canvas):
    _cell_status = {'EMPTY': 0, 'FULL': 1, 'FOOD': 2}
    _cell_fill = {0: 'black', 1: 'green', 2: 'yellow'}
    def __init__(self, master, row_index, column_index, size, stat='EMPTY'):
        super(Cell, self).__init__(master, height=size, width=size)
        self._size = size
        self._row = row_index
        self._col = column_index
        self.grid(row=row_index, column=column_index, sticky=N+W)
        self._status = self._cell_status.get(stat, 0)
        self._update_visual()

    def fill(self):
        self._status = self._cell_status['FULL']
        self._update_visual()

    def empty(self):
        self._status = self._cell_status['EMPTY']
        self._update_visual()

    def food(self):
        self._status = self._cell_status['FOOD']
        self._update_visual()

    def pos(self):
        return self._row, self._col

    def _update_visual(self):
        self.delete(ALL)
        self.create_rectangle(0, 0, self._size, self._size, fill=self._get_fill())
        self.update()

    def _get_fill(self):
        return self._cell_fill[self._status]


class SnakeGame(object):
    directions = {'UP': [0, -1], 'DOWN': [0, 1], 'LEFT': [-1, 0], 'RIGHT': [1, 0]}
    key_bindings = {38: 'UP', 87: 'UP', 83: 'DOWN', 40: 'DOWN', 39: 'RIGHT', 68: 'RIGHT', 37: 'LEFT', 65: 'LEFT'}
    statuses = ['RUNNING', 'PAUSED', 'OVER']
    cell_count = 10
    board_size = 500
    cell_dim = board_size // cell_count
    game_fps = 3
    refresh_rate = 1000 // game_fps

    def __init__(self, master):
        self._master = master
        self._master.geometry('{0}x{0}'.format(self.board_size))
        self._bind_keys()
        self._direction = choice(list(self.directions.keys()))
        self._is_running = False
        self._score = 0
        self._board = [[Cell(self._master, r, c, self.cell_dim, 'EMPTY') for c in range(self.cell_count)] for r in range(self.cell_count)]
        self._head_pos = (choice(range(self.cell_count//4, self.cell_count//2)), choice(range(self.cell_count//4, self.cell_count//2)))
        self._cell_at(self._head_pos).fill()
        self._snake_cells = [self._head_pos]
        self._food_pos = self._get_food_pos()
        self._cell_at(self._food_pos).food()

    def start_game(self):
        self._is_running = True
        self._advance()

    def _bind_keys(self):
        self._master.bind("<Key>", self._kb_click)

    def _kb_click(self, event):
        if not event.keycode or event.keycode not in self.key_bindings:
            return
        self._direction = self.key_bindings[event.keycode]

    def _cell_at(self, coord):
        return self._board[coord[0]][coord[1]]

    def _get_food_pos(self):
        flat_cells = []
        [[flat_cells.append(c.pos()) for c in r] for r in self._board]
        return choice(list(set(flat_cells) - set(self._snake_cells)))

    def _advance(self):
        if not self._is_running:
            return

        new_head_coord = (self._head_pos[0] + self.directions[self._direction][1], self._head_pos[1] + self.directions[self._direction][0])
        if new_head_coord[0] < 0 or new_head_coord[0] >= self.cell_count or new_head_coord[1] < 0 or new_head_coord[1] > self.cell_count:
            print('game over!')
            self._is_running = False
            return

        ate_food = new_head_coord == self._food_pos
        self._snake_cells.append(new_head_coord)
        self._cell_at(new_head_coord).fill()
        if ate_food:
            self._score += 1
            self._food_pos = self._get_food_pos()
            self._cell_at(self._food_pos).food()
        else:
            end_cell_coord = self._snake_cells.pop(0)
            self._cell_at(end_cell_coord).empty()

        self._head_pos = new_head_coord
        if self._is_running:
            self._master.after(self.refresh_rate, self._advance)

    def __str__(self):
        return 'board size: {0}, pos: {1}, dir: {2}'.format(self.cell_count, self._head_pos, self._direction)


root = Tk()
root.title('PySnake!')
snake = SnakeGame(root)
snake.start_game()

root.mainloop()
