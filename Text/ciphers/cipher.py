from collections import deque
from itertools import repeat
from math import ceil


class CipherBase(object):
    def encrypt(self, text):
        pass

    def decrypt(self, text):
        pass


class CaesarCipher(CipherBase):
    plain = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    def __init__(self, letter='', key=0):
        d = deque(self.plain)
        d.rotate(len(self.plain) - self.plain.index(letter) if letter != '' else key)
        self.cipher = list(d)
        self.encrypt_dict = dict(zip(self.plain, self.cipher))
        self.decrypt_dict = dict(zip(self.cipher, self.plain))

    @staticmethod
    def _process(cipher_dict, text):
        return ''.join([cipher_dict.get(x, ' ') for x in text.upper()])

    def encrypt(self, text):
        return self._process(self.encrypt_dict, text)

    def decrypt(self, text):
        return self._process(self.decrypt_dict, text)


class VigenereCipher(CipherBase):
    def __init__(self, keyword):
        self.keyword = keyword
        letters = list(set(self.keyword))
        self.caesar_ciphers = {l: CaesarCipher(letter=l) for l in letters}

    def _get_key(self, text):
        return ''.join(repeat(self.keyword, ceil(len(text) / len(self.keyword))))[:len(text)]

    def _process(self, text, op):
        key = self._get_key(text)
        return ''.join([getattr(self.caesar_ciphers[key[i]], op)(l) for i, l in enumerate(text.upper())])

    def encrypt(self, text):
        return self._process(text, 'encrypt')

    def decrypt(self, text):
        return self._process(text, 'decrypt')
