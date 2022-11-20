import unittest
from DIY_10_1_city_country import ciyt_country

class CityCountryTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted_name = ciyt_country('werl', 'deutschland')
        self.assertEqual(formatted_name, 'Werl Deutschland')

    def test_city_country_population(self):
        formatted_name = ciyt_country('werl', 'deutschland', '30002')
        self.assertEqual(formatted_name, 'Werl Deutschland population-30002')

if __name__ == '__main__':
    unittest.main()


