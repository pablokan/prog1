a = open('pr10/deudores.txt', 'r')
todo = a.read()
primerEnter = todo.find("\n")
todo = todo[primerEnter+1:]
print(todo)
