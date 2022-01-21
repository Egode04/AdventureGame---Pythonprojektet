import math
import random as rand
import colorFontBg as color
import Items as item
import winsound
import time
import sys
import os

#--------------------------------------- Songs --------------------------------------------#
def playBackgroundSound(song):
    songs = [".\\songs\\NarutoFightingSong.wav", ".\\songs\\NarutoBattleSong.wav", ".\\songs\\StayWIthMe_1nonly.wav", ".\\songs\\UniversalCollapse.wav", ".\\songs\\TinyLittleAdiantum.wav", ".\\songs\\CalmTavern.wav"]
    if song == "fight":
        r = songs[0]
    elif song == "battle":
        r = songs[1]
    elif song == "1nonly":
        r = songs[2]
    elif song == "boss":
        r = songs[3]
    elif song == "uwu_1":
        r = songs[4]
    elif song == "Calm Tavern":
        r = songs[5]
    winsound.PlaySound(r, winsound.SND_ASYNC)

def stopBackgroundSound():
    winsound.PlaySound(None, winsound.SND_ASYNC)

#------------------------------------ Player Class --------------------------------------#

class Player(object):
    name = str()
    LVL = int() # level
    DSP = int(6) # default stat points
    SP = int() # stat points
    AD = int(2) # attack damage
    HP = int(8) # hit points
    RS = int(2) # reaction speed
    SET = bool() # set stats or random stats
    MAX_HP = int()
    XP = int(0) # xp amount
    DXPB = int(9) # Default XP Bonus
    
    weapon = 'Stick'
    armor = 'Light Robe'
    artifact = 'Bag of Dust'

    SLOT1 = None
    SLOT2 = None
    SLOT3 = None
    QUIVER = [] # 32 Arrows Max

    weaponBonus = [int(0), int(0), int(0)]
    armorBonus = [int(0), int(0), int(0)]
    artifactBonus = [int(0), int(0), int(0)]

    potionBonusStrength = float(1)
    potionBonusSpeed = float(1)

    def set_name(self):
        self.name = str(input(f"Enter Your {color.yellow}Name{color.end}: "))
    
    def set_lvl(self, lvl):
        self.LVL = lvl

        if self.LVL < 1:
            print("    Level cannot be lower than 1!")
            self.LVL = int(input("Set Your Start Level: "))
            if self.LVL < 1:
                self.LVL = 1
                print("    Start Level Set to 1!")
    
    def set_SP(self):
        self.SP = 3 * self.LVL + self.DSP
    
    def ad_SP(self):
        self.SP += self.DSP
    
    def set_MAX_HP(self):
        self.MAX_HP = self.HP
    
    def setOrRand(self, set):
        if set == 1:
            self.SET = True
        else:
            self.SET = False
    
    def show_stats(self):
        itemBonus()
        if self.SET:
            print(f"""
    You Have {color.blue}{self.SP} Stat Points{color.end} to Use!
        {color.red}Attack Damage: {self.AD}
        {color.pink}Hit Points: {self.HP} / {self.MAX_HP}
        {color.aqua}Reaction Speed: {self.RS}{color.end}
            """)
        else:
            print(f"""
    You Have {color.blue}{self.SP} Stat Points{color.end}!
        {color.red}Attack Damage: {self.AD}
        {color.pink}Hit Points: {self.HP} / {self.MAX_HP}
        {color.aqua}Reaction Speed: {self.RS}{color.end}
            """)
    
    def show_stats_only(self):
        itemBonus()
        if self.SET:
            print(f"""
        {color.pink}Hit Points: {self.HP} / {self.MAX_HP}
        {color.red}Attack Damage: {self.AD}
        {color.aqua}Reaction Speed: {self.RS}{color.end}
            """)
        else:
            print(f"""
        {color.pink}Hit Points: {self.HP} / {self.MAX_HP}
        {color.red}Attack Damage: {self.AD}
        {color.aqua}Reaction Speed: {self.RS}{color.end}
            """)

    def setOrRand_stats(self):
        player.show_stats()
        if self.SET:
            continueLoop = True
            while continueLoop:
                ad = int(input("Add SP to Attack Damage: ")) # in range(0, SP)
                if ad < 0:
                    typing("""
    You Cannot Add Less Than 0 SP to Your Attack Damage!
""", 1)
                    continue
                elif ad > self.SP:
                    typing(f"""
    You Cannot Add More Than {self.SP} SP to Your Attack Damage!
""", 1)
                    continue
                self.AD += ad
                self.SP -= ad
                clear(0.1)
                player.show_stats()
                break

            while continueLoop:
                hp = int(input("Add SP to Hit Points: ")) # in range(0, SP)
                if hp < 0:
                    typing("""
    You Cannot Add Less Than 0 SP to Your Hit Points!
""", 1)
                    continue
                elif hp > self.SP:
                    typing(f"""
    You Cannot Add More Than {self.SP} SP to Your Hit Points!
""", 1)
                    continue
                self.HP += hp
                self.SP -= hp
                player.set_MAX_HP()
                clear(0.1)
                player.show_stats()
                break
                
            while continueLoop:
                rs = int(input("Add SP to Reaction Speed: ")) # in range(0, SP)
                if rs < 0:
                    typing("""
    You Cannot Add Less Than 0 SP to Your Reaction Speed!
""", 1)
                    continue
                elif rs > self.SP:
                    typing(f"""
    You Cannot Add More Than {self.SP} SP to Your Reaction Speed!
""", 1)
                    continue
                self.RS += rs
                self.SP -= rs
                clear(0)
                player.show_stats()
                break
        else:
            ead, ehp, ers = 0, 0, 0
            while self.SP > 0:
                randAD = rand.randint(0, self.SP)
                self.AD += randAD
                self.SP -= randAD
                ead += randAD

                randHP = rand.randint(0, self.SP)
                self.HP += randHP
                self.SP -= randHP
                ehp += randHP
                
                randRS = rand.randint(0, self.SP)
                self.RS += randRS
                self.SP -= randRS
                ers += randRS
            player.set_MAX_HP()

            clear(0)
            print(f"""
    {color.blue}SP{color.end} Added to {color.blue}Stats{color.end}:
        {color.red}Attack Damage{color.end}: +{color.red}{ead}{color.end}
        {color.pink}Hit Points{color.end}: +{color.pink}{ehp}{color.end}
        {color.aqua}Reaction Speed{color.end}: +{color.aqua}{ers}{color.end}
            """)
            pause()
            player.show_stats()

