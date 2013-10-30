from datetime import datetime as dt
from datetime import time, timedelta
from threading import Timer
from os import name as osname
import winsound

parsers = [
    lambda x: ('a', dt.strptime(x, '%H:%M').time()),
    lambda x: ('t', dt.strptime(x, '%Mm').time()),
    lambda x: ('t', dt.strptime(x, '%Mm%Ss').time()),
    lambda x: ('t', dt.strptime(x, '%Ss').time())
]
clear_line = (u'\x1b[K' if osname != 'nt' else '\r')

def parse_input(i):
    for parser in parsers:
        try:
            t = parser(i)
            return t
        except:
            continue
    return None


def play_sound():
    if osname != 'nt':
        return
    winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)


def alarm(msg):
    print(msg)
    play_sound()


def timer_tick(target_time):
    time_left = int((target_time - dt.now()).total_seconds())
    if time_left <= 0:
        alarm('Timer finished!')
        return
    print('{0}{1:d} seconds to go.'.format(clear_line, time_left))
    Timer(1, timer_tick, [target_time]).start()


def main():
    inp = input('Please enter exact time (e.g. 23:12) or a time duration in minutes and seconds (e.g. 2m34s): ')
    now = dt.now()
    t = parse_input(inp)
    if not t:
        print('Invalid input.')
        exit(0)

    if osname != 'nt':
        print('Sounds are not supported in this system. Sorry :(')

    mode, period = t
    if mode == 'a':
        target_date = dt.combine(now, time(period.hour, period.minute))
        if target_date < now:
            target_date = target_date + timedelta(days=1)

        print('The alarm will go off on {0}'.format(target_date))
        Timer((target_date - now).total_seconds(), alarm).start()
    else:
        target_date = now + timedelta(minutes=period.minute,seconds=period.second)
        print('The timer will run for {0}m{1}s and will end on {2}'.format(period.minute, period.second, target_date))
        thread = Timer(1, timer_tick, [target_date])
        thread.start()


if __name__ == '__main__':
    main()