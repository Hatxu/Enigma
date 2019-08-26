from Rotor import Rotor
from Reflector import Reflector
from Plugboard import Plugboard
from Funciones import*






def Interfaz():
  contadorenchufe = 12
  print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
  print('8888888888 888b    888 8888888  .d8888b.  888b     d888        d8888 ')
  print('888        8888b   888   888   d88P  Y88b 8888b   d8888       d88888 ')
  print('888        88888b  888   888   888    888 88888b.d88888      d88P888 ')
  print('8888888    888Y88b 888   888   888        888Y88888P888     d88P 888 ')
  print('888        888 Y88b888   888   888  88888 888 Y888P 888    d88P  888 ')
  print('888        888  Y88888   888   888    888 888  Y8P  888   d88P   888 ')
  print('888        888   Y8888   888   Y88b  d88P 888   "   888  d8888888888 ')
  print('8888888888 888    Y888 8888888  "Y8888P88 888       888 d88P     888 ')
  valor = True
  while valor == True:
      print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
      print("Si desea configurar Engima, presione 1.")    
      print("Si desea utilizar Enigma, presione 2.")
      print("Si desea saber mas de Enigma, presione 3.")
      print("Para salir, presione 4.")
      while True:
          try:
              menu = int(input("Opción: "))
              if menu not in (1,2,3):
                  raise Exception
              break
          except Exception:
              print("Ingrese una Opción valida.")
      if menu ==1:
          while menu ==1:
          #Create
              submenu = 0
              print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
              print("Si desea ver las opciones de Enchufes, presione 1.")
              print("Si desea  ver las opciones de los Rotores, presione 2.")
              print("Si desea editar el Reflector, presione 3.")
              print("Si quiere volver al menu Principal, presione 4.")
              while True:
                  try:
                      submenu = int(input("Opción: "))
                      if menu not in (1,2,3,4):
                          raise Exception
                      break
                  except Exception:
                      print("Ingrese una Opción valida.")
              if submenu == 1:
                  while submenu == 1:
                      print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
                      print("Si desea crear un Enchufe, presione 1.")
                      print("Si desea ver los Enchufes existentes, presione 2.")
                      print("Si desea volver al Menu anterior, presione 3.")
                      print("Si quiere volver al Menu Principal, presione 4 ")
                      
                      subsubmenu = 0
                      while True:
                          try:
                              subsubmenu = int(input("Opción: "))
                              if subsubmenu not in (1,2,3,4):
                                  raise Exception
                              break
                          except Exception:
                              print("Ingrese una Opción valida.")
                      if subsubmenu == 1:
                          if contadorenchufe != 0:
                              print("Letras ocupadas: ", listaenchufe if len(listaenchufe) != 0 else "Ninguna", ", te quedas por usar: ", contadorenchufe," enchufes.")
                              print("Inserta el valor de Nodo 'A' y el Nodo 'B'.")
                              while True:
                                  try:
                                      NodoA = input("Nodo 'A': ")[0].upper()
                                      if NodoA in listaenchufe:
                                          raise Exception
                                      if NodoA not in Alphabet:
                                          raise ValueError
                                      break     
                                  except Exception:
                                      print("La letra que ingreso esta siendo usada ó esta utilizando un valor invalido.")
                              listaenchufe.append(NodoA)
                              while True:
                                  try:
                                      NodoB = input("Nodo 'B': ")[0].upper()
                                      if NodoB in listaenchufe:
                                          raise Exception
                                      if NodoB not in Alphabet:
                                          raise ValueError
                                      break     
                                  except Exception:
                                      print("La letra que ingreso esta siendo usada ó esta utilizando un valor invalido.")
                              listaenchufe.append(NodoB)  
                              plugboardslist.append(Plugboard(NodoA, NodoB))
                              contadorenchufe -= 1
                          else: 
                              print("Ya no puedes crear mas enchufes.")
                      if subsubmenu == 2:
                          if len(plugboardslist)==0:
                              print("Todavia no se han conectado ningún enchufe")
                          else:
                              for i in plugboardslist:
                                  print("Enchufe",plugboardslist.index(i)+1,": ",i)
                  
                      if subsubmenu == 3:  
                          submenu =0
                      if subsubmenu == 4: 
                          submenu = 0
                          menu = 0    
              elif submenu == 2:
                  while submenu == 2:
                      print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
                      print("Si desea editar los Rotores, presione 1.")
                      print("Si desea ver los Rotores, presione 2.")
                      print("Si desea volver al Menu anterior, presione 3.")
                      print("Si quiere volver al Menu Principal, presione 4 ")
                      subsubmenu = 0
                      while True:
                          try:
                              subsubmenu = int(input("Opción: "))
                              if subsubmenu not in (1,2,3,4):
                                  raise Exception
                              break
                          except Exception:
                              print("Ingrese una Opción valida.")
                      if subsubmenu == 1:
                          while subsubmenu == 1:
                              subsubsubmenu = 0
                              print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
                              print("Si desea editar el Rotor Rapido, presione 1.")
                              print("Si desea editar el Rotor Medio, presione 2.")
                              print("Si desea editar el Rotor Lento, presione 3.")
                              print("Si quiere volver al Menu anterior, presione 4 ")
                              print("Si quiere volver al Menu Principal, presione 5 ")
                              while True:
                                  try:
                                      subsubsubmenu = int(input("Opción: "))
                                      if subsubsubmenu not in (1,2,3,4,5):
                                          raise Exception
                                      break
                                  except Exception:
                                      print("Ingrese una Opción valida.")
                              if subsubsubmenu ==1:
                                  print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
                                  print(rotor1)
                                  print("Los modelos del rotor son los siguientes:")
                                  print(modelosR)
                                  while True:
                                      try:
                                          inpmodelo = input("Ingresa el modelo que usaras: ")
                                          if inpmodelo not in modelosR:
                                              raise Exception
                                          break
                                      except Exception:
                                          print("Ingrese una Opción valida.")
                                  rotor1.modelo = inpmodelo   
                                  rotor1.version(inpmodelo)
                                  while True:
                                      try:
                                          inposicion = input("Ingrese la posición del Rotor: ")
                                          if inposicion.upper() not in Alphabet:
                                              raise Exception
                                          break
                                      except Exception:
                                          print("Ingrese una Opción valida.")
                                  rotor1.posicion= inposicion.upper()
                                  print("Cambio completo.")
                                  print(rotor1)
                                  
                              if subsubsubmenu ==2:
                                  print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
                                  print(rotor2)
                                  print("Los modelos del rotor son los siguientes: ")
                                  print(modelosR)
                                  while True:
                                      try:
                                          inpmodelo = input("Ingresa el modelo que usaras: ")
                                          if inpmodelo not in modelosR:
                                              raise Exception
                                          break
                                      except Exception:
                                          print("Ingrese una Opción valida")
                                  rotor2.modelo = inpmodelo  
                                  rotor2.version(inpmodelo)
                                  while True:
                                      try:
                                          inposicion = input("Ingrese la posicion del Rotor: ")
                                          if inposicion.upper() not in Alphabet:
                                              raise Exception
                                          break
                                      except Exception:
                                          print("Ingrese una Opción valida.")
                                  rotor2.posicion= inposicion.upper()
                                  print("Cambio completo.")
                                  print(rotor2)
                              
                              if subsubsubmenu ==3:
                                  print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
                                  print(rotor3)
                                  print("Los modelos del rotor son los siguientes: ")
                                  print(modelosR)
                                  while True:
                                      try:
                                          inpmodelo = input("Ingresa el modelo que usaras: ")
                                          if inpmodelo not in modelosR:
                                              raise Exception
                                          break
                                      except Exception:
                                          print("Ingrese una Opción valida.")
                                  rotor3.modelo = inpmodelo  
                                  rotor3.version(inpmodelo)
                                  while True:
                                      try:
                                          inposicion = input("Ingrese la posición del Rotor: ")
                                          if inposicion.upper() not in Alphabet:
                                              raise Exception
                                          break
                                      except Exception:
                                          print("Ingrese una Opción valida.")
                                  rotor3.posicion= inposicion.upper()
                                  print("Cambio completo.")
                                  print(rotor3)    
                              if subsubsubmenu ==4:
                                  subsubmenu=0 
                              if subsubsubmenu == 5:
                                  subsubmenu = 0
                                  submenu = 0
                                  menu = 0   
                      if subsubmenu ==2:
                          print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
                          print(rotor1)
                          print(rotor2)
                          print(rotor3)
                      if subsubmenu == 3:  
                          submenu =0
                      if subsubmenu == 4: 
                          submenu = 0
                          menu = 0   
                          
              elif submenu == 3:
                  while submenu == 3:
                      print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
                      print("Si desea editar el Reflector, presione 1.")
                      print("Si desea ver el Reflector, presione 2.")
                      print("Si desea volver al Menu anterior, presione 3.")
                      print("Si quiere volver al Menu Principal, presione 4 ")
                      while True:
                          try:
                              subsubmenu = int(input("Opción: "))
                              if subsubmenu not in (1,2,3,4):
                                  raise Exception
                              break
                          except Exception:
                              print("Ingrese un Opción valida.")
                      if subsubmenu == 1:
                              print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
                              print(reflector)
                              print("Los modelos del Reflector son los siguientes:")
                              print(modelosE)
                              while True:
                                  try:
                                      inpmodelo = input("Ingresa el modelo que usaras: ").upper()
                                      if inpmodelo not in modelosE:
                                          raise Exception
                                      break
                                  except Exception:
                                      print("Ingrese una Opción valida.")
                              reflector.modelo= inpmodelo
                              reflector.version(inpmodelo)
                              print("Cambio completo.")
                              print(reflector) 
                      if subsubmenu ==2:
                          print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
                          print(reflector)
                      if subsubmenu == 3:  
                          submenu =0
                      if subsubmenu == 4: 
                          submenu = 0
                          menu = 0   
                                                                  
              elif submenu == 4:
                  menu = 0    
                  
                  
      elif menu == 2:
          while menu == 2:
              print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
              print("Si usar Enigma de Cifrado rapido, presione 1.")
              print("Si usar Enigma de Cifrado lento, presione 2.")
              print("Si desea volver al Menu principal, presione 3.")
              while True:
                  try:
                      submenu = int(input("Opción: "))
                      if menu not in (1,2,3,4):
                          raise Exception
                      break
                  except Exception:
                      print("Ingrese una Opción valida. ")
              if submenu == 1:
                      print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
                      print("Rotores: ", rotor3.posicion,rotor2.posicion,rotor1.posicion)
                      letra = input("Escribe tu mensaje para Codificar aqui:")
                      cifrado = mensajerapido(letra)
                      print("Rotores: ", rotor3.posicion,rotor2.posicion,rotor1.posicion)
                      print("Mensaje Cifrado: ", cifrado)
              elif submenu == 2:
                  print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
                  mensaje = []
                  cifrado = []
                  letra = ""
                  print("Para salir escribe 'Salir'.")
                  while letra != "Salir":
                      print("Rotores: ", rotor3.posicion,rotor2.posicion,rotor1.posicion)
                      while True:
                        try:
                          letra = input("Escribe letra: ")
                          if letra == '':  
                            raise Exception
                          break 
                        except Exception:
                          print("No aceptamos nulls aquí")    
                      if letra == "Salir":
                          print("Mensaje Original: ","".join(mensaje))
                          print("Mensaje Cifrado:  ","".join(cifrado))
                          pass
                      else:
                        letra = letra[-1]
                      if letra.upper() in Alphabet:
                          mensaje.append(letra)
                          x = movimientoRotores(letra.upper())
                          cifrado.append(x)
                          print("Letra cifrada: ",x)

                      else: 
                          mensaje.append(letra)
                          cifrado.append(letra)
              elif submenu == 3:
                  menu = 0
      elif menu == 3:    
          print("")
          print("█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
          print("█ Enigma es una maquina de encryptacion de mensajes Alemana, utilizado     █") 
          print("█ en la segunda guerra mundial. El funcionamiento de enigma consta de      █")
          print("█ tres componentes: Los enchufes o plugs, los rotores y el reflector.      █")
          print("█                                                                          █")
          print("█ El código de Enigma que estan usando fue creado con las siguientes fuen- █")
          print("█ tes de investigación para su desarrollo:                                 █")
          print("█                                                                          █")        
          print("█ * https://web.stanford.edu/class/cs106j/handouts/36-TheEnigmaMachine.pdf █")
          print("█ * https://www.cryptomuseum.com/crypto/enigma/wiring.htm                  █")
          print("█ * https://en.wikipedia.org/wiki/Enigma_machine                           █")
          print("█                                                                          █")
          print("█ Se recomienda entender el funcionamiento de Enigma antes de utilizarse.  █")
          print("█                                                                          █")
          print("█ Creado por: Uriel Gómez Reyes                                            █")
          print("█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
          print("")
      elif menu == 4:    
          valor =False
  # Docs:
  """
  https://web.stanford.edu/class/cs106j/handouts/36-TheEnigmaMachine.pdf
  https://www.cryptomuseum.com/crypto/enigma/wiring.htm
  https://en.wikipedia.org/wiki/Enigma_machine
  """