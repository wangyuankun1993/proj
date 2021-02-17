import unittest
from city_functions import get_formatted_city

class CitiesTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_city = get_formatted_city('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')

    def test_city_country_population(self):
        formatted_city = get_formatted_city('santiago', 'chile', '5000000')
        self.assertEqual(formatted_city, 'Santiago, Chile - Population 5000000')
unittest.main()