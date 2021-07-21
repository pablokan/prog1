# create a list of odd numbers from 1 to 20
# print the list

odd_numbers = list(range(1,21,2))
print(odd_numbers)

def askPrimaryColors():
    '''ask the user to enter primary colors, one per line'''
    primary_colors = []
    while True:
        color = input("Enter a primary color: ")
        if color == "":
            break
        primary_colors.append(color)
    return primary_colors
    