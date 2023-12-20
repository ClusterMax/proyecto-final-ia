"""

Proyecto final - Introducción a la IA

John Jader Marulanda Valero - 2060034
Joann Esteban Bedoya Lopez - 2059906
Carlos Eduardo Guerrero Jaramillo - 2060216

Universidad del Valle Sede Tuluá
Ingeniería de Sistemas - 3743

"""

import numpy as np

# ----------------- Movements ------------------------


# evalua si la posicion no se sale de la matriz
def overflowCheck(matrix, array):
    maxX = len(matrix[0])
    minX = 0
    maxY = len(matrix)
    minY = 0
    if array[1] >= minX and array[1] < maxX and array[0] >= minY and array[0] < maxY:
        return True
    else:
        return False


# evalua si la posicion de destino esta libre
def positionCheck(matrix, coordTo):
    if matrix[coordTo[0]][coordTo[1]] == 0:
        return True
    else:
        print("Regla: La posicion final debe estar vacia")
        return False


# mueve la pieza de posicion
def movePiece(matrix, coordFrom, coordTo):
    matrix[coordTo[0]][coordTo[1]] = matrix[coordFrom[0]][coordFrom[1]]
    matrix[coordFrom[0]][coordFrom[1]] = 0
    return matrix

# calcula el numero de movimientos segunda jugada, se pasa la matriz una vez hecha el moviento
def getSecondMovement(matrix, position):
    contador = 0
    for fila in matrix:
        if fila[position] != 0:
            contador += 1
    return contador

def checkSecondTurn(subTurn, movement):
    if subTurn == 2 and movement == 0:
        return True
    else:
        return False


# ----------------- GameRules ------------------------


# evalua si la jugada esta dentro de los movimientos posibles en este turno
def ruleMaxMovements(coordFrom, coordTo, maxMovements):
    if (
        abs(coordFrom[1] - coordTo[1])
    ) == maxMovements:
        return True
    else:
        print("La pieza debe moverse exactamente: " + str(maxMovements) + " casillas")
        return False


# evalua si el jugador se mueve a otra columna y no se devuelva
def ruleNoComeBack(coordFrom, coordTo, turn):
    if turn == 1 and coordFrom[1] < coordTo[1]:
        return True
    if turn == 2 and coordFrom[1] > coordTo[1]:
        return True
    else:
        print("Regla: Se tiene que mover a otra columna y no se puede devolver.")
        return False


# evalua si el jugador del turno actual mueve su pieza y no la del contrincante
# def ruleOnlyMoveYourPeace(piece, turn):
#     if piece == turn:
#         return True
#     else:
#         print("Regla: No puedes mover la pieza de tu contrincante")
#         return False


def ruleOnlyMoveYourPeace(piece, turn):
    if piece == turn:
        return True
    elif piece == 0:  # Agrega esta condición para celdas vacías
        print("Movimiento no válido: No estas seleccionando niguna ficha.")
        return False
    else:
        print("Regla: no puedes mover la pieza de tu contrincante.")
        return False


def inputPlayer(coordFrom, coordTo):
    return 0


def inputOpponent():
    return 0


# ----------------- Gameplay ------------------------


# funcion para mover una pieza
def move(matrix, coordFrom, coordTo):
    matrix = movePiece(matrix, coordFrom, coordTo)
    return matrix
    
def turns(matrix, coordFrom, coordTo, turn, subTurn, movements):


    #Turno del jugador 1
    if (
        (turn == 1 or turn == 2)
        and overflowCheck(matrix, coordFrom)
        and overflowCheck(matrix, coordTo)
        and positionCheck(matrix, coordTo)
        and ruleNoComeBack(coordFrom, coordTo, turn) 
        and ruleMaxMovements(coordFrom, coordTo, movements)
        ):

        #Se ve en que jugada esta
        if subTurn == 1 or subTurn == 3: #Primera jugada. la tercera jugada es si cae en el movimiento especial
            movements = getSecondMovement(matrix, coordTo[1])
            subTurn += 1
        else:
            if checkSecondTurn(subTurn, movements): #Movimiento especial, vuelve a jugar, solo si turno subturn es 2
                subTurn = 3
                movements = 1 #El proximo movimiento se repetira a 1
            elif subTurn == 2 or subTurn == 4: #Se termina el turno del jugador
                subTurn = 1 #Resetea subturn
                movements = 1 #movimientos a 1 para el proximo jugador

                if turn == 1: #Sigueitne jugador
                    turn = 2
                else:
                    turn = 1
                print("turno jugador "+ str(turn))

        return (move(matrix, coordFrom, coordTo)), movements, subTurn, turn
    
    else: #Turno de la ia
        return False, movements, subTurn, turn