#---------------------------------- Monster Class ---------------------------------------#

class Monster(object):
    type = str()
    LVL = int()
    AD = int(2)
    HP = int(8)
    RS = int(2)
    SP = int()
    DSP = int(3)
    MAX_HP = int()

    # The Monster's Weapon
    weapon = str()

    # List of Different Races
    monsterTypes = ["Skeleton", "Zombie", "Slime"]

    def newMonster(self):
        self.AD = int(2)
        self.HP = int(8)
        self.RS = int(1)
        self.MAX_HP = int(self.HP)

        MinimumMonsterLVL = player.LVL-2
        if MinimumMonsterLVL < 1:
            MinimumMonsterLVL = 1

        self.SP = 3 * self.LVL + self.DSP
        self.LVL = rand.randint(MinimumMonsterLVL, player.LVL+1)
        self.type = rand.choice(monster.monsterTypes)

        while self.SP > 0:
            rad = rand.randint(0, self.SP)
            self.AD += rad
            self.SP -= rad
            rhp = rand.randint(0, self.SP)
            self.HP += rhp
            self.SP -= rhp
            rrs = rand.randint(0, self.SP)
            self.RS += rrs
            self.SP -= rrs
        self.MAX_HP = self.HP

        self.weapon = rand.choice(item.weapons)
    
    def monsterStats(self):
        print(f"""
    Level {self.LVL} {color.light_red}{self.type}{color.end}:
        {color.red}Attack Damage{color.end}: {color.red}{self.AD}{color.end}
        {color.pink}Hit Points{color.end}: {color.pink}{self.HP}{color.end} / {color.pink}{self.MAX_HP}{color.end}
        {color.aqua}Reaction Speed{color.end}: {color.aqua}{self.RS}{color.end}      
""")
    
    def gainXP(self):
        # xp = monster.LVL ** 2 + 2
        addXP = monster.LVL ** 2 + 2
        player.XP += addXP
        typing(f"""
    You {color.light_yellow}Gain{color.end} {color.aqua}{addXP} Experience Points{color.end}!
""", 1)
        LvlUp()
        pause()
    
    def gainXPfromItem(self):
        # xp = monster.LVL ** 2 + 2
        addXP = player.LVL * 2 + 3
        player.XP += addXP
        typing(f"""
    You {color.light_yellow}Gain{color.end} {color.aqua}{addXP} Experience Points{color.end}!
""", 1)
        LvlUp()
        pause()

#------------------ Text Interactions / Dialogs -----------------------#

intro1 = f"""
Welcome New {color.green}Adventurer{color.end}!
My Name is {color.yellow}Athena{color.end} and I am Going to {color.light_yellow}Guide{color.end} You Through Your {color.green}Adventure{color.end}!
What is Your {color.yellow}Name{color.end}?
    """
intro2 = f"""
There are Two Different Ways To Define Your {color.pink}Ability Scores{color.end}!
{color.blue}Number 1{color.end}:
    You Can {color.aqua}Select{color.end} Your {color.pink}Stats{color.end} by Choosing the Amount of {color.pink}Points{color.end} to Set to Your {color.pink}Abilities{color.end},
{color.blue}Number 2{color.end}:
    You Can Also Let Me {color.yellow}(Athena){color.end} {color.aqua}Randomly Select{color.end} Your {color.pink}Abilities{color.end}!
Please Select How You Want to Build Your {color.pink}Stats{color.end}!
    """
intro3 = f"""
Your {color.pink}Character Info{color.end} and {color.pink}Stats{color.end} are Stored in Your {color.pink}Character Sheet{color.end}!
You Can Access Your {color.pink}Character Sheet{color.end} From the {color.red}Menu{color.end}!
I Will Show You How it Looks Before We Move on! 
    """

# Creating New Monster
monster = Monster()

# Setting New Stats to Monster
def newMonster():
    monster.newMonster()

# Character Setup
player = Player()
def characterSetup():
    clear(0)
    if tutYesNo:
        typing(intro1, 2) # 4
    player.set_name()
    clear(0.1)
    if tutYesNo:
        typing(f"""
{color.yellow}{player.name}{color.end} Was it?
Nice to Meet You {color.yellow}{player.name}{color.end}!
What is Your Current {color.green}Level{color.end}?
    """, 2) # 5
    player.set_lvl(int(input(f"Enter The {color.green}Level{color.end} You Want to {color.pink}Start On{color.end}: ")))
    player.set_SP()
    clear(0)
    if tutYesNo:
        typing(intro2, 2) # 3
    player.setOrRand(int(input(f"{color.pink}Set Stats (1){color.end} or {color.pink}Random Stats (2){color.end}: ")))
    clear(0.1)
    player.setOrRand_stats()
    xpToLvlUp()

#---------------------- Adding weapon, armor & artifact bonus -----------------------------#

def weaponBonus():
    player.AD -= player.weaponBonus[0]
    player.HP -= player.weaponBonus[1]
    player.RS -= player.weaponBonus[2]
    if player.weapon == 'Longsword':
        player.weaponBonus = [3, 0, -1]
    elif player.weapon == 'Shortsword':
        player.weaponBonus = [2, 0, 0]
    elif player.weapon == 'Dagger':
        player.weaponBonus = [1, 0, 1]
    elif player.weapon == 'Bow':
        if len(player.QUIVER) > 0:
            player.weaponBonus = [4, 0, -1]
        else:
            player.weaponBonus = [0, 0, 0]
    player.AD += player.weaponBonus[0]
    player.HP += player.weaponBonus[1]
    player.RS += player.weaponBonus[2]

