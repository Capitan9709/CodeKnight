import random
import time
from character import Character
from enemies import Goblin, Zombie, Shadow, Wizard
from colors import bcolors

enemigos = [Goblin(), Zombie(), Shadow(), Wizard()]
enemigo = None
personaje = None
maximoVidaPersonaje = 0
titulo = bcolors.FAIL+"""  _____           _      _   __      _       _     _   
 /  __ \         | |    | | / /     (_)     | |   | |  
 | /  \/ ___   __| | ___| |/ / _ __  _  __ _| |__ | |_ 
 | |    / _ \ / _` |/ _ \    \| '_ \| |/ _` | '_ \| __|
 | \__/\ (_) | (_| |  __/ |\  \ | | | | (_| | | | | |_ 
  \____/\___/ \__,_|\___\_| \_/_| |_|_|\__, |_| |_|\__|
                                       __/ |          
                                      |___/           """+bcolors.ENDC
introduccion = """Bienvenido a Code Knight, 
un juego de rol en el que tu personaje debera enfrentarse a diferentes 
enemigos para poder avanzar en el juego.
El juego esta en desarrollo, por lo que puede que encuentres algun error.
Espero que te lo pases bien."""
separadores = bcolors.OKCYAN+"========================================================="+bcolors.ENDC
separadores2 = bcolors.WARNING+"---------------------------------"+bcolors.ENDC
contadorEnemigos = 0
enemigosEliminados = 0
nivel = 1

# funcion para crear el personaje
def crearPersonaje():
    """Funcion para crear el personaje
    Devuelve el personaje creado
    """
    nombrePersonaje = input(bcolors.OKGREEN+"Introduce el nombre del personaje: "+bcolors.ENDC)
    personaje = Character(nombrePersonaje, 10, 2)
    actualizarMaximoVidaPersonaje(personaje)
    print(" ")
    return personaje

# funcion para actualizar la vida maxima que tiene el personaje
def actualizarMaximoVidaPersonaje(personaje):
    """Funcion para actualizar la vida maxima del personaje
    """
    global maximoVidaPersonaje
    maximoVidaPersonaje = personaje.health

def actualizarNumEnemigosEliminados():
    """Funcion para actualizar el numero de enemigos eliminados
    """
    global numEnemigosEliminados
    numEnemigosEliminados = str(enemigosEliminados)

# funcion para crear un enemigo
def crearEnemigo():
    """Funcion para crear un enemigo aleatorio
    Devuelve el enemigo creado
    """
    enemigo = random.choice(enemigos)
    return enemigo

# funcion para crear un siguiente enemigo al que enfrentarse
# def crearSiguienteEnemigo():
#     """Funcion para crear otro enemigo al haber derrotado al anterior
#     o haber escapado del anterior.
#     """
#     print("Has encontrado otro "+bcolors.FAIL+"Enemigo!"+bcolors.ENDC)
#     sumarContadorEnemigos()
#     enemigo = crearEnemigo()
    
#     return enemigo

# funcion de opciones del juego
def opciones():
    """Funcion para mostrar las opciones del juego
    Devuelve la opcion elegida por el usuario
    """
    print(bcolors.WARNING+"1. Atacar")
    print("2. Huir")
    print("3. Salir del juego"+bcolors.ENDC)
    print(separadores2)
    opcion = input("Elige una opcion: ")
    print(" ")
    while opcion != "1" and opcion != "2" and opcion != "3":
        opcion = input("Elige una opcion Valida: ")
        print(" ")
    return opcion

# funcion para sumar el contador de enemigos 
def sumarContadorEnemigos():
    """Funcion para sumar el contador de enemigos
    Devuelve el contador de enemigos
    """
    global contadorEnemigos
    contadorEnemigos += 1

# funcion para sumar el contador de enemigos eliminados
def sumarContadorEnemigosEliminados():
    """Funcion para sumar el contador de enemigos eliminados
    """
    global enemigosEliminados
    enemigosEliminados += 1

# funcion para subir de nivel
def subirNivel():
    """Funcion para subir de nivel
    """
    global nivel
    nivel += 1

# funcion de prints al subir de nivel
def textoSubirNivel():
    """Funcion de prints al subir de nivel
    """
    subirNivel()
    print(separadores2)
    print("Subes de Nivel!")
    print(separadores2)
    print(" ")
    print("Estas en el Nivel ", nivel,"!")
    print(" ")

# funcion para mostrar un tesoro
def tesoroSorpresa(personaje):
    """Funcion para mostrar un tesoro
    Este llama a otra funcion para elegir las opciones del tesoro
    """
    print(" ")
    print(separadores)
    print("Has encontrado un "+bcolors.OKGREEN+"Tesoro!"+bcolors.ENDC)
    print(separadores)
    print(" ")
    print("En el tesoro hay: ")
    print("1. Un arma")
    print("2. Una pocion de vida")
    opcionesTesoro(personaje)

