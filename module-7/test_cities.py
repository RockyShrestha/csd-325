# Rakesh Shrestha
# July 26, 2026
# CSD325-T301 Advanced Python - Module 7.2 Assignment: Test Cases
# Purpose: Unit tests for the city_country() function in city_functions.py.

import unittest
from city_functions import city_country


class CityCountryTestCase(unittest.TestCase):
    """Tests for the city_country() function."""

    def test_city_country(self):
        """Do two names like Santiago and Chile work?"""
        formatted_city_country = city_country('Santiago', 'Chile')
        self.assertEqual(formatted_city_country, 'Santiago, Chile')


if __name__ == '__main__':
    unittest.main()