def armorBonus():
    player.AD -= player.armorBonus[0]
    player.HP -= player.armorBonus[1]
    player.RS -= player.armorBonus[2]
    if player.armor == 'Plate Armor':
        player.armorBonus = [0, 10, -1]
    elif player.armor == 'Padded Leather Armor':
        player.armorBonus = [0, 6, 0]
    elif player.armor == 'Assassins Robe':
        player.armorBonus = [-1, 0, 4]
    player.AD += player.armorBonus[0]
    player.HP += player.armorBonus[1]
    player.RS += player.armorBonus[2]

def artifactBonus():
    player.AD -= player.artifactBonus[0]
    player.HP -= player.artifactBonus[1]
    player.RS -= player.artifactBonus[2]
    if player.artifact == 'Red Gem':
        player.artifactBonus = [3, 1, 0]
    elif player.artifact == 'Green Gem':
        player.artifactBonus = [0, 4, 0]
    elif player.artifact == 'Blue Gem':
        player.artifactBonus = [1, 0, 3]
    elif player.artifact == 'Purple Gem':
        player.artifactBonus = [2, 3, 2]
    player.AD += player.artifactBonus[0]
    player.HP += player.artifactBonus[1]
    player.RS += player.artifactBonus[2]

def itemBonus():
    player.MAX_HP -= player.weaponBonus[1] + player.armorBonus[1] + player.artifactBonus[1]
    weaponBonus()
    armorBonus()
    artifactBonus()
    player.MAX_HP += player.weaponBonus[1] + player.armorBonus[1] + player.artifactBonus[1]

# XP to Level Up
def xpToLvlUp():
    global MAX_XP
    MAX_XP = player.LVL**3 + player.DXPB

def LvlUp():
    while player.XP >= MAX_XP:
        player.LVL += 1
        player.XP -= MAX_XP
        xpToLvlUp()
        statsUpOnLvlUp()

# Stats Up on Level Up
def statsUpOnLvlUp():
    player.ad_SP()
    typing(f"""
    Congratulations!
    {color.yellow}{player.name}{color.end} Has Reached {color.aqua}Level {player.LVL}{color.end}!
    You Now Have {color.pink}{player.SP} Stat Points{color.end}!
""", 2)
    statsUp()

# Adding the Stats
def statsUp():
    print(f"""
    You Have {color.blue}{player.SP} Stat Points{color.end} to Use!
        {color.red}Attack Damage: {player.AD}
        {color.pink}Hit Points: {player.HP} / {player.MAX_HP}
        {color.aqua}Reaction Speed: {player.RS}{color.end}
            """)
    while player.SP > 0:
        try:
            ad = int(input(f"SP to add to {color.pink}Attack Damage{color.end}: "))
            if ad > player.SP:
                typing(f"""
    {color.red}You Cannot add More Than {player.SP} SP to Your Stats!{color.end}
""", 2)
                continue
            elif ad < 0:
                typing(f"""
    {color.red}You Cannot add Negative SP to Your Stats!{color.end}
""", 1)
                continue
            else:
                player.AD += ad
                player.SP -= ad
        except:
            typing(f"{color.red}Invalid Input!{color.end}", 1)
            continue

        player.show_stats()
        try:
            hp = int(input(f"SP to add to {color.pink}Hit Points{color.end}: "))
            if hp > player.SP:
                typing(f"""
    {color.red}You Cannot add More Than {player.SP} SP to Your Stats!{color.end}
""", 2)
                continue
            elif hp < 0:
                typing(f"""
    {color.red}You Cannot add Negative SP to Your Stats!{color.end}
""", 1)
                continue
            else:
                player.HP += hp
                player.MAX_HP += hp
                player.SP -= hp
        except:
            typing(f"{color.red}Invalid Input!{color.end}", 1)
            continue

        player.show_stats()
        try:
            rs = int(input(f"SP to add to {color.pink}Reaction Speed{color.end}: "))
            if rs > player.SP:
                typing(f"""
    {color.red}You Cannot add More Than {player.SP} SP to Your Stats!{color.end}
""", 2)
                continue
            elif rs < 0:
                typing(f"""
    {color.red}You Cannot add Negative SP to Your Stats!{color.end}
""", 1)
                continue
            else:
                player.RS += rs
                player.SP -= rs
        except:
            typing(f"{color.red}Invalid Input!{color.end}", 1)
            continue

# Character Sheet
def charSheet(lvlup):
    itemBonus()
    clear(0)
    print(f"""
    Character Sheet:
        {color.green}Level {player.LVL} {color.red}Adventurer
        {color.yellow}Character Name: {player.name}
        {color.aqua}Experience: {player.XP} / {lvlup}{color.end}""")
    player.show_stats_only()

def typing(str, speed):
    for char in str:
        sys.stdout.write(char)
        sys.stdout.flush()
        if speed == "none":
            wait(5/1000)
        else:
            wait(rand.randint(speed, speed*3)/100)

#------------------ Clear Terminal, Wait, Pause ---------------------#

def clear(delay):
    wait(delay)
    os.system('cls')

def wait(duration):
    time.sleep(duration)

def pause():
    input(f"""
    Press {color.green}Enter{color.end} to Continue: """)
    clear(0)

# Go Through Tutorial or Not
def tutorial(tut):
    while True:
        if tut.lower() == "y":
            return True
        elif tut.lower() == "n":
            return False
        else:
            typing(f"""{color.red}Invalid Input!{color.end}
""", 1)
        tut = input(f"Tutorial [{color.green}Y{color.end}/{color.red}N{color.end}]: ")

clear(0)
tutYesNo = tutorial(input(f"Tutorial [{color.green}Y{color.end}/{color.red}N{color.end}]: "))

