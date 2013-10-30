class UnsupportedUnitException(BaseException):
    def __init__(self, unit):
        self._unit = unit

    @property
    def unit(self):
        return self._unit

class DifferentUnitsException(BaseException):
    def __init__(self, cat1, cat2):
        self._cat1 = cat1
        self._cat2 = cat2

    @property
    def cat1(self):
        return self._cat1

    @property
    def cat2(self):
        return self._cat2

categories = [
    {
        'name': 'mass',
        'base_unit': 'kg',
        'units': [
            {
                'name': 'kg',
                'val_in_base': 1
            },
            {
                'name': 'g',
                'val_in_base': 0.001
            },
            {
                'name': 'mg',
                'val_in_base': 0.000001
            }
        ]
    },
    {
        'name': 'length',
        'base_unit': 'm',
        'units': [
            {
                'name': 'm',
                'val_in_base': 1
            },
            {
                'name': 'cm',
                'val_in_base': 0.01
            },
            {
                'name': 'mm',
                'val_in_base': 0.001
            },
            {
                'name': 'inch',
                'val_in_base': 0.0254
            },
            {
                'name': 'km',
                'val_in_base': 1000
            }
        ]
    }
]


def find_category(unit):
    for c in categories:
        if [u for u in c['units'] if u['name'] == unit]:
            return c
    raise UnsupportedUnitException(unit)


def get_unit(category, unit):
    return [u for u in category['units'] if u['name'] == unit][0]


def convert_value(value, src_unit_name, target_unit_name):
    src_cat, target_cat = find_category(src_unit_name), find_category(target_unit_name)
    if src_cat != target_cat:
        raise DifferentUnitsException(src_cat['name'], target_cat['name'])

    src_unit = get_unit(src_cat, src_unit_name)
    target_unit = get_unit(src_cat, target_unit_name)

    return (value * src_unit['val_in_base']) / target_unit['val_in_base']


def main():
    print('Hello! With this calculator you can convert units of {0}.'.format(', '.join([c['name'] for c in categories])))
    src_val, src_unit, target_unit = input('Please enter source value, source unit and unit to convert to [e.g. 100 m km]: ').split(' ')
    src_val = float(src_val)

    try:
        converted = convert_value(src_val, src_unit, target_unit)
        print('{0} {1} = {2:.2f} {3}'.format(src_val, src_unit, converted, target_unit))
    except UnsupportedUnitException as uue:
        print('Sorry. I don\'t know what {0} is.'.format(uue.unit))
    except DifferentUnitsException as due:
        print('Sorry. These two units belong to different categories ({0} and {1}) and cannot be converted.'.format(due.cat1, due.cat2))

if __name__ == '__main__':
    main()