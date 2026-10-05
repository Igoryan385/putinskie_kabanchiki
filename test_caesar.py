import unittest
from caesar import caesar_decrypt, caesar_encrypt


class TestCaesarCipher(unittest.TestCase):

    def test_encrypt_basic(self):
        self.assertEqual(caesar_encrypt("Hello", 3), "Khoor")

    def test_decrypt_basic(self):
        self.assertEqual(caesar_decrypt("Khoor", 3), "Hello")

    def test_non_alpha(self):
        self.assertEqual(caesar_encrypt("Hello, World! 123", 3), "Khoor, Zruog! 123")

    def Test_type_error_handling(self):
        with self.assertRaises(TypeError):
            caesar_encrypt(12345, 3)

        with self.assertRaises(TypeError):
            caesar_encrypt("Hello", "three")


if __name__ == "__main__":
    unittest.main()
