
class NumberNameConverter(object):
    _cardinal_numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    _teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    _multiples_of_10 = ['', 'ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    _orders_of_magnitude = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion']

    def _get_digit_groups(self, num):
        """
        Splits a number into its three digit groups.
        The groups are sorted from last to first.
        Example:
        - 1 => ['1']
        - 1234 => ['234', '1']
        - 12345678 = ['678', '345', '12']

        :param num: The number as int or str
        :return: A list of (max) three digit numbers
        """
        num = (num if isinstance(num, str) else str(num))[::-1]
        return [''.join(num[x:x+3][::-1]) for x in range(0, len(num), 3)]

    def _convert_digit_group(self, group):
        """
        Convert a three digit number into string equivalent.
        :param group: Three digit number
        :return: String equivalent of given number
        """

        numstr = str(int(str(group)))

        if len(numstr) == 1:
            return self._cardinal_numbers[int(numstr)]
        elif len(numstr) == 2:
            if numstr[0] == '1':
                return self._teens[int(numstr[1])]
            elif numstr[1] == '0':
                return self._multiples_of_10[int(numstr[0])]
            else:
                return self._convert_digit_group(int(numstr[0]) * 10) + ' ' + self._convert_digit_group(int(numstr) % 10)
        else:
            if int(numstr) % 100 == 0:
                return '{0} hundred'.format(self._convert_digit_group(int(numstr) // 100))
            p1 = self._convert_digit_group(int(numstr[0])*100)
            p2 = self._convert_digit_group(int(numstr) % 100).strip()
            return '{0} {1} {2}'.format(p1, 'and' if p2 else '', p2).strip()

    def convert(self, num):
        """
        Converts given integer into string equivalent
        :param num: Number
        :return: String representing number in English words
        """
        if not isinstance(num, int):
            raise ValueError('Number must be integer.')

        numstr = str(num) if num >= 0 else str(num)[1:] # remove leading - sign (if it exists)

        groups = self._get_digit_groups(numstr)
        if len(groups) > len(self._orders_of_magnitude):
            raise ValueError('This converter supports numbers up to {0}s'.format(self._orders_of_magnitude[-1]))

        conv_groups = []
        for i, g in enumerate(groups):
            if len(groups) > 1 and int(g) == 0:
                continue
            converted = self._convert_digit_group(g)
            if converted:
                if i == 0 and int(g) < 100 and len(groups) > 1:
                    converted = 'and ' + converted
                conv_groups.append('{0} {1}'.format(converted, self._orders_of_magnitude[i]).strip())

        return '{0}{1}'.format('negative ' if num < 0 else '', ' '.join(conv_groups[::-1]))
