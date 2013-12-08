from string import capwords


def chunks(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]


def chemicalize(txt, s):
    elements = [l.split(' ')[0].lower() for l in open('elements.txt').read().splitlines()]
    words = [chunks(p, s) for p in txt.lower().split(' ')]
    return ' '.join([''.join(['*{0}*'.format(capwords(c)) if c in elements else c for c in w]) for w in words])


def main():
    text = 'gozde korkmaz'
    out = chemicalize(text, 2)
    if '*' not in out:
        out = chemicalize(text, 1)

    print(out)


if __name__ == '__main__':
    main()