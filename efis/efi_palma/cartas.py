def mostrar_cartas(cartas, oculta):
    s = ""
    for carta in cartas:
        s = s + "\t┌─────────┐"
    if oculta:
        s += "\t┌──────────┐"
    print(s)
    s = ""
    for carta in cartas:
        if carta.valores == "10":
            s = s + "\t| {}      |".format(carta.valores)
        else:
            s = s + "\t| {}       |".format(carta.valores)  
    if oculta:
        s += "\t|          |"    
    print(s) 
    s = ""
    for carta in cartas:
        s = s + "\t|         |"
    if oculta:
        s += "\t|          |"
    print(s)
    
    s = ""
    for carta in cartas:
        s = s + "\t|    {}    |".format(carta.palo)
    if oculta:
        s += "\t|    ¿?    |"
    print(s)     
    
    s = ""
    for carta in cartas:
        s = s + "\t|         |"
    if oculta:
        s += "\t|          |"
    print(s)       
 
    s = ""
    for carta in cartas:
        if carta.valores == "10":
            s = s + "\t|      {} |".format(carta.valores)
        else:
            s = s + "\t|       {} |".format(carta.valores)
    if oculta:
        s += "\t|          |"        
    print(s)   

    s = ""
    for carta in cartas:
        s = s + "\t└─────────┘"
    if oculta:
        s += "\t└──────────┘"
    print(s)        
 
    print()