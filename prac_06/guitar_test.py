import datetime
from guitar import Guitar

current_year = datetime.datetime.now().year

# Test Case 1: A vintage guitar that is from 1960
vintage_guitar = Guitar("1960 Stratocaster", 1960, 5000.00)
expected_age_v = current_year - 1960

print(f"{vintage_guitar.name} get_age() - Expected {expected_age_v}. Got {vintage_guitar.get_age()}")
print(f"{vintage_guitar.name} is_vintage() - Expected True. Got {vintage_guitar.is_vintage()}")

print("-" * 20) # Just a divider to make the output clean

# Test Case 2: A modern guitar that is from 2015
modern_guitar = Guitar("2015 Les Paul", 2015, 2500.00)
expected_age_m = current_year - 2015

print(f"{modern_guitar.name} get_age() - Expected {expected_age_m}. Got {modern_guitar.get_age()}")
print(f"{modern_guitar.name} is_vintage() - Expected False. Got {modern_guitar.is_vintage()}")