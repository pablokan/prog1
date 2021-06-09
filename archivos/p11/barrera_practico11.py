def load_txt():
  f = open("pelis.json", "r")
  f2 = open("pelis.txt", "w") 
  f2.write("Nombre, Actor, Rating, Recaudacion " + "\n")
  aux = ""
  i = 1
  while i <= 3:
    if i == 1:
      f.seek(0)
    elif i == 2:
      f.seek(1500)
    elif i == 3:
      f.seek(2974)
    text = f.read()
    position_title = text.find("Title") + 9
    position_finish_title = text.find(",", position_title) - 1
    title = text[position_title:position_finish_title]
    position_actor = text.find("Actors") + 10
    position_finish_actor = text.find(",", position_actor - 1)
    actor = text[position_actor:position_finish_actor]
    position_rating = text.find("Rotten Tomatoes") + 44
    position_finish_rating = text.find('%"', position_rating)
    rating = text[position_rating:position_finish_rating]
    position_recaudation = text.find("BoxOffice") + 14
    position_finish_recaudation = text.find('",', position_recaudation)
    recaudation = text[position_recaudation:position_finish_recaudation]
    for j in range(len(recaudation)):
      if recaudation[j] != ",":
        aux = aux + recaudation[j] 
    recaudation = aux
    aux = ""
    f2.write(title + "," + " " + actor + "," + " " + rating + "," + " " + recaudation + "\n")
    i = i + 1
  f2.close()
  f.close()

def rating_recaudations():
  f = open("pelis.txt", "r")
  all_lines = f.readlines()
  rating_list = []
  recaudation_list = []
  for i in range(1,len(all_lines)):
    line = all_lines[i]
    first_point = line.find(",")
    second_point = line.find(",", first_point+2)
    third_point = line.find(",", second_point+2)
    fourth_point = line.find(",", third_point+2) 
    rating_list.append(int(line[second_point+1:third_point]))
    recaudation_list.append(int(line[third_point+1:fourth_point]))
  all_recaudations = 0
  average_rating = 0
  for i in range(len(rating_list)):
    average_rating = average_rating + rating_list[i]
    all_recaudations = all_recaudations + recaudation_list[i]
  average_rating = average_rating//len(rating_list)
  print("Recaudaciones de todas las peliculas:", all_recaudations,"\nPromedio de rating:", average_rating)

def menu():
  op = ""
  while op != "3":
    print("\nMenú de Opciones")
    print("1- Cargar archivo pelis.txt")
    print("2- Mostrar rating y recaudaciones de peliculas")
    print("3- Fin")
    op = input("Opción: ")
    if op == "1":
      load_txt()
      print("Cargado con exito!")
    elif op == "2":
      rating_recaudations()
  print("Bye")

menu()