#------------------------- Attack Setup: Reaction Speed Difference, Attack -----------------------#
def RSDiff():
    itemBonus()
    if math.floor(player.RS * player.potionBonusSpeed) > monster.RS:
        firstStrike = True
    elif math.floor(player.RS * player.potionBonusSpeed) == monster.RS:
        firstStrike = None
    else:
        firstStrike = False
    
    return firstStrike

def attacking():
    firstStrike = RSDiff()
    if firstStrike == True: # Player attacks first
        damage(True)
        if len(player.QUIVER) > 0:
            if player.weapon == "Bow":
                s = ""
                if len(player.QUIVER) == 1:
                    s = "s"
                player.QUIVER.pop()
                typing(f"""
    You Shoot the {color.light_red}{monster.type}{color.end} With Your {color.green}{player.weapon}{color.end} and You Deal {color.red}{math.floor(player.AD * player.potionBonusStrength)} Damage{color.end}!
    You Now Have {color.light_pink}{len(player.QUIVER)} Arrow{s}{color.end} Left!
""", 2)
        else:
            typing(f"""
    You Attack the {color.light_red}{monster.type}{color.end} With Your {color.green}{player.weapon}{color.end} and You Deal {color.red}{math.floor(player.AD * player.potionBonusStrength)} Damage{color.end}!
""", 2)
        monster.monsterStats()
        pause()
        if monster.HP > 0:
            damage(False)
            typing(f"""
        The {color.light_red}{monster.type}{color.end} Attacks You With it's {color.green}{monster.weapon}{color.end} and Deals {color.red}{monster.AD} Damage{color.end}!
    """, 2)
            player.show_stats_only()
            pause()
            if player.HP <= 0:
                typing(f"""
    {color.red}You Have Died!{color.end}
""", 5)
                pause()
                viewCharacter()
                raise Exception(f"{color.red}You Have Died!{color.end}")
        else:
            typing(f"""
    You Have {color.light_yellow}Slayed{color.end} the {color.light_red}{monster.type}{color.end}!
""", 2)
            monster.gainXP()

    else: # Monster attacks first
        damage(False)
        typing(f"""
    The {color.light_red}{monster.type}{color.end} Attacks You With it's {color.green}{monster.weapon}{color.end} and Deals {color.red}{monster.AD} Damage{color.end}!
""", 2)
        player.show_stats_only()
        pause()

        if player.HP > 0:
            damage(True)
            typing(f"""
    You Attack the {color.light_red}{monster.type}{color.end} With Your {color.green}{player.weapon}{color.end} and You Deal {color.red}{math.floor(player.AD * player.potionBonusStrength)} Damage{color.end}!
""", 2)
            monster.monsterStats()
            pause()
            if monster.HP <= 0:
                typing(f"""
    You Have {color.light_yellow}Slayed{color.end} the {color.light_red}{monster.type}{color.end}!
""", 2)
                monster.gainXP()
        else:
            typing(f"""
    {color.red}You Have Died!{color.end}
""", 5)
            pause()
            # NEW ERROR
            raise Exception(f"{color.red}You Have Died!{color.end}")


def attackSetup(): # Needed
    itemBonus()
    RSDiff()
    attacking()

# Healing
def healing(modifier):
    itemBonus()
    if player.HP < player.MAX_HP:
        heal = rand.randint(math.floor(player.MAX_HP/(modifier * 2)), math.floor(player.MAX_HP/modifier))
        if player.HP + heal <= player.MAX_HP:
            player.HP += heal
        else:
            heal -= player.HP + heal - player.MAX_HP
            player.HP += heal
        
        typing(f"""
    You {color.light_yellow}Recive {color.pink}{heal} Health Points{color.end}!
    You Now Have {color.pink}{player.HP}{color.end}/{color.pink}{player.MAX_HP} Health Points{color.end}!
""", 2)
        pause()
    else:
        typing(f"""
    You Already Have {color.pink}Full Health{color.end}!
    {color.pink}{player.HP}{color.end}/{color.pink}{player.MAX_HP} Health Points{color.end}!
""", 2)
        pause()

#---------------------------- Finding Equipment in Chests ------------------------#

