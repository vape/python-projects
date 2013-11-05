import requests
from os import path, mkdir
from string import ascii_lowercase
from random import choice
from math import log
from time import time, sleep
from sys import stderr, stdout
from Classes.utils import initializer
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

    @staticmethod
    def format_bytes(bytes):
        if bytes is None:
            return 'N/A'
        if type(bytes) is str:
            bytes = float(bytes)
        if bytes == 0.0:
            exponent = 0
        else:
            exponent = int(log(bytes, 1024.0))
        suffix = ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB'][exponent]
        converted = float(bytes) / float(1024 ** exponent)
        return '%.2f%s' % (converted, suffix)

    def _calculate_dl_speed(self):
        if not self._dl_start_time:
            return None
        dif = (self._dl_end_time or time()) - self._dl_start_time
        if bytes == 0 or dif < 0.001: # One millisecond
            return None
            #print(self._downloaded_bytes)
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
                        #if self._downloaded_chunks % 10 == 0:
                        #stdout.write(
                        #    '{0}/s\r'.format(self.format_bytes(self.calculate_dl_speed(dl_start_time, time()))))
                        #stdout.flush()
                        #print('\r{0}{1}/s'.format(clear_line, format_bytes(calculate_dl_speed(dl_start_time, time(), downloaded_bytes))))

            self._dl_end_time = time()
        except Exception as e:
            print('awesome error ', e, self._url)

    def run(self):
        self._download_file()


def main():
    def get_progress_bar(percent_complete, bar_length=100):
        percent_complete /= 100 / bar_length
        return '{0}{1}'.format('#' * int(percent_complete), '-' * (bar_length - int(percent_complete)))

    def report_progress(prog, preserve_line=True, show_progress_bar=True):
        stdout.write(
            '{0}{1}/s - {2:.0f}% complete. {3}'.format(get_progress_bar(prog[1], 50) + ' : ' if show_progress_bar else '',
                                                        FileDownloader.format_bytes(prog[0]), prog[1],
                                                        '\r' if preserve_line else ''))
        stdout.flush()

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