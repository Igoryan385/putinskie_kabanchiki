import unittest
from main import caesar_encrypt, caesar_decrypt


class TestCaesarCipher(unittest.TestCase):

    def test_encryption(self):
        self.assertEqual(caesar_encrypt("abc", 1), "bcd")

    def test_decryption(self):
        self.assertEqual(caesar_decrypt("bcd", 1), "abc")


if __name__ == "__main__":
    unittest.main()
