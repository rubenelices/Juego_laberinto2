"""
Aqui creo la clase laberinto a partir de la cual van a partir
 todas las funiones,además sirve para mostrar el código de manera
mas limpia y estructurada.
"""
class Laberinto:

    """
    Creo la función __Init__ a partir de la cual voy a crear la matriz
    que da forma al laberinto, poniendo el numero de filas, y el número de
    columnas.
    """
    def __init__(self, muro):
        filas = 5
        columnas = 5
        self.laberinto = [[' ' for _ in range(columnas)] for _ in range(filas)]
        self.posicion_actual = (filas-5, columnas-5)
        self.destino = (filas-1, columnas-1)
        self.pasos_seguidos = []
        self.inicializar_laberinto(muro)

    """
    En esta función lo que hago es definir el inicio y el final del laberinto
    poniendo El simbolo "¤" Que será el personaje que se irá moviendo por el 
    laberinto y la letra "S" que definirá la salida del mismo
    """
    def inicializar_laberinto(self, muro):
        for coordenada in muro:
            fila, columna = coordenada
            self.laberinto[fila][columna] = 'X'
        self.laberinto[self.posicion_actual[0]][self.posicion_actual[1]] = '¤'
        self.laberinto[self.destino[0]][self.destino[1]] = 'S'


    """
    Esta función imprime el laberinto con un doble espacio entre cada fila para
    que quede mejor visualemente.
    """
    def mostrar_laberinto(self):
        for fila in self.laberinto:
            print('  '.join(fila))
        print()

    """
    esta función sirve para conseguir que el símbolo "¤" sse mueva a lo largo
    del laberinto usando las teclas "w,a,s,d" para moverse, negandote el 
    pasar por las zonas que tienen X(el muro) hasta llegar a la salida.
    """
    def moverse(self, direccion):
        fila, columna = self.posicion_actual


        if direccion == 'w' and fila > 0 and self.laberinto[fila - 1][columna] != 'X':
            fila -= 1

        elif direccion == 's' and fila < len(self.laberinto) - 1 and self.laberinto[fila + 1][columna] != 'X':
            fila += 1

        elif direccion == 'a' and columna > 0 and self.laberinto[fila][columna - 1] != 'X':
            columna -= 1

        elif direccion == 'd' and columna < len(self.laberinto[0]) - 1 and self.laberinto[fila][columna + 1] != 'X':
            columna += 1


        self.laberinto[self.posicion_actual[0]][self.posicion_actual[1]] = ' '

        self.posicion_actual = (fila, columna)

        self.laberinto[fila][columna] = '¤'

        # Agregar pasos a la lista   
        self.pasos_seguidos.append(direccion)  

        self.mostrar_laberinto()

        # Sirve para que cuando llegue a la salida te diga que has ganado.
        if self.posicion_actual == self.destino:
            print("¡Felicidades, has completado el laberinto!")
            print("Pasos seguidos:", self.pasos_seguidos)


# Coordenadas del muro
muro = ((0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (2, 1), (2, 3), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3))

# Crear una instancia de Laberinto
lab = Laberinto(muro)

# Mostrar el laberinto inicial
lab.mostrar_laberinto()

# Moverse por el laberinto hasta completarlo
while lab.posicion_actual != lab.destino:
    direccion = input("Ingresa la dirección (arriba(w), abajo(s), izquierda(a), derecha(d)): ").lower()
    lab.moverse(direccion)

