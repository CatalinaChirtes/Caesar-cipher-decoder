import threading


class Combiner:
    def __init__(self):
        # Dictionary to store content with filenames as keys
        self.content_mapping = {}

        # Lock to ensure thread safety when modifying content_mapping
        self.lock = threading.Lock()

    # Function for adding content to the dictionary
    def add_content(self, filename: str, content: list) -> None:
        with self.lock:
            if filename not in self.content_mapping:
                self.content_mapping[filename] = content

    # Function for writing the s_final file
    def write_final_file(self, final_filename: str) -> None:
        try:
            with open(final_filename, 'w') as file:
                # Sorting filenames for consistent output
                for filename in sorted(self.content_mapping.keys()):
                    content = self.content_mapping[filename]
                    for line in content:
                        file.write(f"{line}\n")
        except Exception as e:
            print(f"Error writing {final_filename}: {e}")
