print(r'The LaTeX command for a reference is \ref.')

print('The current time is {hour}:{minute}:{second}.'.format(hour=18, minute=4, second=54))

print('The current time is {hour}:{minute:02}:{second:02}.'.format(hour=18, minute=4, second=54))

hour = 18
minute = 4
second = 54
print('The current time is {hour}:{minute:02}:{second:02}.'.format(hour=hour, minute=minute, second=second))
print(f'The current time is {hour}:{minute:02}:{second:02}.')
