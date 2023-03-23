from colors import bcolors
# clase del personaje principal
class Character():
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def description(self):
        return f"Tu personaje se llama {bcolors.OKGREEN+self.name+bcolors.ENDC}\nTiene {self.health} puntos de vida y \n{self.power} puntos de ataque."

    def upgradePower(self):
        self.power += 2
        
    def refillHealth(self, vida):
        self.health = vida
