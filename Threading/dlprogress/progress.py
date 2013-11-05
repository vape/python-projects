import requests
from os import path, mkdir
from string import ascii_lowercase
from random import choice
from time import time, sleep
from sys import stderr, stdout
from Classes.utils import initializer
from Threading.dlprogress.utils import report_progress
from threading import Thread


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'}
files_dir = 'files'
chunk_size = 10240
clear_line = ('\x1b[K' if stderr.isatty() else '')

if not path.exists(files_dir):
    mkdir(files_dir)


class FileDownloader(Thread):
    @initializer(private=True)
    def __init__(self, url, target_path):
        Thread.__init__(self)
        self._is_downloading = False
        self._file_size_bytes = 0
        self._downloaded_chunks = 0
        self._downloaded_bytes = 0
        self._dl_start_time = None
        self._dl_end_time = None

    def _calculate_dl_speed(self):
        if not self._dl_start_time:
            return None
        dif = (self._dl_end_time or time()) - self._dl_start_time
        if bytes == 0 or dif < 0.001: # One millisecond
            return None
        return float(self._downloaded_bytes) / dif

    def _calculate_dl_progress(self):
        return 0 if not self._file_size_bytes else self._downloaded_bytes / self._file_size_bytes * 100

    def get_progress(self):
        return self._calculate_dl_speed(), self._calculate_dl_progress()

    def _download_file(self):
        try:
            r = requests.get(self._url, headers=headers, stream=True)
            self._file_size_bytes = int(r.headers['content-length'])

            self._dl_start_time = time()
            with open(self._target_path, 'wb') as image_file:
                for chunk in r.iter_content(chunk_size=chunk_size):
                    if chunk:
                        self._downloaded_bytes += chunk_size
                        self._downloaded_chunks += 0
                        image_file.write(chunk)
                        image_file.flush()

            self._dl_end_time = time()
        except Exception as e:
            print('awesome error ', e, self._url)

    def run(self):
        self._download_file()


def main():
    dl = FileDownloader('http://download.thinkbroadband.com/5MB.zip',
                        path.join(files_dir, '{0}.zip'.format(''.join(choice(ascii_lowercase) for x in range(10)))))
    dl.start()

    while dl.is_alive():
        report_progress(dl.get_progress())
        sleep(1)

    print('')
    print('Download finished. Download stats: ')
    report_progress(dl.get_progress(), preserve_line=False, show_progress_bar=False)


if __name__ == '__main__':
    main()