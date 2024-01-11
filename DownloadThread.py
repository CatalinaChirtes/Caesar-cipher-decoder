import threading
import requests


class DownloadThread(threading.Thread):
    def __init__(self, url: str, filename: str):
        super().__init__()

        # URL from which to download the file
        self.url = url

        # Filename to save the downloaded content
        self.filename = filename

    # Downloading content from the specified URL
    def download_file(self) -> bytes:
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.content
        return None

    # Saving the downloaded content to a file
    def save_content(self, content: bytes) -> None:
        if content:
            with open(self.filename, 'wb') as file:
                file.write(content)

    # Downloading and saving the content
    def run(self) -> None:
        try:
            content = self.download_file()
            self.save_content(content)
        except Exception as e:
            print(f"Error downloading {self.url}: {e}")
