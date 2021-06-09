def menu():
    op = ""
    while op != "3":
        print("\nMenú de Opciones")
        print("1- Carga")
        print("2- Resultado")
        print("3- Fin")
        op = input("Opción: ")

        if op == "1":
            print("Carga")
        elif op == "2":
            print("Resultado")
    print("Bye")

menu()
