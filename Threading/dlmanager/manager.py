from Threading.dlprogress.progress import FileDownloader
from os import path
from random import choice
from string import ascii_lowercase
from Threading.dlprogress.utils import report_progress
from time import sleep

files_dir = 'files'


def main():
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
