
class Rotor:
    def __init__(self,modelo,posicion,velocidad):
        self.modelo = modelo
        self.posicion = posicion
        self.velocidad = velocidad
        self.turnover = ''
        self.lista = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        self.diccio= {} #Diccionario Input
        self.version(modelo)
        
    def __str__(self):
        return "El rotor de velocidad: "+self.velocidad+", es un modelo: "+self.modelo+", y se encuentra en la posicion: "+self.posicion
    
    def version(self,modelo): #Modelo del rotor
        if modelo == 'I':
            self.diccio = {'A': 'E', 'B': 'K', 'C': 'M', 'D': 'F', 'E': 'L', 'F': 'G', 'G': 'D', 'H': 'Q', 'I': 'V', 'J': 'Z', 'K': 'N', 'L': 'T', 'M':'O', 'N': 'W', 'O': 'Y', 'P': 'H', 'Q': 'X', 'R': 'U', 'S': 'S', 'T': 'P', 'U': 'A', 'V': 'I', 'W': 'B', 'X': 'R', 'Y': 'C', 'Z': 'J'}
            self.turnover = 'Q'
        elif modelo == 'II':
            self.diccio = {'A': 'A', 'B': 'J', 'C': 'D', 'D': 'K', 'E': 'S', 'F': 'I', 'G': 'R', 'H': 'U', 'I': 'X', 'J': 'B', 'K': 'L', 'L': 'H', 'M':'W', 'N': 'T', 'O': 'M', 'P': 'C', 'Q': 'Q', 'R': 'G', 'S': 'Z', 'T': 'N', 'U': 'P', 'V': 'Y', 'W': 'F', 'X': 'V', 'Y': 'O', 'Z': 'E'}
            self.turnover = 'E'
        elif modelo == 'III':
            self.diccio = {'A': 'B', 'B': 'D', 'C': 'F', 'D': 'H', 'E': 'J', 'F': 'L', 'G': 'C', 'H': 'P', 'I': 'R', 'J': 'T', 'K': 'X', 'L': 'V', 'M':'Z', 'N': 'N', 'O': 'Y', 'P': 'E', 'Q': 'I', 'R': 'W', 'S': 'G', 'T': 'A', 'U': 'K', 'V': 'M', 'W': 'U', 'X': 'S', 'Y': 'Q', 'Z': 'O'}
            self.turnover = 'V'
        elif modelo == 'IV':
            self.diccio = {'A': 'E', 'B': 'S', 'C': 'O', 'D': 'V', 'E': 'P', 'F': 'Z', 'G': 'J', 'H': 'A', 'I': 'Y', 'J': 'Q', 'K': 'U', 'L': 'I', 'M':'R', 'N': 'H', 'O': 'X', 'P': 'L', 'Q': 'N', 'R': 'F', 'S': 'T', 'T': 'G', 'U': 'K', 'V': 'D', 'W': 'C', 'X': 'M', 'Y': 'W', 'Z': 'B'}
            self.turnover = 'J'
        elif modelo == 'V':
            self.diccio = {'A': 'V', 'B': 'Z', 'C': 'B', 'D': 'R', 'E': 'G', 'F': 'I', 'G': 'T', 'H': 'Y', 'I': 'U', 'J': 'P', 'K': 'S', 'L': 'D', 'M':'N', 'N': 'H', 'O': 'L', 'P': 'X', 'Q': 'A', 'R': 'W', 'S': 'M', 'T': 'J', 'U': 'Q', 'V': 'O', 'W': 'F', 'X': 'E', 'Y': 'C', 'Z': 'K'}
            self.turnover = 'Z '
        else: 
            self.diccio=("No existe ese modelo")

    
    def pasoletra(self,letra): #devuelve la letra del diccionario
        return self.diccio.get(letra)
      
    def letracual(self,valor): #En base a la posicion de la letra te dice cual sigue"
        resultado = self.lista.index(self.posicion)+ self.lista.index(valor)
        if resultado >= 26:
            return self.lista[resultado-26]
        return self.lista[resultado]

    def valorabc(self,valor): #Es para sacar los valores de la tabla y obetener un resultado.
        resultado = self.lista.index(valor) - self.lista.index(self.posicion)
        if resultado >= 26: 
            return self.lista[resultado-26]
        return self.lista[resultado]
    
    def regreso(self,letra): #Es para sacar los valores de la tabla y obetener un resultado.
        return list(self.diccio.keys())[list(self.diccio.values()).index(letra)]
