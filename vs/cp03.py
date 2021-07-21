# create a list of colors
colors = ["red", "yellow", "green", "blue", "indigo", "violet"]
# print the list one per line
for color in colors:
    print(color)

# ask the user for a color to remove
color = input("Which color would you like to remove? ")
# check if the color is in the list
if color in colors:
    # remove the color from the list
    colors.remove(color)
    # print the list
    for color in colors:
        print(color)





