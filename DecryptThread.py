import threading


def caesar_decrypt(text, offset):
    decrypted = ''
    for char in text:
        if char.isalpha():
            shift = ord(char) - offset
            if char.islower():
                decrypted += chr((shift - 97) % 26 + 97)
            elif char.isupper():
                decrypted += chr((shift - 65) % 26 + 65)
        else:
            decrypted += char
    return decrypted


class DecryptThread(threading.Thread):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.decrypted_content = []

    def read_file(self):
        with open(self.filename, 'r') as file:
            return file.read()

    def run(self):
        try:
            content = self.read_file()
            decrypted_content = caesar_decrypt(content, 8)
            self.decrypted_content = decrypted_content.splitlines()
        except Exception as e:
            print(f"Error decrypting {self.filename}: {e}")
