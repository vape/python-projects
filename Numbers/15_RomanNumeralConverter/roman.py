from re import match, IGNORECASE

roman_chars = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def is_valid_roman_format(roman):
    return match('^[{0}]+$'.format(''.join(roman_chars.keys())), roman, IGNORECASE) is not None


def convert_to_int(roman):
    last_char = ''
    total_value, current_value = 0, 0
    for c in list(roman.upper()):
        if not last_char:
            current_value = roman_chars[c]
        elif c == last_char:
            current_value += roman_chars[c]
        elif roman_chars[c] < roman_chars[last_char]:
            total_value += current_value
            current_value = roman_chars[c]
        elif roman_chars[c] > roman_chars[last_char]:
            current_value = roman_chars[c] - current_value
        last_char = c

    return total_value + current_value


def main():
    roman = input('Enter roman numeral to convert: ')
    if not is_valid_roman_format(roman):
        print('The roman numeral you entered is invalid. Roman numerals can contain {0}'.format(', '.join(roman_chars.keys())))
    else:
        print('{0} equals {1}.'.format(roman, convert_to_int(roman)))


if __name__ == '__main__':
    main()