# create a list of colors
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'white', 'black', 'cyan', 'magenta']
# ask the user to remove a color
remove = input('Which color would you like to remove? ')
# remove the color from the list
colors.remove(remove)
# print the list
print(colors)

# pedir números y sumarlos
nums = []
while True:
    num = input('Enter a number: ')
    if num == 'done':
        break
    else:
        nums.append(float(num))
print(sum(nums))


