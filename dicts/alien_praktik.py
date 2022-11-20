
alien_0 = {'x_position': 0, 'y_positson': 25, 'speed': 'medium'}
print(f"Original posotson: {alien_0['x_position']}")
# alien_0['speed'] = 'fast'
# Зсунути прибульця правороуч.
# Визначити як далеко зсунули прибульця
# зважаючи на його поточну швидкість.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Це швидкий прибулець.
    x_increment = 3

# Нове розташування -- це старе розташування + зміщеня
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New positions: {alien_0['x_position']}")
print(alien_0)
del alien_0['speed']
print(alien_0)

speed_value = alien_0.get('speed', 'No speed value assigneted.')
print(speed_value)

