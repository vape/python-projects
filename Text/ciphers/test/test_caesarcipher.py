from unittest import TestCase
from Text.ciphers.cipher import CaesarCipher


class CaesarCipherTests(TestCase):
    def test_cipher_initialization_with_letter(self):
        cc_a = CaesarCipher(letter='A')
        self.assertEqual(cc_a.cipher[0], 'A')

        cc_x = CaesarCipher(letter='X')
        self.assertEqual(cc_x.cipher[0], 'X')

    def test_cipher_initialization_with_number(self):
        cc_0 = CaesarCipher(key=0)
        self.assertEqual(cc_0.cipher[0], 'A')

        cc_3 = CaesarCipher(key=3)
        self.assertEqual(cc_3.cipher[0], 'X')

    def test_cipher_encryption_with_key(self):
        cip = CaesarCipher(key=3)
        self.assertEqual(cip.encrypt('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'), 'QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD')

    def test_cipher_encryption_with_letter(self):
        cip = CaesarCipher(letter='X')
        self.assertEqual(cip.encrypt('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'), 'QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD')