# funcion para mostrar las opciones del tesoro
def opcionesTesoro(personaje):
    eleccion = input("Elige una opcion: ")
    if eleccion == "1":
        print(" ")
        print("Has elegido el Arma!")
        print(" ")
        print("Tu personaje ha mejorado su ataque!")
        print(" ")
        personaje.upgradePower()
        print(bcolors.OKGREEN+personaje.name+bcolors.ENDC+" ahora tiene "+bcolors.OKGREEN+str(personaje.power)+bcolors.ENDC+" puntos de ataque!")
        print(separadores)
        print(" ")
    elif eleccion == "2":
        print(" ")
        print("Has elegido la pocion de vida!")
        print(" ")
        print("Tu personaje se ha curado completamente!")
        print(" ")
        personaje.refillHealth(maximoVidaPersonaje)
        print(bcolors.OKGREEN+personaje.name+bcolors.ENDC+" ahora tiene "+bcolors.OKGREEN+str(personaje.health)+bcolors.ENDC+" puntos de vida!")
        print(separadores)
        print(" ")

# funcion de ataque
def atacar(personaje, enemigo):
    """Funcion para atacar al enemigo, si este no muere, el enemigo atacara al personaje.
    Seguira asi sucesivamente hasta que uno de los dos muera.
    Cuando el enemigo muere, el juego continua.
    Cuando el personaje muere, el juego termina.
    Devuelve True si el enemigo ha muerto.
    quit() si el personaje ha muerto.
    """
    enemigoMuerto = False
    print("Has decidido "+bcolors.FAIL+"Atacar."+bcolors.ENDC)
    print(" ")
    time.sleep(0.5)
    
    enemigo.health -= personaje.power
    print(f"Tu personaje ha hecho {personaje.power} puntos de daño al enemigo.")
    
    # Comparamos si el enemigo ha muerto
    if enemigo.health <= 0:
        # Si el enemigo ha muerto continua el juego
        print(f"El enemigo tiene {enemigo.health} puntos de vida, ha muerto.")
        print(" ")
        print("Has ganado el combate!")
        print(separadores)
        print(separadores)
        enemigoMuerto = True
        return enemigoMuerto
    else:
        personaje.health -= enemigo.power
        print(f"El enemigo ha hecho {enemigo.power} puntos de daño al personaje.")
        
        # Comparamos si el personaje ha muerto
        if personaje.health <= 0:
            # Si mi personaje ha muerto, el juego termina
            print(f"Tu personaje tiene {personaje.health} puntos de vida, ha muerto.")
            print(f"El enemigo se ha quedado con {enemigo.health} puntos de vida.")
            print(" ")
            print("Has perdido el combate!")
            print(separadores)
            print(separadores)
            if enemigosEliminados > 0:
                    print(f"Has eliminado {enemigosEliminados} enemigos de {contadorEnemigos} enemigos encontrados.")
                    print("---------------------------------")
                    print("Gracias por jugar!")
                    quit()
            else:
                quit()
        else:
            # Si el personaje no ha muerto, se muestran los puntos de vida de ambos
            print(f"Tu personaje tiene {personaje.health} puntos de vida.")
            print(f"El enemigo tiene {enemigo.health} puntos de vida.")
            print(" ")
            print(separadores)

