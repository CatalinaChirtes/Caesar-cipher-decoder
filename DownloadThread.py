import threading
import requests


class DownloadThread(threading.Thread):
    def __init__(self, url, filename):
        super().__init__()
        self.url = url
        self.filename = filename

    def download_file(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.content
        return None

    def save_content(self, content):
        if content:
            with open(self.filename, 'wb') as file:
                file.write(content)

    def run(self):
        try:
            content = self.download_file()
            self.save_content(content)
        except Exception as e:
            print(f"Error downloading {self.url}: {e}")
