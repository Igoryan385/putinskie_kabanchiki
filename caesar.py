import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def caesar_encrypt(text: str, shift: int) -> str:
    """Зашифровка с валидацией, логированием и оптимизированной сборкой строки."""
    if not isinstance(text, str):
        logging.error("Некорректный тип аргумента 'text': %s", type(text))
        raise TypeError("Параметр 'text' должен быть строкой (str).")

    if not isinstance(shift, int):
        logging.error("Некорректный тип аргумента 'shift': %s", type(shift))
        raise TypeError("Параметр 'shift' должен быть целым числом (int).")

    result_chars = []
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result_chars.append(encrypted_char)
        else:
            result_chars.append(char)

    logging.info("Успешно зашифровано сообщение длиной %d символов.", len(text))
    return "".join(result_chars)


def caesar_decrypt(encrypted_text: str, shift: int) -> str:
    logging.info("Запуск расшифровки сообщения...")
    return caesar_encrypt(encrypted_text, -shift)
