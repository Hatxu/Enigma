from Rotor import Rotor
from Reflector import Reflector
from Plugboard import Plugboard

# Valores            
rotor1 =Rotor("III",'A',"Rapida")
rotor2 =Rotor("II",'A',"Media")
rotor3 =Rotor("I",'A',"Lenta")
reflector = Reflector("UKW-B")
plugboardslist = [] #List to save all the plugs in it.
listaenchufe = []
contadorenchufe = 12
Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
modelosR = ['I','II','III','IV','V']
modelosE = ['UKW-A','UKW-B','UKW-C']


# Funciones de Maquinas
def plugValor(letra):
    if len(plugboardslist)==0:
        return(letra)
    if sorted([valor.changeplug(letra) for valor in plugboardslist])[-1] != '0':
        return(sorted([valor.changeplug(letra) for valor in plugboardslist])[-1])
    else: 
        return(letra)
       #return sorted([valor.changeplug(letra) for valor in plugboardslist])[-1] if sorted([valor.changeplug(letra) for valor in plugboardslist])[-1] != '0' else letra        
            
def señalRes(valor):
     
   # print("VaI: ",valor)
   # print("VaP: ",plugValor(valor))
    
    print("R1i: ",rotor1.pasoletra(rotor1.letracual(plugValor(valor))))
   # print("Ori1: ",rotor1.valorabc(rotor1.pasoletra(rotor1.letracual(plugValor(valor)))))
    print("R2i: ",rotor2.pasoletra(rotor2.letracual( rotor1.valorabc(rotor1.pasoletra(rotor1.letracual(plugValor(valor))))) ))
   # print("Ori2: ",rotor2.valorabc(rotor2.pasoletra(rotor2.letracual( rotor1.valorabc(rotor1.pasoletra(rotor1.letracual(plugValor(valor))))) )))
    
    print("R3i: ", rotor3.pasoletra(rotor3.letracual(rotor2.valorabc(rotor2.pasoletra(rotor2.letracual( rotor1.valorabc(rotor1.pasoletra(rotor1.letracual(plugValor(valor))))) )))))
   # print("Ori3: ", rotor3.valorabc(rotor3.pasoletra(rotor3.letracual(rotor2.valorabc(rotor2.pasoletra(rotor2.letracual( rotor1.valorabc(rotor1.pasoletra(rotor1.letracual(plugValor(valor)))))))))))
    print("Ref:  "+ reflector.pasoletra(rotor3.valorabc(rotor3.pasoletra(rotor3.letracual(rotor2.valorabc(rotor2.pasoletra(rotor2.letracual( rotor1.valorabc(rotor1.pasoletra(rotor1.letracual(plugValor(valor))))))))))))

    print("R3o: ",rotor3.regreso(rotor3.letracual(reflector.pasoletra(rotor3.valorabc(rotor3.pasoletra(rotor3.letracual(rotor2.valorabc(rotor2.pasoletra(rotor2.letracual( rotor1.valorabc(rotor1.pasoletra(rotor1.letracual(plugValor(valor))))))))))))))
    print("R2o: ",rotor2.regreso(rotor2.letracual(rotor3.valorabc(rotor3.regreso(rotor3.letracual(reflector.pasoletra(rotor3.valorabc(rotor3.pasoletra(rotor3.letracual(rotor2.valorabc(rotor2.pasoletra(rotor2.letracual( rotor1.valorabc(rotor1.pasoletra(rotor1.letracual(plugValor(valor)))))))))))))))))
    print("R2o: ",rotor1.regreso(rotor1.letracual(rotor2.valorabc(rotor2.regreso(rotor2.letracual(rotor3.valorabc(rotor3.regreso(rotor3.letracual(reflector.pasoletra(rotor3.valorabc(rotor3.pasoletra(rotor3.letracual(rotor2.valorabc(rotor2.pasoletra(rotor2.letracual( rotor1.valorabc(rotor1.pasoletra(rotor1.letracual(plugValor(valor))))))))))))))))))))


    return plugValor(rotor1.valorabc(rotor1.regreso(rotor1.letracual(rotor2.valorabc(rotor2.regreso(rotor2.letracual(rotor3.valorabc(rotor3.regreso(rotor3.letracual(reflector.pasoletra(rotor3.valorabc(rotor3.pasoletra(rotor3.letracual(rotor2.valorabc(rotor2.pasoletra(rotor2.letracual( rotor1.valorabc(rotor1.pasoletra(rotor1.letracual(plugValor(valor)))))))))))))))))))))

   
def movimientoRotores(valor):
    lista=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    if rotor1.posicion == rotor1.turnover:
        rotor1.posicion = lista[lista.index(rotor1.posicion)+1]
        if rotor2.posicion == 'Z':
                rotor2.posicion = lista[0]
        else:
            if rotor2.posicion == rotor2.turnover:
                if rotor3.posicion == 'Z':
                    rotor3.posicion = lista[0]
                else:
                    rotor3.posicion =lista[lista.index(rotor3.posicion)+1]
            rotor2.posicion = lista[lista.index(rotor2.posicion)+1]          
    else:
        if rotor1.posicion == 'Z':
            rotor1.posicion = lista[0]
        else:
            rotor1.posicion = lista[lista.index(rotor1.posicion)+1]
        if rotor2.posicion == rotor2.turnover:
            rotor2.posicion = lista[lista.index(rotor2.posicion)+1]
            if rotor3.posicion == 'Z':
                rotor3.posicion = lista[0]

            
    return señalRes(valor)

# Funciones de Interfaz:
def mensajerapido(mensaje): #Modo Veloz
    codigo = list(mensaje)
    return "".join([movimientoRotores(i.upper()) if i.upper() in Alphabet else i for i in codigo]) 
