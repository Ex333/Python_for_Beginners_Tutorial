#display single string
print('FR')

#display multiple strings
print('FR', 'ES', 'USA', 'IT', 'PL')

#use variables
country_france = 'FR'
country_spain = 'ES'
country_usa = 'USA'
country_italy = 'IT'
country_poland = 'PL'

print(country_france, country_spain, country_usa, country_italy, country_poland, sep='\n')

#do calculations
pi = 3.14
r = 5
print('Area of circle with radius', r, 'is', pi * r * r)
area = pi * r * r
print('Area of circle with radius', r, 'is', area)

# separators
print(1, 2 , 3, 4, 5, sep='-')
print('backslash', 'is', 'used', 'to', 'escape', 'characters', sep='\\')
print('newline', 'is', 'used', 'to', 'start', 'a', 'new', 'line', sep='\n')

print(x, y, z, sep='-')  # This line will raise an error because x, y, z are not defined
