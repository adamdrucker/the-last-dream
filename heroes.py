# Hero boilerplate object
class Hero:
    def __init__(self, name, hp, mp, pattk, mattk, pdef, mdef, eva, skill, alive):
        self.name = name
        self.hp = hp                # hit points
        self.mp = mp                # magic points
        self.pattk = pattk          # physical attack
        self.mattk = mattk          # magic attack
        self.pdef = pdef            # physical defense
        self.mdef = mdef            # magic defense
        self.eva = eva              # evasion
        self.skill = skill          # special skill/ability
        self.alive = alive          # bool/is the hero above 0 HP


# Basic heroes

# // stat ranges //
# check to prevent values from exceeding/dropping below mix/max
# how do stats scale up, how do chars level up
'''
    HP: 200 - 500                   # factor of 2.5
    MP: 10 - 50                     # factor of 5
    Physical attack: 10 - 50        # factor of 5
    Magic attack: 10 - 50           # factor of 5
    Physical defense: 10 - 50       # factor of 5
    Magic defense: 5 - 25           # factor of 5
    Evasion: 5 - 25                 # factor of 5 
'''

hero_warrior = Hero("Warrior", 350, 10, 30, 10, 50, 10, 10, "Blade Rush", True)
'''
    Blade Rush: three-fold attack with chance of critical hits (multiple targets)
'''

hero_monk = Hero("Monk", 500, 20, 35, 30, 40, 15, 25, "Focus", True)
'''
    Focus: doubles attack and ensures next attack is 100% accurate
'''

hero_blackmage = Hero("Black Mage", 200, 50, 10, 50, 10, 20, 15, "Fireball", True)
'''
    Fireball: a flaming sphere that has the chance to burn for an additional turn"
'''

hero_lancer = Hero("Lancer", 265, 15, 50, 15, 25, 10, 20, "Lunge", True)
'''
    Lunge: a low accuracy attack that causes critical damage
'''

hero_whitemage = Hero("White Mage", 250, 40, 15, 35, 20, 25, 15, "Cure", True)
'''
    Cure: recovers HP for an ally
'''


