# Rakesh Shrestha
# July 26, 2026
# CSD325-T301 Advanced Python - Module 7.2 Assignment: Test Cases
# Purpose: Defines city_country(), which builds a formatted "City, Country"
# string, with optional population and language details.

def city_country(city, country, population='', language=''):
    """Return a formatted 'City, Country' string.

    Population and language are optional. If both are supplied the
    string includes both; if only population is supplied it is
    included on its own; otherwise just 'City, Country' is returned.
    """
    if population and language:
        return f"{city}, {country} - population {population}, {language}"
    elif population:
        return f"{city}, {country} - population {population}"
    else:
        return f"{city}, {country}"


if __name__ == '__main__':
    print(city_country('Santiago', 'Chile'))
    print(city_country('Santiago', 'Chile', 5000000))
    print(city_country('Santiago', 'Chile', 5000000, 'Spanish'))