def openChest():
    # List of Different Chests You Can Find
    chestTypes = [f"{color.pink}Weapon Chest{color.end}", f"{color.pink}Armor Chest{color.end}", f"{color.pink}Artifact Chest{color.end}", f"{color.pink}Item Chest{color.end}"]

    # Defines Which Type of Chest You Found
    chestType = rand.choice(chestTypes)
    if chestType == chestTypes[0]:
        selectedItem = rand.choice(item.chestWeapons)
    elif chestType == chestTypes[1]:
        selectedItem = rand.choice(item.chestArmors)
    elif chestType == chestTypes[2]:
        selectedItem = rand.choice(item.chestArtifacts)
    elif chestType == chestTypes[3]:
        selectedItem = rand.choice(item.chestItems)
    
    # Adds a "n" after the a If the Chest Starts With a Vocal
    if chestType == chestTypes[0]:
        n = ""
    else:
        n = "n"
    
    # Makes the SelectedItem Plural If We Find Arrows
    if selectedItem == "Arrow":
        s = "s"
    else:
        s = ""
    
    typing(f"""
    You Found a{n} {chestType} Containing {color.light_pink}{selectedItem}{s}{color.end}!
""", 3)

    if selectedItem == player.weapon:
        typing(f"""
    You Already Have {color.light_pink}{selectedItem}{color.end}!
    Here are Some {color.aqua}Experience Points{color.end} Instead!
""", 2)
        monster.gainXPfromItem()
    else:
        # Asks If We Want to Equip the New Weapon If We Find a Weapon Chest
        if chestType == chestTypes[0]:
            while True:
                changeWeapon = str(input(f"Do You Want to {color.light_yellow}Replace {color.pink}{player.weapon}{color.end} With the {color.light_pink}{selectedItem}{color.end} [{color.green}Y{color.end}/{color.red}N{color.end}]: "))
                if changeWeapon.lower() == "y":
                    typing(f"""
        {color.pink}{player.weapon}{color.end} Has Been {color.light_yellow}Replaced{color.end} With {color.light_pink}{selectedItem}{color.end}!
        """, 2)
                    player.weapon = selectedItem
                    break
                elif changeWeapon.lower() == "n":
                    typing(f"""
            You {color.light_yellow}Decide{color.end} You {color.light_red}Don't{color.end} Need the {color.light_pink}{selectedItem}{color.end} so You {color.light_yellow}Leave{color.end} it Behind!
        """, 2)
                    break
                else:
                    typing(f"""
            {color.red}Invalid Input!{color.end}
        """, 1)

    if selectedItem == player.armor:
        typing(f"""
    You Already Have {color.light_pink}{selectedItem}{color.end}!
    Here are Some {color.aqua}Experience Points{color.end} Instead!
""", 2)
        monster.gainXPfromItem()
    else:
        # Asks If We Want to Equip the New Armor If We Find an Armor Chest
        if chestType == chestTypes[1]:
            while True:
                changeArmor = str(input(f"Do You Want to {color.light_yellow}Replace{color.end} {color.pink}{player.armor}{color.end} With {color.light_pink}{selectedItem}{color.end} [{color.green}Y{color.end}/{color.red}N{color.end}]: "))
                if changeArmor.lower() == "y":
                    typing(f"""
        {color.pink}{player.armor}{color.end} Has Been {color.light_yellow}Replaced{color.end} With {color.light_pink}{selectedItem}{color.end}!
        """, 2)
                    player.armor = selectedItem
                    break
                elif changeArmor.lower() == "n":
                    typing(f"""
            You {color.light_yellow}Decide{color.end} You {color.light_red}Don't{color.end} Need the {color.light_pink}{selectedItem}{color.end} so You {color.light_yellow}Leave{color.end} it Behind!
        """, 2)
                    break
                else:
                    typing(f"""
            {color.red}Invalid Input!{color.end}            
        """, 1)

    if selectedItem == player.artifact:
        typing(f"""
    You Already Have {color.light_pink}{selectedItem}{color.end}!
    Here are Some {color.aqua}Experience Points{color.end} Instead!
""", 2)
        monster.gainXPfromItem()
    else:
        # Asks If We Want to Equip the New Artifact If We Find an Artifact Chest
        if chestType == chestTypes[2]:
            while True:
                changeArtifact = str(input(f"Do You Want to {color.light_yellow}Replace {color.pink}{player.artifact}{color.end} With {color.light_pink}{selectedItem}{color.end} [{color.green}Y{color.end}/{color.red}N{color.end}]: "))
                if changeArtifact.lower() == "y":
                    typing(f"""
        {color.pink}{player.artifact}{color.end} Has Been {color.light_yellow}Replaced{color.end} With {color.light_pink}{selectedItem}{color.end}!
        """, 2)
                    player.artifact = selectedItem
                    break
                elif changeArtifact.lower() == "n":
                    typing(f"""
            You {color.light_yellow}Decide{color.end} You {color.light_red}Don't{color.end} Need the {color.light_pink}{selectedItem}{color.end} so You {color.light_yellow}Leave{color.end} it Behind!
        """, 2)
                    break
                else:
                    typing(f"""
            {color.red}Invalid Input!{color.end}            
        """, 1)

    # If We Find Arrows in the Item Chest
    #   Adds a Random Between 6 and 12 Amount of selectedItem
    # Else If the Quiver is Full
    #   Does Not Add Arrows to the Quiver
    # Else If We Find Any Other Item
    #   If We Already Have 3 Items in the Item Slots
    #       Ask Which Slot We Want to Replace With the New Item, (1), (2), (3) or None
    #   Else If We Have Any Slot Free
    #       Adds the New Item in the Free Slot
    if chestType == chestTypes[3]:
        if selectedItem == "Arrow":
            quiver = len(player.QUIVER)
            if quiver < 32:
                arrows = rand.randint(6, 12)
                x = 0
                while x < arrows:
                    quiver = len(player.QUIVER)
                    if quiver < 32:
                        player.QUIVER.append(item.items[4])
                    else:
                        arrows -= 1
                    x += 1
                
                if arrows == 1:
                    s = ""
                else:
                    s = "s"
                typing(f"""
    {color.light_pink}{arrows} Arrow{s}{color.end} Has Been {color.light_yellow}Added{color.end} to Your {color.pink}Quiver{color.end}!
""", 2)
            else:
                typing(f"""
    Your {color.pink}Quiver{color.end} is {color.light_red}Full{color.end}!                
""", 2)
        else:
            if player.SLOT1 and player.SLOT2 and player.SLOT3 != None:
                typing(f"""
    {color.light_yellow}Select{color.end} the {color.pink}Item{color.end} You Want to {color.light_yellow}Replace{color.end}:
""", 2)
                print(f"""
        {color.pink}Slot 1{color.end}: {color.light_yellow}{player.SLOT1}{color.end}
        {color.pink}Slot 2{color.end}: {color.light_yellow}{player.SLOT2}{color.end}
        {color.pink}Slot 3{color.end}: {color.light_yellow}{player.SLOT3}{color.end}
""")
                while True:
                    replaceItem = str(input(f"{color.light_pink}(1){color.end}, {color.light_pink}(2){color.end}, {color.light_pink}(3){color.end} or {color.red}None{color.end}: "))
                    if replaceItem == "1" or "2" or "3":
                        break
                    elif replaceItem.lower() == "none":
                        break
                    else:
                        typing(f"""
    {color.red}Invalid Input!{color.end}
""", 1)
                
                if replaceItem == "1":
                    player.SLOT1 = selectedItem
                    typing(f"""
    {color.light_pink}{selectedItem}{color.end} Has Been {color.light_yellow}Added{color.end} to Your {color.pink}Inventory{color.end} in {color.pink}Item Slot {color.light_yellow}1{color.end}!
""", 2)
                elif replaceItem == "2":
                    player.SLOT2 = selectedItem
                    typing(f"""
    {color.light_pink}{selectedItem}{color.end} Has Been {color.light_yellow}Added{color.end} to Your {color.pink}Inventory{color.end} in {color.pink}Item Slot {color.light_yellow}2{color.end}!
""", 2)
                elif replaceItem == "3":
                    player.SLOT3 = selectedItem
                    typing(f"""
    {color.light_pink}{selectedItem}{color.end} Has Been {color.light_yellow}Added{color.end} to Your {color.pink}Inventory{color.end} in {color.pink}Item Slot {color.light_yellow}3{color.end}!
""", 2)
                else:
                    typing(f"""
    You {color.light_yellow}Decide{color.end} You {color.light_red}Don't{color.end} Need the {color.light_pink}{selectedItem}{color.end} so You {color.light_yellow}Leave{color.end} it Behind!
""", 2)
            elif player.SLOT1 and player.SLOT2 != None:
                player.SLOT3 = selectedItem
                typing(f"""
    {color.light_pink}{selectedItem}{color.end} Has Been {color.light_yellow}Added{color.end} to Your {color.pink}Inventory{color.end} in {color.pink}Item Slot {color.light_yellow}3{color.end}!
""", 2)
            elif player.SLOT1 != None:
                player.SLOT2 = selectedItem
                typing(f"""
    {color.light_pink}{selectedItem}{color.end} Has Been {color.light_yellow}Added{color.end} to Your {color.pink}Inventory{color.end} in {color.pink}Item Slot {color.light_yellow}2{color.end}!
""", 2)
            else:
                player.SLOT1 = selectedItem
                typing(f"""
    {color.light_pink}{selectedItem}{color.end} Has Been {color.light_yellow}Added{color.end} to Your {color.pink}Inventory{color.end} in {color.pink}Item Slot {color.light_yellow}1{color.end}!
""", 2)
    itemBonus()

