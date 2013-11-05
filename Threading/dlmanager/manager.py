from Threading.dlprogress.progress import FileDownloader
from os import path
from random import choice
from string import ascii_lowercase
from sys import stdout
from time import sleep

files_dir = 'files'


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

    dl1 = FileDownloader('http://download.thinkbroadband.com/5MB.zip',
                        path.join(files_dir, '{0}.zip'.format(''.join(choice(ascii_lowercase) for x in range(10)))))

    dl2 = FileDownloader('http://download.thinkbroadband.com/5MB.zip',
                        path.join(files_dir, '{0}.zip'.format(''.join(choice(ascii_lowercase) for x in range(10)))))

    print('Starting downloads')
    dl1.start()
    dl2.start()

    while dl1.is_alive() or dl2.is_alive():
        report_progress(dl1.get_progress(), preserve_line=False, show_progress_bar=False)
        report_progress(dl2.get_progress(), show_progress_bar=False)
        sleep(1)

    dl1.join()
    dl2.join()

    print('Downloads complete')
    report_progress(dl1.get_progress(), preserve_line=False, show_progress_bar=False)
    report_progress(dl2.get_progress(), show_progress_bar=False)



if __name__ == '__main__':
    main()
