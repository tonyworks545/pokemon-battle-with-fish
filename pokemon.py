import time
import numpy as np 
import sys 

# Delay printing

def delay_print(s):
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-charater-at-a-time-on-one-line
    for c in s: 
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

# Create the class
class Pokemon:
    def __init__(self, name, types, moves, EVs, health='==================='):
        # save variables as attributes
        self.name = name 
        self.types = types
        self.moves = moves   
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20 # Amount of health bars


    def fight(self, pokemon2):
        # Allow two pokemon to fight each other

        # Print fight information
        print("-----POKEMONE BATTLE-----")
        print(f"\n{self.name}")
        print("TYPE/",self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("LVL", 3*(1+np.mean([self.attack,self.defense])))
        print("\nVS")
        print(f"\n{pokemon2.name}")
        print("TYPE/",pokemon2.types)
        print("ATTACK/", pokemon2.attack)
        print("DEFENSE/", pokemon2.defense)
        print("LVL", 3*(1+np.mean([pokemon2.attack,pokemon2.defense])))

        time.sleep(2)

        # Consid type advantages
        version = ['Fire', 'Water', 'Grass']
        string_1_attack = 'default_1'   #default in case of issue
        string_2_attack = 'default_2'
        for i,k in enumerate(version):
            if self.types == k:
                # both are same type
                if pokemon2.types == k:
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts not very effective...'

                # pokemon2 is STRONG
                if pokemon2.types == version[(i+1)%3]:
                    pokemon2.attack *= 2
                    pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = '\nit not very effective...'
                    string_2_attack = '\nit super effective!'
                
                # pokemon 2 is WEAK
                if pokemon2.types == version[(i+2)%3]:
                    self.attack *= 2
                    self.defense *= 2
                    pokemon2.attack /= 2
                    pokemon2.defense /= 2
                    string_1_attack = '\nIts super effective!'
                    string_2_attack = '\nIts not very effective'


        # Now for the actual fighting...
        # Continue while pokemon srills have health
        while (self.bars > 0) and (pokemon2.bars > 0):
            # Print the heath of each pokemon
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{pokemon2.name}\t\tHLTH\t{pokemon2.health}\n")

            print(f"Go {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            index = int(input('pick a move:'))
            delay_print(f"\n{self.name} used {self.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_1_attack)

            # Determine damage
            pokemon2.bars -= self.attack
            pokemon2.heath = ""

            # Add back bars plus defense boost
            for j in range(int(pokemon2.bars+.1*pokemon2.defense)):
                pokemon2.heath += "="

            time.sleep(1)   
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{pokemon2.name}\t\tHLTH\t{pokemon2.health}\n")
            time.sleep(.5)

            # Check to see if pokemon fainted
            if pokemon2.bars <= 0:
                delay_print("\n..." + pokemon2.name + ' fainted.')
                break

            # Pokemon2s turn

            print(f"Go {pokemon2.name}!")
            for i, x in enumerate(pokemon2.moves):
                print(f"{i+1}.", x)
            index = int(input('pick a move:'))
            delay_print(f"\n{pokemon2.name} used {pokemon2.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_2_attack)

            # Determine damage
            self.bars -= pokemon2.attack
            self.heath = ""

            # Add back bars plus defense boost
            for j in range(int(self.bars+.1*self.defense)):
                self.heath += "="

            time.sleep(1)   
            print(f"{self.name}\t\tHLTH\t{self.health}")
            print(f"{pokemon2.name}\t\tHLTH\t{pokemon2.health}\n")
            time.sleep(.5)

            # Check to see if pokemon fainted
            if self.bars <= 0:
                delay_print("\n..." + self.name + ' fainted.')
                break
        
        money = np.random.choice(5000)
        delay_print(f"\nOpponent paid you ${money}.")






if __name__ == '__main__':
    # Crate pokemon
    Charizard = Pokemon('Charizard', 'Fire', ['Flamethower', 'Fly', 'Blast Burn', 'Fire Punch'], {'ATTACK':12, 'DEFENSE': 8})
    Blastoise = Pokemon('Blastoise', 'Water', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'],{'ATTACK':10, 'DEFENSE':10})
    Venusaur = Pokemon('Venusaur', 'Grass', ['Vine wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'],{'ATTACK':8, 'DEFENSE':5})

    Charmander = Pokemon('Charmander', 'Fire', ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'],{'ATTACK':4, 'DEFENSE':2})
    Squirtle = Pokemon('Squirtle', 'Water', ['Bubblebeam', 'Tackle', 'Headbutt', 'Surf'],{'ATTACK':3, 'DEFENSE':3})
    Bulbasaur = Pokemon('Bulbasaur', 'Grass', ['Vine wip', 'Razor Leaf', 'Tackle', 'Leech Seed'],{'ATTACK':2, 'DEFENSE':4})

    Charmeleon = Pokemon('Charmeleon', 'Fire', ['Ember', 'Scratch', 'Flamethower', 'Fire Punch'],{'ATTACK':6, 'DEFENSE':5})
    Wartortle = Pokemon('Wartortle', 'Water', ['Bubblebeam', 'Water Gun', 'Headbutt', 'Surf'],{'ATTACK':5, 'DEFENSE':5})
    Ivysaur = Pokemon('Ivysaur\t', 'Grass', ['Vine Wip', 'Razor Leaf', 'Bullet Seed', 'Leech Seed'],{'ATTACK':4, 'DEFENSE':6})


    Charizard.fight(Blastoise) 
    # Get them to fight each other












