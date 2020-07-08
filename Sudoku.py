# Sudoku

# Programa para resolver un sudoku 

################################################################################
####################################Tablero#####################################
################################################################################

tablero=[
    [0, 0, 3, 0, 5, 8, 0, 0, 0],
    [0, 0, 0, 6, 0, 0, 4, 3, 0],
    [7, 6, 0, 3, 2, 4, 5, 0 ,0],
    [0, 0, 0, 0, 8, 6, 0, 0, 7],
    [0, 0, 0, 0, 0, 3, 9, 6, 0],
    [3, 0, 0, 7, 0, 0, 2, 0, 0],
    [6, 0, 8, 5, 0, 7, 0, 2, 0],
    [0, 0, 0, 0, 0, 2, 8, 7, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0]
    ]

def imprimir_tablero(tab):
    
    #Imprime lineas horizontales
    for i in range(len(tab)) :
        if i % 3 == 0 :
            print("- - - - - - - - - - - - - - -")

        #Imprime lineas verticales            
        for j in range(len(tab[0])) :
            if j % 3 == 0 :
                print(" | ", end="")
                
        #Imprime los números y la línea del final           
            if j == 8 :
                print(str(tab[i][j]) + " | ")
            else : 
                print(str(tab[i][j]) + " ", end="") 
    print("- - - - - - - - - - - - - - -")
            
imprimir_tablero(tablero)

################################################################################
################################################################################
################################################################################


################################################################################
####################################Checamos si hay cero########################
################################################################################

def checar_cero(tab):
    
    #Recorremos cada elemento del tamblero para ver si encontramos un cero (cero represennta casillas en blanco)
    for i in range(len(tab)) :
        for j in range(len(tab[0])):
            if tab[i][j] == 0 :
                return ( i, j)     #Lo llamaremos posicion

################################################################################
################################################################################
################################################################################


################################################################################
####################################¿Se puede poner x numero en (i, j)?#########
################################################################################

def checar(tab, numero, posicion):
    
    #Revisamos el renglón
    for i in range(len(tab[0])):
        if tablero[posicion[0]][i] == numero and posicion[1] != i:
            return False
        
    #Revisamos las columnas
    for i in range(len(tab[0])):
        if tablero[i][posicion[1]] == numero and posicion[0] != i:
            return False
        
    #Checamos la cuadricula
        #Checamos en qué caja estamos utilizando la poderosa division entera
    caja_x = posicion[1] // 3
    caja_y = posicion[0] // 3
    
    for i in range (caja_y * 3, caja_y * 3 + 3) :
            for j in range (caja_x * 3, caja_x * 3 + 3) : 
                if tab[i][j] == numero and (i, j) != posicion:
                    return False

    return True

################################################################################
################################################################################
################################################################################


################################################################################
####################################Resolver####################################
################################################################################

def resolver(tab):
    
    cero = checar_cero(tab)
    if not cero:
        return True
    else: 
        renglon, columna = cero
        
    for i in range (1,10):
        if checar(tab, i, (renglon ,columna)) :
            tab[renglon][columna] = i
            
            if resolver(tab):
                return True
            
        tab[renglon][columna] = 0
        
    return False

################################################################################
################################################################################
################################################################################

imprimir_tablero(tablero)
resolver(tablero)
print("++++++++++++++++++++++++++++++++++++++++++++++++++")
imprimir_tablero(tablero)
