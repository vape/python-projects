from tkinter import *
from itertools import chain

def enum(name, *sequential, **named):
    values = dict(zip(sequential, range(len(sequential))), **named)
    return type(name, (), values)

Op = enum('Op', ADD='+', SUB='-', MUL='*', DIV='/')
Util = enum('Util', 'CLR', 'NEGATE', 'RESULT', 'FRACTION')

button_font = ('Tahoma', '12')
result_font = ('Courier New', '26')
base_button_style = {
    'padx': 7,
    'pady': 3,
    'font': button_font,
    #'width': 5
}

button_narrow = {
    'width': 3
}

button_wide = {
    'width': 8
}

tall_button = {
    'height': 3
}

base_grid_style = {
    'padx': 3,
    'pady': 3
}

def comb(*dicts):
    return dict(chain(*map(dict.items, list(dicts))))


class Calculator(object):
    def __init__(self, master):
        self.max_input_length = 10
        self.result = 0
        self.memory_input = ''
        self.current_input = ''
        self.current_op = ''
        self.op_specified = False

        self.result_var = StringVar()
        self.result_label = Label(master, textvariable=self.result_var, font=result_font, width=10, justify=RIGHT, bg='DarkGrey', **base_grid_style)
        self.result_label.grid(row=0, column=0, columnspan=4)

        self.bind_result()

        #row 1
        self.clear_button = Button(master, text='AC', command=self._ul(Util.CLR), **comb(base_button_style, button_narrow)).grid(row=1, column=0, **base_grid_style)
        self.plus_minus_button = Button(master, text='+/-', command=self._ul(Util.NEGATE), **comb(base_button_style, button_narrow)).grid(row=1, column=1, **base_grid_style)
        self.division_button = Button(master, text='÷', command=self._ol(Op.DIV), **comb(base_button_style, button_narrow)).grid(row=1, column=2, **base_grid_style)
        self.multiplication_button = Button(master, text='x', command=self._ol(Op.MUL), **comb(base_button_style, button_narrow)).grid(row=1, column=3, **base_grid_style)

        #row 2
        self.num_7_button = Button(master, text='7', command=self._nl(7), **comb(base_button_style, button_narrow)).grid(row=2, column=0, **base_grid_style)
        self.num_8_button = Button(master, text='8', command=self._nl(8), **comb(base_button_style, button_narrow)).grid(row=2, column=1, **base_grid_style)
        self.num_9_button = Button(master, text='9', command=self._nl(9), **comb(base_button_style, button_narrow)).grid(row=2, column=2, **base_grid_style)
        self.minus_button = Button(master, text='-', command=self._ol(Op.SUB), **comb(base_button_style, button_narrow)).grid(row=2, column=3, **base_grid_style)

        #row 3
        self.num_4_button = Button(master, text='4', command=self._nl(4), **comb(base_button_style, button_narrow)).grid(row=3, column=0, **base_grid_style)
        self.num_5_button = Button(master, text='5', command=self._nl(5), **comb(base_button_style, button_narrow)).grid(row=3, column=1, **base_grid_style)
        self.num_6_button = Button(master, text='6', command=self._nl(6), **comb(base_button_style, button_narrow)).grid(row=3, column=2, **base_grid_style)
        self.plus_button = Button(master, text='+', command=self._ol(Op.ADD), **comb(base_button_style, button_narrow)).grid(row=3, column=3, **base_grid_style)

        #row 4
        self.num_1_button = Button(master, text='1', command=self._nl(1), **comb(base_button_style, button_narrow)).grid(row=4, column=0, **base_grid_style)
        self.num_2_button = Button(master, text='2', command=self._nl(2), **comb(base_button_style, button_narrow)).grid(row=4, column=1, **base_grid_style)
        self.num_3_button = Button(master, text='3', command=self._nl(3), **comb(base_button_style, button_narrow)).grid(row=4, column=2, **base_grid_style)
        self.equals_button = Button(master, text='=', command=self._ul(Util.RESULT), **comb(base_button_style, tall_button)).grid(row=4, column=3, rowspan=2, **base_grid_style)

        #row 5
        self.num_0_button = Button(master, text='0', command=self._nl(0), **comb(base_button_style, button_wide)).grid(row=5, column=0, columnspan=2, **base_grid_style)
        self.fraction_button = Button(master, text=',', command=self._ul(Util.FRACTION), **comb(base_button_style, button_narrow)).grid(row=5, column=2, **base_grid_style)

    def num_button_callback(self, num):
        if self.op_specified:
            self.op_specified = False
            self.current_input = ''
        if len(self.current_input) == self.max_input_length:
            return
        self.current_input += str(num)
        self.current_input = self.current_input.lstrip('0')
        self.bind_result()

    def op_button_callback(self, op):
        self.current_op = op
        self.op_specified = True
        self.memory_input = self.current_input

    def util_button_callback(self, op):
        if op == Util.NEGATE and self.current_input != '':
            if self.current_input[0] == '-':
                self.current_input = self.current_input.lstrip('-')
            else:
                self.current_input = '-' + self.current_input
        elif op == Util.CLR:
            self.current_op = ''
            self.current_input = ''
            self.memory_input = ''
            self.result = 0
        elif op == Util.FRACTION:
            if self.op_specified:
                self.op_specified = False
                self.current_input = ''
            if self.current_input == '':
                self.current_input = '0.'
            elif '.' not in self.current_input:
                self.current_input += '.'
        elif op == Util.RESULT:
            inputval = self.current_input or '0'
            res = eval('{0} {1} {2}'.format(self.memory_input or '0', self.current_op, '0' + self.current_input if inputval[0] == '.' else self.current_input.rstrip('.')))
            self.current_input = str(res) if isinstance(res, int) else '{0:g}'.format(res)

        self.bind_result()

    def _nl(self, num):
        """
        Utility method to return a lambda which calls the num_button_callback function
        with a specific number. We have this so the Button definitions can be shorter.
        :param num: value to call num_button_callback with
        :return: a lambda which calls num_button_callback
        """
        return lambda: self.num_button_callback(num)

    def _ol(self, op):
        """
        Utility method to return a lambda which calls the op_button_callback function
        with a specific number. We have this so the Button definitions can be shorter.
        :param op: op to call op_button_callback with
        :return: a lambda which calls op_button_callback
        """
        return lambda: self.op_button_callback(op)

    def _ul(self, op):
        return lambda: self.util_button_callback(op)

    def bind_result(self):
        inputval = self.current_input or '0'
        self.result_var.set('0' + self.current_input if inputval[0] == '.' else inputval)

root = Tk()
root.title('Calculator')
calc = Calculator(root)
root.mainloop()
