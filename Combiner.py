import threading


class Combiner:
    def __init__(self):
        self.content_mapping = {}
        self.lock = threading.Lock()

    def add_content(self, filename, content):
        with self.lock:
            if filename not in self.content_mapping:
                self.content_mapping[filename] = content

    def write_final_file(self, final_filename):
        try:
            with open(final_filename, 'w') as file:
                for filename in sorted(self.content_mapping.keys()):
                    content = self.content_mapping[filename]
                    for line in content:
                        file.write(f"{line}\n")
        except Exception as e:
            print(f"Error writing {final_filename}: {e}")
