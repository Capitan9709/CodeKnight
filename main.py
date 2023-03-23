import random
import time
from character import Character
from enemies import Goblin, Zombie, Shadow, Wizard

enemigos = [Goblin(), Zombie(), Shadow(), Wizard()]
enemigo = None
personaje = None
titulo = """  _____           _      _   __      _       _     _   
 /  __ \         | |    | | / /     (_)     | |   | |  
 | /  \/ ___   __| | ___| |/ / _ __  _  __ _| |__ | |_ 
 | |    / _ \ / _` |/ _ \    \| '_ \| |/ _` | '_ \| __|
 | \__/\ (_) | (_| |  __/ |\  \ | | | | (_| | | | | |_ 
  \____/\___/ \__,_|\___\_| \_/_| |_|_|\__, |_| |_|\__|
                                       __/ |          
                                      |___/           """
introduccion = """Bienvenido a Code Knight, 
un juego de rol en el que tu personaje debera enfrentarse a diferentes 
enemigos para poder avanzar en el juego.
Espero que te lo pases bien."""
separadores = "========================================================="
contadorEnemigos = 0
enemigosEliminados = 0

# funcion para crear el personaje
def crearPersonaje():
    nombrePersonaje = input("Introduce el nombre del personaje: ")
    personaje = Character(nombrePersonaje, 10, 2)
    print(" ")
    return personaje

# funcion para crear un enemigo
def crearEnemigo():
    enemigo = random.choice(enemigos)
    return enemigo

# funcion de opciones del juego
def opciones():
    print("1. Atacar")
    print("2. Huir")
    print("3. Salir del juego")
    opcion = input("Elige una opcion: ")
    print(" ")
    while opcion != "1" and opcion != "2" and opcion != "3":
        opcion = input("Elige una opcion Valida: ")
        print(" ")
    return opcion

# funcion para sumar el contador de enemigos 
def sumarContadorEnemigos():
    global contadorEnemigos
    contadorEnemigos += 1
    
# funcion para obtener el contador de enemigos
def getContadorEnemigos():
    return contadorEnemigos

# funcion para sumar el contador de enemigos eliminados
def sumarContadorEnemigosEliminados():
    global enemigosEliminados
    enemigosEliminados += 1

# funcion para obtener el contador de enemigos eliminados
def getContadorEnemigosEliminados():
    return enemigosEliminados

# funcion de ataque
def atacar(personaje, enemigo):
    enemigoMuerto = False
    print("Has decidido atacar.")
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
            if getContadorEnemigosEliminados() > 0:
                    print(f"Has eliminado {getContadorEnemigosEliminados()} enemigos de {getContadorEnemigos()} enemigos encontrados.")
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
def huir():
    huida = False
    print("Has decidido huir del combate.")
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
    
        print("Has encontrado un enemigo!")
        sumarContadorEnemigos()
        enemigo = crearEnemigo()
        
        print(separadores)
        print(enemigo.description())
        print(separadores)

        while (enemigo.health > 0 or enemigo != None) and personaje.health > 0:
            opcion = opciones()
            if opcion == "1":
                enemigoMuerto = atacar(personaje, enemigo)
                if enemigoMuerto == True:
                    sumarContadorEnemigosEliminados()
                    enemigo.reset()
                    print("Has encontrado otro enemigo!")
                    sumarContadorEnemigos()
                    enemigo = crearEnemigo()
                    
                    print(separadores)
                    print(enemigo.description())
                    print(separadores)
            elif opcion == "2":
                huida = huir()
                if huida == True:
                    print("Has encontrado otro enemigo!")
                    sumarContadorEnemigos()
                    enemigo = crearEnemigo()
                    
                    print(separadores)
                    print(enemigo.description())
                    print(separadores)
            elif opcion == "3":
                print("Has decidido salir del juego.")
                print(" ")
                if getContadorEnemigosEliminados() > 0:
                    print(f"Has eliminado {getContadorEnemigosEliminados()} enemigos de {getContadorEnemigos()} enemigos encontrados.")
                    print("---------------------------------")
                    print("Gracias por jugar!")
                    quit()
                else:
                    quit()
        
            
main()