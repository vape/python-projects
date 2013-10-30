from requests import get
from math import sqrt, radians, sin, cos, asin


def geocode(address):
    payload = {'sensor': 'false', 'address': address}
    try:
        r = get('http://maps.googleapis.com/maps/api/geocode/json', params=payload)
        res = r.json()['results'][0]
        return res['formatted_address'], res['geometry']['location']['lat'], res['geometry']['location']['lng']
    except:
        return None


def get_distance(p1, p2):
    radius = 6371 #km
    lat1, lon1, lat2, lon2 = map(radians, (list(p1) + list(p2)))
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + (cos(lat1) * cos(lat2) * sin(dlon/2)**2)
    c = 2 * asin(sqrt(a))
    return radius * c


def main():
    address1 = input('Please enter address of first location: ')
    address2 = input('Please enter address of second location: ')
    g1 = geocode(address1)
    g2 = geocode(address2)
    print('"{0}" will be treated as "{1}"'.format(address1, g1[0]) if g1 else 'Sorry. I couldn\'t find anything for "{0}"'.format(address1))
    print('"{0}" will be treated as "{1}"'.format(address2, g2[0]) if g2 else 'Sorry. I couldn\'t find anything for "{0}"'.format(address2))
    if not g1 or not g2:
        return

    print('The distance between "{0}" and "{1}" is {2:.2f}km'.format(g1[0], g2[0], get_distance((g1[1], g1[2]), (g2[1], g2[2]))))


if __name__ == '__main__':
    main()