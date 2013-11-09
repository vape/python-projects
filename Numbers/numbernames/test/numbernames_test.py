from unittest import TestCase
from Numbers.numbernames.numbernames import NumberNameConverter


class NumberNamesTests(TestCase):
    def setUp(self):
        self.conv = NumberNameConverter()

    def test_non_integer_conversion(self):
        with self.assertRaises(ValueError):
            self.conv.convert(1.6)

    def test_single_number(self):
        self.assertEqual(self.conv.convert(0), 'zero')
        self.assertEqual(self.conv.convert(1), 'one')

    def test_tween_numbers(self):
        self.assertEqual(self.conv.convert(11), 'eleven')
        self.assertEqual(self.conv.convert(16), 'sixteen')
        self.assertEqual(self.conv.convert(10), 'ten')

    def test_two_digit_whole_numbers(self):
        self.assertEqual(self.conv.convert(20), 'twenty')
        self.assertEqual(self.conv.convert(90), 'ninety')

    def test_two_digit_numbers(self):
        self.assertEqual(self.conv.convert(23), 'twenty three')
        self.assertEqual(self.conv.convert(42), 'fourty two')
        self.assertEqual(self.conv.convert(99), 'ninety nine')

    def test_three_digit_numbers(self):
        self.assertEqual(self.conv.convert(100), 'one hundred')
        self.assertEqual(self.conv.convert(300), 'three hundred')
        self.assertEqual(self.conv.convert(420), 'four hundred and twenty')
        self.assertEqual(self.conv.convert(856), 'eight hundred and fifty six')

    def test_four_digit_numbers(self):
        self.assertEqual(self.conv.convert(4100), 'four thousand one hundred')
        self.assertEqual(self.conv.convert(6150), 'six thousand one hundred and fifty')
        self.assertEqual(self.conv.convert(8491), 'eight thousand four hundred and ninety one')

    def test_negative_numbers(self):
        self.assertEqual(self.conv.convert(-1), 'negative one')
        self.assertEqual(self.conv.convert(-300), 'negative three hundred')
        self.assertEqual(self.conv.convert(-6150), 'negative six thousand one hundred and fifty')

    def test_large_numbers(self):
        self.assertEqual(self.conv.convert(67000001), 'sixty seven million and one')

    def test_too_large_number(self):
        self.assertEqual(self.conv.convert(1000000000000000), 'one quadrillion', 'Should convert up to quadrillion')
        with self.assertRaises(ValueError):
            self.conv.convert(1000000000000000000)