#-------------------------------- Setup Character ---------------------------#
# Starts the Background Music
playBackgroundSound("Calm Tavern")
characterSetup()
clear(0)
if tutYesNo:
    typing(intro3, 2)
    pause()
    charSheet(MAX_XP)
    pause()

# Find the Campfire
def findCampfire():
    typing(f"""
    You Have {color.light_yellow}Found{color.end} a {color.yellow}Campfire{color.end}!
""", 2)
    while True:
        rest = str(input(f"    Would You Like to {color.light_yellow}Rest{color.end} at the {color.yellow}Campfire{color.end} to {color.light_pink}Restore{color.end} Some {color.pink}Health Points{color.end} [{color.green}Y{color.end}/{color.red}N{color.end}]: "))
        if rest.lower() == "y":
            typing(f"""
    You Recieve Some {color.pink}Health{color.end} From Resting!
""", 2)
            healing(1)
            break
        elif rest.lower() == "n":
            clear(0.1)
            typing(f"""
    You {color.light_yellow}Deside{color.end} That You {color.light_red}Don't{color.end} Feel Tired and You {color.light_yellow}Continue{color.end} to Walk...
""", 2)
            break
        else:
            typing(f"""
    {color.red}Invalid Input!{color.end}
""", "none")
    itemBonus()

#---------------------------- View Character and Inventory -------------------------#
def showInventory():
    s = "s"
    if len(player.QUIVER) == 1:
        s = ""
    clear(0)
    typing(f"""
Player {color.pink}Inventory{color.end}:

    {color.pink}Equipment{color.end}:
        {color.pink}Weapon{color.end}: {color.light_red}{player.weapon}{color.end}
        {color.pink}Armor{color.end}: {color.light_green}{player.armor}{color.end}
        {color.pink}Artifact{color.end}: {color.light_aqua}{player.artifact}{color.end}

    Accessible {color.pink}Items{color.end}:
        {color.pink}Slot 1{color.end}: {color.light_yellow}{player.SLOT1}{color.end}
        {color.pink}Slot 2{color.end}: {color.light_yellow}{player.SLOT2}{color.end}
        {color.pink}Slot 3{color.end}: {color.light_yellow}{player.SLOT3}{color.end}
        {color.pink}Quiver{color.end}: {color.light_yellow}{len(player.QUIVER)}{color.end} {color.light_pink}Arrow{s}{color.end}

""", 1)
    pause()

def printInventory():
    s = "s"
    if len(player.QUIVER) == 1:
        s = ""
    clear(0)
    print(f"""
Player {color.pink}Inventory{color.end}:

    {color.pink}Equipment{color.end}:
        {color.pink}Weapon{color.end}: {color.light_red}{player.weapon}{color.end}
        {color.pink}Armor{color.end}: {color.light_green}{player.armor}{color.end}
        {color.pink}Artifact{color.end}: {color.light_aqua}{player.artifact}{color.end}

    Accessible {color.pink}Items{color.end}:
        {color.pink}Slot 1{color.end}: {color.light_yellow}{player.SLOT1}{color.end}
        {color.pink}Slot 2{color.end}: {color.light_yellow}{player.SLOT2}{color.end}
        {color.pink}Slot 3{color.end}: {color.light_yellow}{player.SLOT3}{color.end}
        {color.pink}Quiver{color.end}: {color.light_yellow}{len(player.QUIVER)}{color.end} {color.light_pink}Arrow{s}{color.end}

""")

def viewCharacter():
    itemBonus()
    clear(0)
    typing(f"""
{color.yellow}{player.name}{color.end}:
    {color.green}Level {player.LVL}{color.end}
    {color.aqua}Experience{color.end}: {player.XP} / {MAX_XP}
    Player {color.pink}Stats{color.end}:
        {color.pink}Health{color.end}: {player.HP} / {player.MAX_HP}
        {color.pink}Attack{color.end}: {player.AD}
        {color.pink}Speed{color.end}: {player.RS}
""", "none")
    pause()

