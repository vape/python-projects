from collections import defaultdict

index = defaultdict(set)


def _get_data():
    with open('data.txt') as f:
        return f.read().splitlines()


def _build_index(lines):
    for li, l in enumerate(lines):
        for wi, w in enumerate(l.split(' ')):
            index[w].add(li)


def _search(q):
    res = set()
    for i in [index.get(w, None) for w in q.split(' ') if index.get(w, [])]:
        res = res.intersection(i) if res else i
    return res


def _print_results(q, results):
    if not results:
        print('No results for search term "{0}".'.format(q))
    else:
        print('{0} result{3} for search term "{1}" on line{3} {2}.'.format(len(results), q, ', '.join(map(str, list(results))), 's' if len(results) > 1 else ''))


def main():
    lines = _get_data()
    _build_index(lines)
    print(index)

    while True:
        query = input('Enter search query or "-q" to quit: ')
        if query.lower() == '-q':
            break
        results = _search(query)
        _print_results(query, results)


if __name__ == '__main__':
    main()