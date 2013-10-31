import socket


def main():
    ip, port_range = input('Enter IP Address and port range to scan [e.g. 127.0.0.1 2000-2100]: ').split(' ')
    try:
        socket.inet_aton(ip)
    except OSError:
        print('Invalid IP Address')
        exit(0)

    try:
        rng = port_range.split('-')
        range_start = int(rng[0])
        range_end = int(rng[1]) if len(rng) > 1 else range_start + 1
    except ValueError and IndexError:
        print('Invalid port range')
        exit(0)

    open_sockets = []
    closed_sockets = []
    for p in range(range_start, range_end):
        print('Checking port {0}...'.format(p))
        try:
            with socket.create_connection((ip, p), timeout=3) as conn:
                print('Port {0} is open.'.format(p))
                open_sockets.append(p)
        except:
            print('Port {0} is closed.'.format(p))
            closed_sockets.append(p)

    print('')
    print('{0} open sockets: {1}'.format(len(open_sockets), ', '.join(map(str, open_sockets))))
    print('{0} closed sockets: {1}'.format(len(closed_sockets), ', '.join(map(str, closed_sockets))))


if __name__ == '__main__':
    main()
