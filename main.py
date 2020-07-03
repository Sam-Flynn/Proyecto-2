#Tres en raya 
def presentar_1():
    print()
    print("Tres en raya")
    print()
    print("Escoja una ficha jugador1 (X o O):")
    ficha1=""
    while ficha1!="O" and ficha1!="X":
        ficha1=input(" ").upper()
    if ficha1=="O":
        jugador1="O"
        jugador2="X"
    elif ficha1=="X":
        jugador1="X"
        jugador2="O"
    return jugador1, jugador2

def mostrar_tablero(tablero):
    print()
    print()
    print()
    print("    1     |2     |3")
    print("      {}   |{}     | {}".format(tablero[0],tablero[1],tablero[2]))
    print("          |      |")
    print("-------------------------")
    print("    4     |5     |6")
    print("      {}   |{}     | {}".format(tablero[3],tablero[4],tablero[5]))
    print("          |      |")
    print("-------------------------")
    print("    7     |8     |9")
    print("      {}   |{}     | {}".format(tablero[6],tablero[7],tablero[8]))
    print("          |      |")
    print()
def continuar_jugando():
#da true si se quiere sueguir jugando, false si no quieren
    print()
    respuesta=input("Si quieres jugar otra vez escribe (si)").lower()
    if respuesta=="si":
        return True
    else:
        return False
def tablero_completo(tablero):
    for i in tablero:
        if i==" ":
            return False
    else:
          return True
def casilla_vacia(tablero,casilla):
  if tablero[casilla]==" ":
    return True
  else:
    return False
def movimiento_jugador1(tablero):
  posiciones=["1","2","3","4","5","6","7","8","9"]
  posicion=None
  while True:
      if posicion not in posiciones:
            posicion=input("Escoge entre 1-9: ")
      else:
            posicion=int(posicion)
            if not casilla_vacia(tablero,posicion-1):
                print("Ocupada")
            else:
                return posicion-1
def ganador1(tablero,jugador):
  if  tablero[0]==tablero[1]==tablero[2]==jugador1 or \
      tablero[3]==tablero[4]==tablero[5]==jugador1 or \
      tablero[6]==tablero[7]==tablero[8]==jugador1 or \
      tablero[0]==tablero[3]==tablero[6]==jugador1 or \
      tablero[1]==tablero[4]==tablero[7]==jugador1 or \
      tablero[2]==tablero[5]==tablero[8]==jugador1 or \
      tablero[0]==tablero[4]==tablero[8]==jugador1 or \
      tablero[2]==tablero[4]==tablero[6]==jugador1 :
      return True
  else:
    return False
def ganador2(tablero,jugador):
  if  tablero[0]==tablero[1]==tablero[2]==jugador2 or \
      tablero[3]==tablero[4]==tablero[5]==jugador2 or \
      tablero[6]==tablero[7]==tablero[8]==jugador2 or \
      tablero[0]==tablero[3]==tablero[6]==jugador2 or \
      tablero[1]==tablero[4]==tablero[7]==jugador2 or \
      tablero[2]==tablero[5]==tablero[8]==jugador2 or \
      tablero[0]==tablero[4]==tablero[8]==jugador2 or \
      tablero[2]==tablero[4]==tablero[6]==jugador2 :
      return True
  else:
      return False
def movimiento_jugador2(tablero):
  posiciones=["1","2","3","4","5","6","7","8","9"]
  posicion=None
  while True:
      if posicion not in posiciones:
            posicion=input("Escoge entre 1-9: ")
      else:
            posicion=int(posicion)
            if not casilla_vacia(tablero,posicion-1):
                print("Ocupada")
            else:
                return posicion-1
juego=True
while juego:
    tablero=[" "]*9
    jugador1,jugador2=presentar_1()
    mostrar_tablero(tablero)
    if jugador1=="X":
        turno= "Jugador1"
    if jugador1=="O":
        turno="Jugador1"
    partida= True

    while partida:
  
        if turno=="Jugador1":
            casilla=movimiento_jugador1(tablero)
            tablero[casilla]=jugador1
            turno="Jugador2"
            mostrar_tablero(tablero)
            print("Turno Jugador2")
            if ganador1(tablero,jugador1):
              print("Ganador: jugador1")
              partida=False
            elif  tablero_completo(tablero)==True:
                print("Empate")
                break
        elif turno=="Jugador2":
            casilla=movimiento_jugador2(tablero)
            tablero[casilla]=jugador2
            turno="Jugador1"
            mostrar_tablero(tablero)
            print("Turno Jugador1")
            if ganador2(tablero,jugador2):
              print("Ganador: jugador2")
              partida=False
            elif  tablero_completo(tablero)==True:
                print("Empate")
                break
