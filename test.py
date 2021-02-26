from random import random
from kivy.graphics import Color

color = (random(), random(), random())

print(color)
print(*color)
c = Color(random(), 1, 1)
print(c)
