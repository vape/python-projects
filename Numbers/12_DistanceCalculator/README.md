### Distance Between Two Cities

Calculates the distance between two cities and allows the user to specify a unit
of distance. This program may require nding coordinates of the cities like lat-
itude and longitude.

Note: I implemented this as a "Distance Between Two Addresses" utility. I'm using the
[Google Geocoding API](https://developers.google.com/maps/documentation/geocoding/)
to geocode the addresses specified by the user. Then I calculate the distance
between these two points using the [Haversine Formula](http://en.wikipedia.org/wiki/Haversine_formula).