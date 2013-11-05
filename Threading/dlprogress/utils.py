from sys import stdout
from math import log


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


def get_progress_bar(percent_complete, bar_length=100):
    percent_complete /= 100 / bar_length
    return '{0}{1}'.format('#' * int(percent_complete), '-' * (bar_length - int(percent_complete)))


def report_progress(prog, preserve_line=True, show_progress_bar=True):
    stdout.write(
        '{0}{1}/s - {2:.0f}% complete. {3}'.format(get_progress_bar(prog[1], 50) + ' : ' if show_progress_bar else '',
                                                   format_bytes(prog[0]), prog[1],
                                                   '\r' if preserve_line else ''))
    stdout.flush()
