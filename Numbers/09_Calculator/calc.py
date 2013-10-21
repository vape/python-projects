from tkinter import *


def enum(name, *sequential, **named):
    values = dict(zip(sequential, range(len(sequential))), **named)
    return type(name, (), values)

Op = enum('Op', ADD='+', SUB='-', MUL='*', DIV='/')
Util = enum('Util', 'CLR', 'NEGATE', 'RESULT', 'FRACTION')


class Calculator(object):
    def __init__(self, master):
        self.max_input_length = 10
        self.result = 0
        self.memory_input = ''
        self.current_input = ''
        self.current_op = ''
        self.op_specified = False

        self.result_var = StringVar()
        self.result_label = Label(master, textvariable=self.result_var)
        self.result_label.grid(row=0, column=0, columnspan=4)

        self.bind_result()

        #row 1
        self.clear_button = Button(master, text='AC', command=self._ul(Util.CLR)).grid(row=1, column=0)
        self.plus_minus_button = Button(master, text='+/-', command=self._ul(Util.NEGATE)).grid(row=1, column=1)
        self.division_button = Button(master, text='÷', command=self._ol(Op.DIV)).grid(row=1, column=2)
        self.multiplication_button = Button(master, text='x', command=self._ol(Op.MUL)).grid(row=1, column=3)

        #row 2
        self.num_7_button = Button(master, text='7', command=self._nl(7)).grid(row=2, column=0)
        self.num_8_button = Button(master, text='8', command=self._nl(8)).grid(row=2, column=1)
        self.num_9_button = Button(master, text='9', command=self._nl(9)).grid(row=2, column=2)
        self.minus_button = Button(master, text='-', command=self._ol(Op.SUB)).grid(row=2, column=3)

        #row 3
        self.num_4_button = Button(master, text='4', command=self._nl(4)).grid(row=3, column=0)
        self.num_5_button = Button(master, text='5', command=self._nl(5)).grid(row=3, column=1)
        self.num_6_button = Button(master, text='6', command=self._nl(6)).grid(row=3, column=2)
        self.plus_button = Button(master, text='+', command=self._ol(Op.ADD)).grid(row=3, column=3)

        #row 4
        self.num_1_button = Button(master, text='1', command=self._nl(1)).grid(row=4, column=0)
        self.num_2_button = Button(master, text='2', command=self._nl(2)).grid(row=4, column=1)
        self.num_3_button = Button(master, text='3', command=self._nl(3)).grid(row=4, column=2)
        self.equals_button = Button(master, text='=', command=self._ul(Util.RESULT)).grid(row=4, column=3, rowspan=2)

        #row 5
        self.num_0_button = Button(master, text='0', command=self._nl(0)).grid(row=5, column=0, columnspan=2)
        self.fraction_button = Button(master, text=',').grid(row=5, column=2)

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
        if op == Util.NEGATE:
            self.result *= -1
        elif op == Util.CLR:
            self.current_op = ''
            self.result = 0
        elif op == Util.RESULT:
            res = eval('{0} {1} {2}'.format(self.memory_input or '0', self.current_op, self.current_input or '0'))
            self.current_input = str(res) if isinstance(res, int) else '{0:.4f}'.format(res)

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
        self.result_var.set(self.current_input or '0')

root = Tk()
root.title = 'Calculator'
root.geometry('300x400')
calc = Calculator(root)
root.mainloop()
