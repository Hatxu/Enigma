class Reflector:
    def __init__(self,modelo):
        self.modelo = modelo
        self.diccio= {}
        self.version(modelo)
        
    def __str__(self):
        return "El Reflector es un modelo: "+self.modelo
        
    def version(self,modelo): #Modelo del Reflector
        if modelo == 'UKW-A':
            self.diccio = {'A': 'E', 'B': 'J', 'C': 'M', 'D': 'Z', 'E': 'A', 'F': 'L', 'G': 'Y', 'H': 'X', 'I': 'V', 'J': 'B', 'K': 'W', 'L': 'F', 'M':'C', 'N': 'R', 'O': 'Q', 'P': 'U', 'Q': 'O', 'R': 'N', 'S': 'T', 'T': 'S', 'U': 'P', 'V': 'I', 'W': 'K', 'X': 'H', 'Y': 'G', 'Z': 'D'}
        elif modelo == 'UKW-B':
            self.diccio = {'A': 'Y', 'B': 'R', 'C': 'U', 'D': 'H', 'E': 'Q', 'F': 'S', 'G': 'L', 'H': 'D', 'I': 'P', 'J': 'X', 'K': 'N', 'L': 'G', 'M':'O', 'N': 'K', 'O': 'M', 'P': 'I', 'Q': 'E', 'R': 'B', 'S': 'F', 'T': 'Z', 'U': 'C', 'V': 'W', 'W': 'V', 'X': 'J', 'Y': 'A', 'Z': 'T'}
        elif modelo == 'UKW-C':
            self.diccio = {'A': 'F', 'B': 'V', 'C': 'P', 'D': 'J', 'E': 'I', 'F': 'A', 'G': 'O', 'H': 'Y', 'I': 'E', 'J': 'D', 'K': 'R', 'L': 'Z', 'M':'X', 'N': 'W', 'O': 'G', 'P': 'C', 'Q': 'T', 'R': 'K', 'S': 'U', 'T': 'Q', 'U': 'S', 'V': 'B', 'W': 'N', 'X': 'M', 'Y': 'H', 'Z': 'L'}
        else: 
            self.diccio=("No existe ese modelo")  
            
    def pasoletra(self,letra): #devuelve la letra del diccionario
        return self.diccio.get(letra)