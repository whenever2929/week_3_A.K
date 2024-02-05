
# string formatting

planets ={'mercury': 57.91,
          'Venus': 108.2,
          'Earth': 149.597870,
          'Mars': 227.94
}

for i, key in enumerate (planets.keys(),1):
    print("{:2d} {:<10s} {:06.2f} Gm".format(i,  key, planets [key]))

# other formating
print('cake'.capitalize())



from operator import length_hint
size=length_hint(planets)
print(size)