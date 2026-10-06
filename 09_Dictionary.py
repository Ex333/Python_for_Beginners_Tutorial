alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0["points"])

print(alien_0.get("health", 'No exist!'))
print(alien_0.get("color", 'No exist!'))

new_points = alien_0['points']
print(f"Killing this allien you've got {alien_0['points']} points! Nice work!")