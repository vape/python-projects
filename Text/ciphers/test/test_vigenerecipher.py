from unittest import TestCase
from Text.ciphers.cipher import VigenereCipher

class VigenereCipherTests(TestCase):
    def test_cipher_encryption(self):
        vig = VigenereCipher('LEMON')
        self.assertEqual(vig.encrypt('ATTACKATDAWN'), 'LXFOPVEFRNHR')

    def test_cipher_decryption(self):
        vig = VigenereCipher('LEMON')
        self.assertEqual(vig.decrypt('LXFOPVEFRNHR'), 'ATTACKATDAWN')
