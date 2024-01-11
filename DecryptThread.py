import threading


# Function to decrypt text using the Caesar cipher
def caesar_decrypt(text: str, offset: int) -> str:
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
    def __init__(self, filename: str):
        super().__init__()

        # Filename of the encrypted file
        self.filename = filename

        # List to store decrypted content
        self.decrypted_content = []

    # Function for reading the content of the encrypted file
    def read_file(self) -> str:
        with open(self.filename, 'r') as file:
            return file.read()

    def run(self) -> None:
        try:
            # Decrypting the content using the Caesar cipher
            content = self.read_file()
            decrypted_content = caesar_decrypt(content, 8)

            # Splitting the decrypted content into lines
            self.decrypted_content = decrypted_content.splitlines()
        except Exception as e:
            print(f"Error decrypting {self.filename}: {e}")
