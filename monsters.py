# Monster boilerplate object
class Monster:
    def __init__(self, name, hp, mp, pattk, mattk, pdef, mdef, eva, alive):
        self.name = name
        self.hp = hp                # hit points
        self.mp = mp                # magic points
        self.pattk = pattk          # physical attack
        self.mattk = mattk          # magic attack
        self.pdef = pdef            # physical defense
        self.mdef = mdef            # magic defense
        self.eva = eva              # evasion
        self.alive = alive          # bool/is the monster above 0 HP


# Some introductory mobs
# Descriptions can be used in some future manner

# // stat ranges //
# check to prevent values from exceeding/dropping below mix/max
# stats scale with heroes levels?
'''
    HP: 200 - 5000                  # factor of 25
    MP: 10 - 250                    # factor of 25
    Physical attack: 20 - 200       # factor of 10
    Magic attack: 5 - 50            # factor of 10
    Physical defense: 100 - 500     # factor of 5
    Magic defense: 50 - 250         # factor of 5
    Evasion: 5 - 25                 # factor of 5
'''

# Orc
monster_orc = Monster("Orc", 550, 20, 50, 10, 200, 70, 10, True)
'''
    Dominating hilly grasslands near and far, the orc is a formidable brute of a foe.
    Orcs are mostly physical creatures, but have been known to cast minor magic.
'''

# Goblin
monster_goblin = Monster("Goblin", 300, 35, 35, 20, 150, 80, 25, True)
'''
    Hailing from rocky, mountainous areas, goblins are fierce tricksters.
    Goblins have high evasion, but low defenses.
'''

# Serpent
monster_serpent = Monster("Serpent", 1250, 100, 75, 35, 250, 110, 15, True)
'''
    Mystical creatures birthed from the elements, serpents are rarely found throughout the world.
    Serpents have high HP and wield powerful magic and attack. 
'''

# Troll
monster_troll = Monster("Troll", 1000, 10, 75, 5, 350, 50, 5, True)
'''
    Residing primarily in forests and caves, trolls are intimidating in stature.
    Trolls have high defense, but aren't too smart when it comes to the arcane arts.
'''

# Ghoul
monster_ghoul = Monster("Ghoul", 350, 100, 30, 40, 300, 60, 20, True)
'''
    Undead effigies of anger and despair, some say ghouls are former magicians bound to life through death.
    Ghouls use potent magical abilities, but their greatest strength is also their weakness.
'''

# Mimic
# Starts as a monster with all lowest possible stats
# Will either die from one attack or transform into a random other monster
# Random choice physical or magical attack at start of battle, 25/75
monster_mimic = Monster("Mimic", 200, 10, 20, 5, 100, 50, 5, True)
'''
    A seeming blob of loosely held together matter and organic material.
    The mimic's origin and purpose of existence are unknown.
'''

# Boss-type classes

# Moroz
# means "frost" in Russian
# should be weak to fire (are there weaknesses yet?)
monster6 = Monster("Moroz", 3500, 200, 130, 400, 375, 180, 25, True)
'''
    The shade of an ancient sorcerer, twisted and frozen.
    Wields the most powerful magic known, with only one presumed weakness...
'''

# Behemoth
# max stats
monster_behemoth = Monster("Behemoth", 5000, 250, 200, 50, 500, 250, 50, True)
'''
    Claimed to be the king of all beasts.
    It's legend prevails through ages-old word-of-mouth.
    Believed to slumber in a cave atop the highest peak.
    This creature is found in records pre-dating modern civilization.
'''

