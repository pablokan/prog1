# create a list of names
names = ['Khan', 'Omar', 'Sara', 'Ali', 'Mohammed', 'Sofia', 'Mateo']
# create a list of ages
ages = [60, 50, 55, 70, 25, 20, 40]
# create a list of heights
heights = [1.75, 1.90, 1.55, 1.80, 1.65, 1.71, 1.88]
# create a list of sexs
sexs = ['M', 'M', 'F', 'M', 'M', 'F', 'M']


# convert above lists to list of dicts
# create a list of dicts
women = []
men = []
for x in range(7):
    if sexs[x] == 'F':
        women.append({'name': names[x], 'age': ages[x], 'height': heights[x]})
    else:
        men.append({'name': names[x], 'age': ages[x], 'height': heights[x]})

print(women)
print()
print(men)