# funcion de huida de combate
def huir(personaje, enemigo):
    """Funcion de huida para dar la opcion al personaje de huir del combate.
    Si no consigue huir, el enemigo le hara daño.
    Devuelve True si el personaje ha conseguido huir.
    """
    
    # funcion para que el enemigo haga daño al personaje
    def dañoParaPersonaje(personaje, enemigo):
        """Si el personaje intenta huir y no 
        lo consigue este recibira daño del enemigo.
        """
        personaje.health -= enemigo.power
        print(f"El enemigo ha hecho {enemigo.power} puntos de daño al personaje mientras intentaba escapar.")
        
        # Comparamos si el personaje ha muerto
        if personaje.health <= 0:
            # Si mi personaje ha muerto, el juego termina
            print(f"Tu personaje tiene {personaje.health} puntos de vida, ha muerto.")
            print(f"El enemigo se ha quedado con {enemigo.health} puntos de vida.")
            print(" ")
            print("Has perdido el combate!")
            print(separadores)
            print(separadores)
            if enemigosEliminados > 0:
                    print(f"Has eliminado {enemigosEliminados} enemigos de {contadorEnemigos} enemigos encontrados.")
                    print("---------------------------------")
                    print("Gracias por jugar!")
                    quit()
            else:
                quit()
        else:
            # Si el personaje no ha muerto, se muestran los puntos de vida de ambos
            print(f"Tu personaje tiene {personaje.health} puntos de vida.")
            print(f"El enemigo tiene {enemigo.health} puntos de vida.")
            print(" ")
            print(separadores)
        
    huida = False
    print("Has decidido "+bcolors.OKBLUE+"Huir"+bcolors.ENDC+" del combate.")
    print(" ")
    time.sleep(0.5)
    # variable dadoHuida para definir como de dificil sera
    # en ese combate
    dadoHuida = random.randint(1, 6)
    
    # 2 dados para que sea totalemente aleatoria la decision de huida
    dado1 = random.randint(1, dadoHuida)
    dado2 = random.randint(1, dadoHuida)
    
    # si el dadoHuida es 1, el personaje huye del combate automaticamente
    if dadoHuida == 1:
        print("Has huido del combate.")
        print(separadores)
        print(separadores)
        # si el personaje huye del combate, el enemigo desaparece
        huida = True
        return huida
        
    # si el dadoHuida es 2, 3 o 4, el personaje tiene posibilidades de huir
    elif dadoHuida >=2 and dadoHuida <= 4:
        print("Hay posibilidades de huir del combate...")
        print(" ")
        time.sleep(0.5)
        if dado1 == dado2:
            print("Has huido del combate.")
            print(separadores)
            print(separadores)
            # si el personaje huye del combate, el enemigo desaparece
            huida = True
            return huida
        else:
            print("No has podido huir del combate.")
            print(" ")
            dañoParaPersonaje(personaje, enemigo)
            
    # si el dadoHuida es 5 o 6, el personaje tiene pocas posibilidades de huir
    elif dadoHuida > 4:
        print("Hay pocas posibilidades de huir del combate.")
        print(" ")
        time.sleep(0.5)
        if dado1 == dado2:
            print("Has huido del combate.")
            print(separadores)
            print(separadores)
            # si el personaje huye del combate, el enemigo desaparece
            huida = True
            return huida
        else:
            print("No has podido huir del combate.")
            print(" ")
            dañoParaPersonaje(personaje, enemigo)
            

# funcion principal
def main():
    print(separadores)
    print(titulo)
    print(separadores)
    print(introduccion)
    print(separadores)
    time.sleep(1)
    
    personaje = crearPersonaje()   
    print(separadores) 
    print(personaje.description())
    print(separadores+"\n")
    time.sleep(0.5)
    
    while personaje.health > 0:
    
        print("Has encontrado un "+bcolors.FAIL+"Enemigo!"+bcolors.ENDC)
        sumarContadorEnemigos()
        enemigo = crearEnemigo()
        
        print(separadores)
        print(enemigo.description())
        print(separadores)

        while (enemigo.health >= 0 or enemigo != None) and personaje.health > 0:

            # comprobar los enemigos eliminados para subir de nivel
            if nivel == 1:
                actualizarNumEnemigosEliminados()
                if numEnemigosEliminados[-1] == "5":
                    textoSubirNivel()
            else:
                actualizarNumEnemigosEliminados()
                if numEnemigosEliminados[-1] == "0" or "5":
                    textoSubirNivel()


            opcion = opciones()
            if opcion == "1":
                enemigoMuerto = atacar(personaje, enemigo)
                if enemigoMuerto == True:
                    sumarContadorEnemigosEliminados()
                    enemigo.reset()
                    # comprobar los enemigos vistos para que aparezca un tesoro
                    if contadorEnemigos % 3 == 0:
                        tesoroSorpresa(personaje)
                    # crearSiguienteEnemigo()
                    print("Has encontrado otro "+bcolors.FAIL+"Enemigo!"+bcolors.ENDC)
                    sumarContadorEnemigos()
                    enemigo = crearEnemigo()
                    
                    print(separadores)
                    print(enemigo.description())
                    print(separadores)
                    
            elif opcion == "2":
                huida = huir(personaje, enemigo)
                if huida == True:
                    # comprobar los enemigos vistos para que aparezca un tesoro
                    if contadorEnemigos % 3 == 0:
                        tesoroSorpresa(personaje)
                    # crearSiguienteEnemigo()
                    print("Has encontrado otro "+bcolors.FAIL+"Enemigo!"+bcolors.ENDC)
                    sumarContadorEnemigos()
                    enemigo = crearEnemigo()
                    
                    print(separadores)
                    print(enemigo.description())
                    print(separadores)
                    
            elif opcion == "3":
                print("Has decidido salir del juego.")
                print(" ")
                if enemigosEliminados > 0:
                    print(f"Has eliminado {enemigosEliminados} enemigos de {contadorEnemigos} enemigos encontrados.")
                    print("---------------------------------")
                    print("Gracias por jugar!")
                    quit()
                else:
                    quit()
        

main()