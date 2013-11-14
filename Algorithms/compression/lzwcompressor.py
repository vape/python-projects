from bitstring import BitArray
from collections import OrderedDict
from string import ascii_lowercase
from math import ceil, log


class LZWCompressor(object):
    def __init__(self, alphabet=''):
        self._alphabet = alphabet or ascii_lowercase+'_'
        self._max_key_length = ceil(log(len(self._alphabet), 2))
        self._dict = self._init_dict()

    def _init_dict(self):
        d = OrderedDict()
        for i, c in enumerate(self._alphabet):
            d[c] = BitArray(uint=i, length=self._max_key_length)
        return d

    def _increment_code_length(self):
        self._max_key_length += 1
        ndict = OrderedDict()
        for k, v in self._dict.items():
            ndict[k] = BitArray(uint=v.uint, length=self._max_key_length)
        self._dict = ndict

    def _add_to_dict(self, v):
        if ceil(log(len(self._dict), 2)) + 1 > self._max_key_length:
            self._increment_code_length()
        self._dict[v] = BitArray(uint=len(self._dict), length=self._max_key_length)

    def compress(self, data, file=''):
        out = []
        s = ''
        for c in data:
            t = s+c
            if t in self._dict:
                s += c
            else:
                out.append(s)
                self._add_to_dict(t)
                s = c
        out.append(s)
        if file:
            with open(file, 'wb') as f:
                [self._dict[e].tofile(f) for e in out]
        return [self._dict[e].bin for e in out]

