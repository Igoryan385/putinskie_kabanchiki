def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(encrypted_text, shift):
    return caesar_encrypt(encrypted_text, -shift)

if __name__ == "__main__":
<<<<<<< HEAD
    text = "Hello World"
    shift = 5
=======
    text = "Secret Message"
    shift = 3
>>>>>>> feature-branch
    encrypted = caesar_encrypt(text, shift)
    print(f"Зашифровано: {encrypted}")
