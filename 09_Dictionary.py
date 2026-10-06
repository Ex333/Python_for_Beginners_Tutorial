alien_0 = {
    'color': 'green',
    'points': 5
}

print(alien_0['color'])
print(alien_0['points'])

print(alien_0.get('health', 'No exist!'))
print(alien_0.get('color', 'No exist!'))

new_points = alien_0['points']
print(f"Killing this alien you've got {new_points} points! Nice work!")


# Change color
print(f"Alien has {alien_0['color']} color!")

alien_0['color'] = 'yellow'

print(f"Alien has right now {alien_0['color']} color!")


# Add new information
X = {
    'x_position': 0,
    'y_position': 25,
    'speed': 'medium'
}

alien_0.update(X)


print(f"Starting value x-position is {alien_0['x_position']}")


# Move alien
while True:

    if alien_0['speed'] == 'slow':
        x_increment = 1

    elif alien_0['speed'] == 'medium':
        x_increment = 2

    else:
        # It has to be a really fast alien :D
        x_increment = 3

    alien_0['x_position'] = alien_0['x_position'] + x_increment

    print(f"New value of X-position: {alien_0['x_position']}")

    alien_0['speed'] = 'fast'

    pressed_key = input("Press q to quit: ")

    if pressed_key == 'q':
        break


# Delete value
del alien_0['speed']

print(alien_0)