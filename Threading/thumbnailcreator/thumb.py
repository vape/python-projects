from wand.image import Image, ORIENTATION_TYPES
from os import path, mkdir, listdir
from os.path import isfile
from threading import Thread
from Classes.utils import initializer
from time import time
from multiprocessing import Process

files_dir = path.join(path.dirname(__file__), 'files')
output_dir = path.join(files_dir, 'out')
supported_formats = ['jpg', 'png']
thumbnail_size = { 'width': 120, 'height': 120 }

if not path.exists(output_dir):
    mkdir(output_dir)


class ImageResizer(Thread):
    @initializer(private=True)
    def __init__(self, id, input_dir, output_dir, filenames):
        Thread.__init__(self)

    @staticmethod
    def resize_image(id, input_dir, output_dir, filename):
        filepath = path.join(input_dir, filename)
        with Image(filename=filepath) as img:
            img.transform(resize='120x120>')
            img.strip()
            if img.orientation == 'left_bottom':
                img.rotate(270)
            elif img.orientation == 'right_bottom':
                img.rotate(90)

            img.save(filename=path.join(output_dir, filename))
            print('{0}: {1} resized.'.format(id, filename))

    def run(self):
        [ImageResizer.resize_image(self._id, self._input_dir, self._output_dir, fn) for fn in self._filenames]


def get_filenames():
    return [f for f in listdir(files_dir) if isfile(path.join(files_dir, f)) and path.splitext(f)[1].lower()[1:] in supported_formats]


def get_chunked_filenames():
    filenames = get_filenames()
    chunk_size = (len(filenames)//10) + 1
    return [filenames[x:x+chunk_size] for x in range(0, len(filenames), chunk_size)]


def _main_multithreading():
    chunks = get_chunked_filenames()
    threads = []
    for i, chunk in enumerate(chunks):
        threads.append(ImageResizer(i, files_dir, output_dir, chunk))

    [t.start() for t in threads]
    [t.join() for t in threads]


def _main_sequential():
    resize_images(get_filenames())


def resize_images(filenames):
    [ImageResizer.resize_image(0, files_dir, output_dir, f) for f in filenames]


def _main_multiprocess():
    chunks = get_chunked_filenames()
    procs = []
    for i, chunk in enumerate(chunks):
        procs.append(Process(target=resize_images, args=(chunk,)))

    [p.start() for p in procs]
    [p.join() for p in procs]


def main():
    start = time()
    #_main_sequential()
    #_main_multithreading()
    #_main_multiprocess()
    end = time()
    print('Resizing finished in {0:.2f} seconds.'.format(end - start))


if __name__ == '__main__':
    main()
