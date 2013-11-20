from tkinter import *
from random import choice
from copy import copy


def enum(name, *sequential, **named):
    values = dict(zip(sequential, range(len(sequential))), **named)
    return type(name, (), values)

GameStatus = enum('GameStatus', UNINITIALIZED=0, RUNNING=1, PAUSED=2, OVER=3)


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
    key_bindings = {38: 'UP', 87: 'UP', 83: 'DOWN', 40: 'DOWN', 39: 'RIGHT', 68: 'RIGHT', 37: 'LEFT', 65: 'LEFT', 32: 'PAUSE'}
    statuses = ['RUNNING', 'PAUSED', 'OVER']
    cell_count = 10
    board_size = 500
    control_panel_height=30
    cell_dim = board_size // cell_count
    game_fps = 3
    max_level = 10
    refresh_rate = 1000 // game_fps

    def __init__(self, master):
        self._status = GameStatus.UNINITIALIZED
        self._master = master
        self._init_master()
        self._bind_keys()
        self._init_direction()
        self._init_score()
        board_frame = self._init_board_frame()
        self._board = [[Cell(board_frame, r, c, self.cell_dim, 'EMPTY') for c in range(self.cell_count)] for r in range(self.cell_count)]
        self._init_snake_and_food()
        self._init_ui()

    def _init_master(self):
        self._master.geometry('{0}x{1}'.format(self.board_size+70, self.board_size+self.control_panel_height+50))

    def _init_direction(self):
        self._direction = choice(list(self.directions.keys()))
        self._next_direction = copy(self._direction)

    def _init_score(self):
        self._score = 0
        self._level = 1
        self._score_var = IntVar(self._master, self._score)
        self._level_var = IntVar(self._master, self._level)

    def _init_snake_and_food(self):
        self._head_pos = (choice(range(self.cell_count//4, self.cell_count//2)), choice(range(self.cell_count//4, self.cell_count//2)))
        self._cell_at(self._head_pos).fill()
        self._snake_cells = [self._head_pos]
        self._food_pos = self._get_food_pos()
        self._cell_at(self._food_pos).food()

    def _init_board_frame(self):
        board_frame = Frame(self._master, height=self.board_size, width=self.board_size)
        board_frame.grid(row=0, column=0)
        board_frame.pack()
        return board_frame

    def _init_ui(self):
        game_control_frame = Frame(self._master, height=self.control_panel_height, width=self.board_size)
        game_control_frame.grid(row=1, column=0)
        game_control_frame.pack()
        new_game_button = Button(game_control_frame, text='New Game', command=self._new_game_click)
        new_game_button.grid(row=0, column=0)
        pause_game_button = Button(game_control_frame, text='Pause', command=self._pause_click)
        pause_game_button.grid(row=0, column=1)
        score_label = Label(game_control_frame, text='Score: ')
        score_label.grid(row=0, column=2)
        score_value_label = Label(game_control_frame, textvariable=self._score_var)
        score_value_label.grid(row=0, column=3)
        level_label = Label(game_control_frame, text='Level: ')
        level_label.grid(row=0, column=4)
        level_value_label = Label(game_control_frame, textvariable=self._level_var)
        level_value_label.grid(row=0, column=5)

    def start_game(self):
        self._status = GameStatus.RUNNING
        self._advance()

    @property
    def _is_running(self):
        return self._status == GameStatus.RUNNING

    def _bind_keys(self):
        self._master.bind("<Key>", self._kb_click)

    def _kb_click(self, event):
        if not event.keycode or event.keycode not in self.key_bindings:
            return
        if self.key_bindings[event.keycode] == 'PAUSE':
            self._pause_click()
            return
        if not self._is_running:
            return
        if -self.directions[self._direction][0] == self.directions[self.key_bindings[event.keycode]][0] or -self.directions[self._direction][1] == self.directions[self.key_bindings[event.keycode]][1]:
            return
        self._next_direction = self.key_bindings[event.keycode]

    def _cell_at(self, coord):
        return self._board[coord[0]][coord[1]]

    def _get_food_pos(self):
        flat_cells = []
        [[flat_cells.append(c.pos()) for c in r] for r in self._board]
        return choice(list(set(flat_cells) - set(self._snake_cells)))

    def _reset_level(self):
        self._level = 1
        self._level_var.set(self._level)

    def _increment_level(self):
        self._level += 1
        self._level_var.set(self._level)
        self.game_fps += self._level // 2
        self.refresh_rate = 1000 // self.game_fps

    def _reset_score(self):
        self._score = 0
        self._score_var.set(self._score)

    def _increment_score(self):
        self._score += 1
        self._score_var.set(self._score)

    def _pause_click(self):
        if self._status not in (GameStatus.RUNNING, GameStatus.PAUSED):
            return
        self._status = GameStatus.PAUSED if self._status == GameStatus.RUNNING else GameStatus.RUNNING
        if self._status == GameStatus.RUNNING:
            self._advance()

    def _new_game_click(self):
        if self._status in (GameStatus.RUNNING, GameStatus.PAUSED):
            return
        self._init_score()
        [[c.empty() for c in r] for r in self._board]
        self._init_snake_and_food()
        self._init_direction()
        self.start_game()

    def _advance(self):
        if self._status != GameStatus.RUNNING:
            return

        self._direction = copy(self._next_direction)
        new_head_coord = (self._head_pos[0] + self.directions[self._direction][1], self._head_pos[1] + self.directions[self._direction][0])
        if new_head_coord[0] < 0 or new_head_coord[0] >= self.cell_count or new_head_coord[1] < 0 or new_head_coord[1] > self.cell_count:
            print('game over! hit wall')
            self._status = GameStatus.OVER
            return
        if new_head_coord in self._snake_cells:
            print('game over! hit self')
            self._status = GameStatus.OVER
            return

        ate_food = new_head_coord == self._food_pos
        self._snake_cells.append(new_head_coord)
        self._cell_at(new_head_coord).fill()
        if ate_food:
            self._increment_score()
            self._food_pos = self._get_food_pos()
            self._cell_at(self._food_pos).food()
            if self._score / self.max_level > self._level:
                self._increment_level()
        else:
            end_cell_coord = self._snake_cells.pop(0)
            self._cell_at(end_cell_coord).empty()

        self._head_pos = new_head_coord
        if self._status == GameStatus.RUNNING:
            self._master.after(self.refresh_rate, self._advance)

    def __str__(self):
        return 'board size: {0}, pos: {1}, dir: {2}'.format(self.cell_count, self._head_pos, self._direction)


root = Tk()
root.title('PySnake!')
snake = SnakeGame(root)
snake.start_game()

root.mainloop()