def printCharacter():
    itemBonus()
    clear(0)
    print(f"""
{color.yellow}{player.name}{color.end}:
    {color.green}Level {player.LVL}{color.end}
    {color.aqua}Experience{color.end}: {player.XP} / {MAX_XP}
    Player {color.pink}Stats{color.end}:
        {color.pink}Health{color.end}: {player.HP} / {player.MAX_HP}
        {color.pink}Attack{color.end}: {player.AD}
        {color.pink}Speed{color.end}: {player.RS}
""")
    pause()

# Dealing Damage
def damage(Player):
    itemBonus()
    if Player: # Player Attacks
        dmg = math.floor(player.AD * player.potionBonusStrength)
        monster.HP -= dmg
    else: # Monster Attacks
        player.HP -= monster.AD

#------------------------ Explore / Open Character Menu ------------------------------#
def firstMenu():
    while True:
        try:
            clear(0)
            m1 = str(input(f"Would You Like to {color.light_red}Explore{color.end} / {color.light_green}Open Character Menu{color.end} / {color.red}Quit{color.end} | [{color.light_red}E{color.end}/{color.light_green}M{color.end}/{color.red}Q{color.end}]: "))
            if m1.lower() == "e":
                explore()
                continue
            elif m1.lower() == "m":
                secondMenu()
                continue
            elif m1.lower() == "q":
                confirm = confirmQuit()
                if confirm == True:
                    break
                else:
                    continue
            else:
                typing(f"""
    {color.red}Invalid Input!{color.end}
""", 1)
        except:
            if player.HP > 0:
                typing(f"""
    {color.red}Invalid Input!{color.end}
""", 1)
            else:
                clear(0)
                raise Exception(f"{color.red}You Have Died!{color.end}")

#------------------------------------- View Character Sheet / View Inventory / Go Back ------------------------#
def secondMenu():
    while True:
        try:
            clear(0)
            m2 = str(input(f"""{color.light_green}Character Menu{color.end}:
    Would You Like to {color.light_aqua}View Character Sheet{color.end} / {color.light_pink}View Inventory{color.end} / {color.red}Go Back{color.end} | [{color.light_aqua}C{color.end}/{color.light_pink}I{color.end}/{color.red}B{color.end}]: """))
            if m2.lower() == "c":
                printCharacter()
                continue
            elif m2.lower() == "i":
                thirdMenu()
                continue
            elif m2.lower() == "b":
                break
            else:
                typing(f"""
    {color.red}Invalid Input!{color.end}
""", 1)
                continue

        except:
            typing(f"""
    {color.red}Invalid Input!{color.end}
""", 1)




#----------------------------- Use Item / Go Back ---------------------------------#
def thirdMenu():
    clear(0)
    printInventory()
    while True:
        try:
            clear(0)
            printInventory()
            m3 = str(input(f"Would You Like to {color.light_pink}Use Item{color.end} / {color.red}Go Back{color.end} | [{color.light_pink}U{color.end}/{color.red}B{color.end}]: "))
            if m3.lower() == "u":
                forthMenu()
                continue
            elif m3.lower() == "b":
                break
            else:
                typing(f"""
    {color.red}Invalid Input!{color.end}
""", 1)
        except:
            typing(f"""
    {color.red}Invalid Input!{color.end}
""", 1)


#----------------------------- What Item to Use: [Slot 1, Slot 2, Slot 3] ------------------------------#
def forthMenu():
    while True:
        try:
            clear(0)
            printInventory()
            m4 = str(input(f"Which {color.pink}Item{color.end} Would You like to Use | [{color.light_yellow}1{color.end}/{color.light_yellow}2{color.end}/{color.light_yellow}3{color.end}/{color.light_yellow}None{color.end}]: {color.light_yellow}"))
            color.end
            if m4 == "1":
                if player.SLOT1 != None: 
                    useItem(1)
                else:
                    typing(f"""
    There Are no {color.pink}Items{color.end} in {color.pink}Slot 1{color.end}!
""", 2)
                break
            elif m4 == "2":
                if player.SLOT2 != None: 
                    useItem(2)
                else:
                    typing(f"""
    There Are no {color.pink}Items{color.end} in {color.pink}Slot 2{color.end}!
""", 2)
                break
            elif m4 == "3":
                if player.SLOT3 != None: 
                    useItem(3)
                else:
                    typing(f"""
    There Are no {color.pink}Items{color.end} in {color.pink}Slot 3{color.end}!
""", 2)
                break
            elif m4.lower() == "none":
                break
            else:
                typing(f"""
    {color.red}Invalid Input!{color.end}
""", 1)
        except:
            typing(f"""
    {color.red}Invalid Input!{color.end}
""", 1)

# Confirm Quit or Not
def confirmQuit():
    clear(0)
    while True:
        confirm = str(input(f"Are You Sure You Would Like to {color.light_red}Quit{color.end} | [{color.red}Y{color.end}/{color.green}N{color.end}]: "))
        if confirm.lower() == "y":
            typing(f"""
    Type {color.red}Confirm Quit{color.end} to {color.light_red}Quit{color.end}!
""", 1)
            confirm2 = str(input(f"Confirm Here: {color.red}"))
            color.end
            if confirm2 == "Confirm Quit":
                return True
        elif confirm.lower() == "n":
            break
        else:
            typing(f"""
    {color.red}Invalid Input!{color.end}
""", 1)
    color.end
    clear(0)

#------------------------- Randomize events: Monster Apears, Find Chest, Find Campfire, Find Nothing... ----------------------------#
def explore():
    randEvent = []
    for i in range(0, 14):
        randEvent.append("Monster Apears")
    for i in range(0, 7):
        randEvent.append("Find Chest")
    if player.HP < player.MAX_HP:
        for i in range(0, 4):
            randEvent.append("Find Campfire")
    for i in range(0, 1):
        randEvent.append("Find Nothing")

    randomEvent = rand.choice(randEvent)

    if randomEvent == "Monster Apears":
        monsterApears()
    elif randomEvent == "Find Chest":
        openChest()
        pause()
    elif randomEvent == "Find Campfire":
        findCampfire()
    elif randomEvent == "Find Nothing":
        findNothing()

