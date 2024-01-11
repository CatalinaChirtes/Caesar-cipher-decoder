from DownloadThread import DownloadThread
from DecryptThread import DecryptThread
from Combiner import Combiner


def download_files() -> None:
    # Creating DownloadThread instances for each file to be downloaded
    download_threads = [
        DownloadThread("https://advancedpython.000webhostapp.com/s1.txt", "s1_enc.txt"),
        DownloadThread("https://advancedpython.000webhostapp.com/s2.txt", "s2_enc.txt"),
        DownloadThread("https://advancedpython.000webhostapp.com/s3.txt", "s3_enc.txt")
    ]

    # Starting download threads
    for thread in download_threads:
        thread.start()

    # Waiting for all download threads to finish
    for thread in download_threads:
        thread.join()


def decrypt_files() -> list:
    # Creating DecryptThread instances for each encrypted file
    decrypt_threads = [
        DecryptThread("s1_enc.txt"),
        DecryptThread("s2_enc.txt"),
        DecryptThread("s3_enc.txt")
    ]

    # Starting decryption threads
    for thread in decrypt_threads:
        thread.start()

    # Waiting for all decryption threads to finish
    for thread in decrypt_threads:
        thread.join()
    return decrypt_threads


def combine_files(decrypt_threads: list) -> Combiner:
    # Creating a Combiner instance to combine decrypted content
    combiner = Combiner()

    # Adding decrypted content to the Combiner
    for decrypt_thread in decrypt_threads:
        filename = decrypt_thread.filename.replace("_enc.txt", ".txt")
        content = decrypt_thread.decrypted_content
        combiner.add_content(filename, content)
    return combiner


def main() -> None:
    # Downloading files
    download_files()

    # Decrypting files and obtaining DecryptThread instances
    decrypt_threads = decrypt_files()

    # Combining decrypted content using Combiner
    combiner = combine_files(decrypt_threads)

    # Writing the final combined content to a file
    combiner.write_final_file("s_final.txt")

    # Displaying the content of the final combined file
    with open("s_final.txt", "r") as file:
        print(file.read())


if __name__ == "__main__":
    main()
