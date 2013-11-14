from Algorithms.compression.lzwcompressor import LZWCompressor


def main():
    print(LZWCompressor().compress('banana_bandana'))
    LZWCompressor().compress(open('input.txt').read(), file='keke.bin')


if __name__ == '__main__':
    main()