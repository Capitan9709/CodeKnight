# clase de los enemigos
# enemigo goblin
class Goblin():
    def __init__(self, type = "Goblin", health = 5, power = 1):
        self.type = type
        self.health = health
        self.power = power
        
    def description(self):
        return f"Un {self.type} con {self.health} puntos de vida y {self.power} puntos de ataque."

    def reset(self):
        self.health = 5
        self.power = 1
    

# enemigo zombie
class Zombie():
    def __init__(self, type = "Zombie", health = 3, power = 2):
        self.type = type
        self.health = health
        self.power = power
        
    def description(self):
        return f"Un {self.type} con {self.health} puntos de vida y {self.power} puntos de ataque."
    
    def reset(self):
        self.health = 3
        self.power = 2
       
# enemigo shadow
class Shadow():
    def __init__(self, type = "Shadow", health = 1, power = 3):
        self.type = type
        self.health = health
        self.power = power
        
    def description(self):
        return f"Un {self.type} con {self.health} puntos de vida y {self.power} puntos de ataque."
    
    def reset(self):
        self.health = 1
        self.power = 3

# enemigo wizard
class Wizard():
    def __init__(self, type = "Wizard", health = 5, power = 3):
        self.type = type
        self.health = health
        self.power = power
        
    def description(self):
        return f"Un {self.type} con {self.health} puntos de vida y {self.power} puntos de ataque."
    
    def reset(self):
        self.health = 5
        self.power = 3
