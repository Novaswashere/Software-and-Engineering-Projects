import random

class Player:

    def __init__(self,name,health,attackpower,defensepower):
        self.name = name
        self.health = health
        self.attackpower = attackpower
        self.defensepower = defensepower


class Battle:

    def __init__(self,fighter1,fighter2):
        self.player1 = fighter1
        self.player2 = fighter2


    def attack(self):

        while self.player1.health > 0 and self.player2.health > 0:
            damageDone = self.player1.attackpower - self.player2.defensepower

            if damageDone > 0:
                self.player2.health = self.player2.health - damageDone
            else:
                self.player2.health = self.player2.health - 1

            print(f"{self.player1.name} did {damageDone} damage to {self.player2.name} and now {self.player2.name} has {self.player2.health} HP left." + '\n ')

            damageDone2 = self.player2.attackpower - self.player1.defensepower

            if damageDone2 > 0:
                self.player1.health = self.player1.health - damageDone2
            else:
                self.player1.health = self.player1.health - 1

            print(
                f"{self.player2.name} did {damageDone2} damage to {self.player1.name} and now {self.player1.name} has {self.player1.health} HP left." + '\n')

        if self.player1.health > 0 and self.player2.health <= 0:
            print(f"The winner is {self.player1.name}")
        else:
            print(f"The winner is {self.player2.name}")









while True:
    player1_Name = input("Please enter the player 1 name: ")
    player2_Name = input("Please enter player 2 name: ")

    #attack should be between 15-25
    #DP should be between 5-15
    #Health should be between 100-150

    player1 = Player(player1_Name,random.randint(100,150),random.randint(15,25),random.randint(5,15) )
    player2 = Player(player2_Name,random.randint(100,150),random.randint(15,25),random.randint(5,15) )

    simulation = Battle(player1,player2)

    simulation.attack()
    break




