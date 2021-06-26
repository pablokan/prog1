nombres = ['Torres, Ana', 'Hudson, Kate', 'Quesada, Benicio']
print(*nombres)

my_list = [1, 2, 3, 4, 5, 6]
a, *b, c = my_list
print(a, b, c)

def foo(a, b, *args):
    print(a+b+sum(args))
foo(1,2,3,4)

def bar(*numbers):
    print(numbers)
bar(1,2,3)
