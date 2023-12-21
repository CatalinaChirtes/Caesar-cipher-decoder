from DownloadThread import DownloadThread
from DecryptThread import DecryptThread
from Combiner import Combiner


def download_files():
    download_threads = [
        DownloadThread("https://advancedpython.000webhostapp.com/s1.txt", "s1_enc.txt"),
        DownloadThread("https://advancedpython.000webhostapp.com/s2.txt", "s2_enc.txt"),
        DownloadThread("https://advancedpython.000webhostapp.com/s3.txt", "s3_enc.txt")
    ]

    for thread in download_threads:
        thread.start()
    for thread in download_threads:
        thread.join()


def decrypt_files():
    decrypt_threads = [
        DecryptThread("s1_enc.txt"),
        DecryptThread("s2_enc.txt"),
        DecryptThread("s3_enc.txt")
    ]

    for thread in decrypt_threads:
        thread.start()
    for thread in decrypt_threads:
        thread.join()
    return decrypt_threads


def combine_files(decrypt_threads):
    combiner = Combiner()
    for decrypt_thread in decrypt_threads:
        filename = decrypt_thread.filename.replace("_enc.txt", ".txt")
        content = decrypt_thread.decrypted_content
        combiner.add_content(filename, content)
    return combiner


def main():
    download_files()
    decrypt_threads = decrypt_files()
    combiner = combine_files(decrypt_threads)
    combiner.write_final_file("s_final.txt")

    with open("s_final.txt", "r") as file:
        print(file.read())


if __name__ == "__main__":
    main()
