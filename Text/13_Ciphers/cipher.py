from collections import deque

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


cip = CaesarCipher(letter='H')
#enc = cip.encrypt('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG')
dec = cip.decrypt('JHLZHY JPWOLYZ HYL LHZF AV IYLHR')

#print(enc)
print(dec)