def findNothing():
    typing(f"""
    You {color.light_yellow}Walk{color.end} Into a Small Cave and You See...
""", 2)
    wait(2)
    typing(f"""
    {color.red}NOTHING AT ALL!{color.end}
""", 10)
    pause()

# Attack / Open Inventory
def battleMenu():
    global battleLoop
    battleLoop = bool(True)
    while battleLoop:
        try:
            clear(0)
            b1 = str(input(f"Would You Like to {color.red}Attack{color.end}, {color.pink}Open Inventory{color.end} or {color.light_aqua}View Character{color.end} | [{color.red}A{color.end}/{color.pink}I{color.end}/{color.aqua}C{color.end}]: "))
            if b1.lower() == "a":
                attackSetup()
            elif b1.lower() == "i":
                thirdMenu()
            elif b1.lower() == "c":
                printCharacter()
            else:
                typing(f"""
    {color.red}Invalid Input!{color.end}
""", 1)
            if monster.HP <= 0:
                break
            elif player.HP <= 0:
                break
        except:
            if player.HP > 0:
                typing(f"""
    {color.red}Invalid Input!{color.end}
""", 1)
            else:
                raise Exception(f"{color.red}You Have Died!{color.end}")

def monsterApears():
    playBackgroundSound("boss")
    newMonster()
    typing(f"""
    You Have {color.light_red}Encountered{color.end} a {color.aqua}Level {monster.LVL}{color.end} {color.red}{monster.type}{color.end}!
""", 2)
    pause()
    battleMenu()

    if player.potionBonusSpeed > float(1):
        resetAllPotions()
    elif player.potionBonusStrength > float(1):
        resetAllPotions()

    # At the End of The Function
    playBackgroundSound("Calm Tavern")

# Resets All Potion Effects
def resetAllPotions():
    # Resets Potion Effects
    player.potionBonusStrength = float(1)
    player.potionBonusSpeed = float(1)

    typing(f"""
    Your {color.blue}Potion Effects{color.end} Have Reset!
""", 2)
    pause()

# Use a Selected Item
def useItem(slot):
    if slot == 1:
        if player.SLOT1 == item.items[0]: # Use "Potion of Strength"
            player.potionBonusStrength = float(1.5)
            typing(f"""
    {color.light_yellow}Using {color.blue}{item.items[0]}{color.end}!
""", 2)
        elif player.SLOT1 == item.items[1]: # Use "Potion of Healing"
            healing(2)
            typing(f"""
    {color.light_yellow}Using {color.blue}{item.items[1]}{color.end}!
""", 2)
        elif player.SLOT1 == item.items[2]: # Use "Potion of Speed"
            player.potionBonusSpeed = float(1.5)
            typing(f"""
    {color.light_yellow}Using {color.blue}{item.items[2]}{color.end}!
""", 2)
        elif player.SLOT1 == item.items[3]: # Use "Food"
            typing(f"""
    {color.light_yellow}Using {color.light_blue}{item.items[3]}{color.end}!
""", 2)
            healing(4)
        resetSlots(1)
    elif slot == 2:
        if player.SLOT2 == item.items[0]: # Use "Potion of Strength"
            player.potionBonusStrength = float(1.5)
            typing(f"""
    {color.light_yellow}Using {color.blue}{item.items[0]}{color.end}!
""", 2)
        elif player.SLOT2 == item.items[1]: # Use "Potion of Healing"
            healing(2)
            typing(f"""
    {color.light_yellow}Using {color.blue}{item.items[1]}{color.end}!
""", 2)
        elif player.SLOT2 == item.items[2]: # Use "Potion of Speed"
            player.potionBonusSpeed = float(1.5)
            typing(f"""
    {color.light_yellow}Using {color.blue}{item.items[2]}{color.end}!
""", 2)
        elif player.SLOT2 == item.items[3]: # Use "Food"
            typing(f"""
    {color.light_yellow}Using {color.light_blue}{item.items[3]}{color.end}!
""", 2)
            healing(4)
        resetSlots(2)
    elif slot == 3:
        if player.SLOT3 == item.items[0]: # Use "Potion of Strength"
            player.potionBonusStrength = float(1.5)
            typing(f"""
    {color.light_yellow}Using {color.blue}{item.items[0]}{color.end}!
""", 2)
        elif player.SLOT3 == item.items[1]: # Use "Potion of Healing"
            healing(2)
            typing(f"""
    {color.light_yellow}Using {color.blue}{item.items[1]}{color.end}!
""", 2)
        elif player.SLOT3 == item.items[2]: # Use "Potion of Speed"
            player.potionBonusSpeed = float(1.5)
            typing(f"""
    {color.light_yellow}Using {color.blue}{item.items[2]}{color.end}!
""", 2)
        elif player.SLOT3 == item.items[3]: # Use "Food"
            typing(f"""
    {color.light_yellow}Using {color.light_blue}{item.items[3]}{color.end}!
""", 2)
            healing(4)
        resetSlots(3)
    pause()

# Remove and Move Items
def resetSlots(slot):
    if slot == 1:
        player.SLOT1 = None
        if player.SLOT2 != None:
            player.SLOT1 = player.SLOT2
            player.SLOT2 = None
            if player.SLOT3 != None:
                player.SLOT2 = player.SLOT3
                player.SLOT3 = None
    elif slot == 2:
        player.SLOT2 = None
        if player.SLOT3 != None:
            player.SLOT2 = player.SLOT3
            player.SLOT3 = None
    elif slot == 3:
        player.SLOT3 = None

#------------------------------- Starting The Game --------------------------------#

firstMenu()