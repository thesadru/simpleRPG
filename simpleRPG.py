import random
import os
import time
class GameExit(Exception):
    pass

class char: #character
    def __init__(self,id,type,name,strengh,stamina,health,lvl,special):
        self.id      = id
        self.type    = type
        self.name    = name
        self.strengh = strengh
        self.stamina = stamina
        self.health  = health
        self.lvl     = lvl
        self.special = special
        
        self.special_lvl = 1
        self.charge = False
        self.bleed  = False
        self.dodge  = False
        self.scare  = False
        self.hp = health
        self.st = stamina
        self.xp = 0
        self.xp_current = 0
        self.move = ""
        self.devmove = ""
        self.movehistory = ""
        self.moveban = ""
hero  = char(1,2,3,4,5,6,7,8)
enemy = char(1,2,3,4,5,6,7,8)
class res: #result
    def __init__(self,herohp,herost,heroch,enemyhp,enemyst,enemych,string,heroinfo=None,enemyinfo=None,hero=hero):
        self.herohp  = herohp
        self.herost  = herost
        self.herocharge = heroch
        self.enemyhp = enemyhp
        self.enemyst = enemyst
        self.enemycharge = enemych
        self.string = string
        
        self.charge = False
        self.bleed  = False
        self.dodge  = False
        self.scare  = False
        
        self.bleed = True if heroinfo  == "bleed.True" else (False if heroinfo  == "bleed.False" else hero.bleed)
        self.dodge = True if heroinfo  == "dodge.True" else (False if heroinfo  == "dodge.False" else hero.dodge)
        self.scare = True if enemyinfo == "scare.True" else (False if enemyinfo == "scare.False" else hero.scare)
        


hero_list = [
    char("h00","hero","knight",2,4,4,1,"bleed"), # 1 damage per turn  | 2 damage per turn | will gain stamina from enemy
    char("h01","hero","rogue ",2,4,4,1,"dodge"), # always defend      | reflect damage    | stun enemy
    char("h02","hero","ninja ",2,4,4,1,"punch"), # does double damage | go through shield | leave with only 1hp OR kill
]
enemy_list = [
    char("e00","enemy","worm           ",1,2,1,2,False),
    char("e01","enemy","rat            ",1,2,2,3,False),
    char("e02","enemy","goblin         ",1,4,2,4,False),
    char("eo3","enemy","skeleton       ",2,4,2,5,False),
    char("e04","enemy","zombie         ",2,4,4,6,False),
    char("e05","enemy","guard          ",2,4,6,7,False),
    char("e06","enemy","guardian       ",3,4,6,8,False), #no special avalible
]
boss_list = [
    char("b00","boss" ,"vengeful spirit",4,8,6 ,10,"haunt       "), # stun enemy
    char("b01","boss" ,"possesed priest",3,8,8 ,10,"heal        "), # change all stamina to health
    char("b02","boss" ,"skeleton wizard",2,4,14,10,"fire ball   "), # half health, all lost health = damage
]
limited_boss_list = boss_list[:]

seed = int(time.time())
random.seed(seed)
try:
    output_mode
    output_mode = "terminal"
except:
    output_mode = "console"

#definitions
noclear = False
def clr(output_mode=output_mode,noclear=noclear): #clear screen
    if not noclear:
        if output_mode == "console":
            os.system( 'cls' )
        else:
            print("\n" * 50)
    else:
        noclear = True
    

#main menu definitions
def tutorial(page=1): #tutorial
    while page != "0":
        clr()
        if   page == "0":
            pass
        elif page == "1":
            print("basics:\n")
            print("Your task is to kill all the enemies and escape the dungeon.")
            print("You can attack with 5 different moves.")
            print("No move can be used 3 times in a row.")
            print("Once you enter the dungeon you will be faced with an enemy.")
            print("If the enemy is defeated, you will gain it's levels as xp.")
            print("Every time you defeat 3 enemies, you will face a boss.")
            print("The boss also has a special move, but it gives 10 xp.")
            print("Once you defeat 3 bosses you will enter endless mode.")
            print("You now regenerate only half the HP.")
            print("The maximum level is 10, when you reach it, you will fight buffed enemies.")
            print("enemies get tougher every 25 xp and you fight bosses every 4th enemy.")
            print("Once the game ends, your levels will be converted to a score.")
            print("Remember that enemies don't know your special.")
            page = input("page: ")
        elif page == "2":
            print("moves:\n")
            print("attack: reduce health of the enemy by your strengh, but lose 2 stamina")
            print('defend: be immune to "attack", but lose 1 stamina')
            print("run: run away and refill your stamina, but you are vulnerable to attacks")
            print("charge: charge your special move")
            print("special: unleash a special move if you are charged")
            print()
            print("specials:")
            print("bleed lvl 1: every turn, the enemy loses 1 hp")
            print("bleed lvl 2: every turn, the enemy loses 2 hp")
            print("bleed lvl 3: every turn, the enemy loses 2 hp, and the hero drains 1 stamina")
            print("dodge lvl 1: if you were to be attacked, you will lose 0 hp")                # |console max
            print("dodge lvl 2: if you were to be attacked, the damage will be dealt to the enemy instead")
            print("dodge lvl 3: if you were to be attacked, the damage will be dealt to the enemy instead and it gets stunned")
            print("punch lvl 1: you will do a basic atack at double the damage")
            print("punch lvl 2: you will do a basic attack at triple the damage")
            print("punch lvl 3: the enemy loses health equal to double your strengh, if it doesn't die, it will be left with 1 hp")
            print("lvl 5: all previous abilities + heals 2 hp")
            print("haunt: the hero gets stunned")
            print("heal: the enemy loses all stamina, it will get healed for the amount of stamina  it just lost")
            print("fire ball: the enemy loses half it's hp, all lost hp will be dealt to the hero")
            page = input("page: ")
        elif page == "3":
            print("settings:\n")
            print("seed {seed}: will let you change the seed, useful for speedrunning (no spaces allowed)")
            print("developer: enable notes and cheat codes")
            print("terminal: makes text clear by moving it up with 50 empty lines")
            print("console:  makes text clear by clearing the entire screen")
            print("exit (in main screen/death screen): crashes the window")
            print("suicide (while moving): immidieataly crashes the game")
            print()
            print("more settings may be implemented in ~5 years")
            page = input("page: ")
        else:
            print("invalid page number, only 0,1,2,3 are accepted")
            page = input("page: ")


            
                     
#game
while True:
    started = False
    developer = False
    while started == False:
        clr()
        print("Welcome to simpleRPG, my very first python game")
        print("If you are new, I recommend reading the tutorial with 'tut'/'tutorial'")
        print("You can also fiddle with settings with the commands in 'tut' page 3")
        print("You may also type 'console' or 'terminal' to fix formating")
        print("To play enter 'start'")
        action = input("[tutorial/settings/start] ")
    
        
        if action == "tut" or action == "tutorial":
            tutorial("1")
        elif action == "start":
            hero = None
            while hero == None:
                clr()
                print("1: knight | bleed, do damage every turn")
                print("2: rogue  | dodge, dodge enemy attack")
                print("3: ninja  | punch, deal high damage")
                try:
                    hero = hero_list[int(input("which hero do you want to play as: [1/2/3] "))-1]
                    difficulty = None
                    while difficulty == None:
                        clr()
                        print("0: baby   | enemies will never attack\n" if developer==True else "",end="") 
                        print("1: easy   | enemies sub-randomly move, only for people who have low experience with games")
                        print("2: normal | enemies use AI to attack, recomended for casual players")
                        print("3: hard   | super smart AI, hard to beat, recommended for true challenge")
                        try:
                            difficulty = int(input("which difficulty can you take? [1/2/3] "))
                            if developer == True:
                                allowed_difficulties = [0,1,2,3]
                            else:
                                allowed_difficulties = [1,2,3]
                            if difficulty in allowed_difficulties:
                                started = True
                            else:
                                difficulty = None
                        except:
                            pass
                except:
                    pass
        elif action.split()[0] == "seed":
            print("seed =",seed)
            seed = action.split()[1]
            random.seed(seed)
            print("new seed:",seed)
            input()
        elif action == "developer":
            developer = True
            
        elif action == "console":
            output_mode = "console"
        elif action == "terminal":
            output_mode = "terminal"
            
        elif action == "exit":
            raise GameExit("exiting game")
            
    
    defeated = [0,0]
    endless = False
    
    #######
    while hero.hp > 0:
    #upgrade | 0=0 1=15 2=30 3=45 4=60 5=75  6=100 7=125 8=150 9=175 10=200
        clr()
        if hero.lvl < 5: #upgrades for 15 xp
            if hero.xp_current > 15:
                hero.xp_current = hero.xp_current-15
                hero.lvl += 1
                upgrade = True
                while upgrade == True:
                    clr()
                    print(hero.name)
                    print("lvl",hero.lvl)
                    print("xp",hero.xp_current,"/",15)
                    print("score:",hero.xp*difficulty if hero.xp*difficulty!=69 else "nice")
                    print("1 - strengh:",    str(hero.strengh),"/ 4")
                    print("2 - stamina:",    str(hero.stamina),"/ 8")
                    print("3 - health:" ,    str(hero.health) ,"/ 8")
                    print("4 - special:",str(hero.special_lvl),"/ 5")
                    print()
                    print("1 - +1 strengh")
                    print("2 - +2 stamina")
                    print("3 - +2 health" )
                    print("4 - +1 special")
                    print()
                    action = input("which stat do you want to upgarde: [1/2/3/4] ")
                    if action == "1":
                        if hero.strengh < 4:
                            hero.strengh += 1
                            print("upgraded strengh")
                            input()
                            upgrade = False
                        else:
                            print("strengh is already MAX level")
                            input()
                    elif action == "2":
                        if hero.stamina < 8:
                            hero.stamina += 2
                            print("upgarded stamina")
                            input()
                            upgrade = False
                        else:
                            print("stamina is already MAX level")
                            input()
                    elif action == "3":
                        if hero.health < 8:
                            hero.health += 2
                            print("upgarded health")
                            input()
                            upgrade = False
                        else:
                            print("health is already MAX level")
                            input()
                    elif action == "4":
                        if hero.special_lvl < 5:
                            hero.special_lvl += 1
                            print("upgarded speciaL")
                            input()
                            upgrade = False
                        else:
                            print("special is already MAX level")
                            input()
                    else:
                        clr()
    
    
            clr()
            print(hero.name)
            print("lvl",hero.lvl)
            print("xp",hero.xp_current,"/",15)
            print("score:",hero.xp*difficulty)
    
        elif hero.lvl < 10: #upgrades for 25 xp
            if hero.xp_current >= 25:
                hero.xp_current = hero.xp_current-25
                hero.lvl += 1
                upgrade = True
                while upgrade == True:
                    print(hero.name)
                    print("lvl",hero.lvl)
                    print("xp",hero.xp_current,"/",25)
                    print("score:",hero.xp*difficulty if hero.xp*difficulty!=69 else "nice")
                    print("1 - strengh:",    str(hero.strengh),"/ 4")
                    print("2 - stamina:",    str(hero.stamina),"/ 8")
                    print("3 - health:" ,    str(hero.health) ,"/ 8")
                    print("4 - special:",str(hero.special_lvl),"/ 5")
                    print()
                    print("1 - +1 strengh")
                    print("2 - +2 stamina")
                    print("3 - +2 health" )
                    print("4 - +1 special")
                    print()
                    action = input("which stat do you want to upgarde: [1/2/3/4] ")
                    if action == "1":
                        if hero.strengh < 4:
                            hero.strengh += 1
                            print("upgraded strengh")
                            input()
                            upgrade = False
                        else:
                            print("strengh is already MAX level")
                            input()
                    elif action == "2":
                        if hero.stamina < 8:
                            hero.stamina += 2
                            print("upgarded stamina")
                            input()
                            upgrade = False
                        else:
                            print("stamina is already MAX level")
                            input()
                    elif action == "3":
                        if hero.health < 8:
                            hero.health += 2
                            print("upgarded health")
                            input()
                            upgrade = False
                        else:
                            print("health is already MAX level")
                            input()
                    elif action == "4":
                        if hero.special_lvl < 8:
                            hero.special_lvl += 2
                            print("upgarded speciaL")
                            input()
                            upgrade = False
                        else:
                            print("special is already MAX level")
                            input()
    
            print(hero.name)
            print("lvl",hero.lvl)
            print("xp",hero.xp_current,"/",25)
            print("score:",hero.xp*difficulty if hero.xp*difficulty!=69 else "nice")
    
        else: #endless
            print(hero.name)
            print("lvl max")
            print("score:",hero.xp*difficulty if hero.xp*difficulty!=69 else "nice")     
        input()
        noclear = False
    # enemy generation
        clr()
        if defeated[0]<3:
            if defeated[1]%3 == 0 and defeated[1]!=0 and enemy.type=="enemy":
                enemy = limited_boss_list[random.randrange(0,2)]
                limited_boss_list.remove(enemy)
            else:
                enemy = enemy_list[random.randrange(0,6)]
        else:
            if endless and defeated[1]%3 == 0 and enemy.type=="enemy":
                enemy = boss_list[random.randrange(0,2)]
            else:
                enemy = enemy_list[random.randrange(0,6)]
                endless = True
        input(("you encountered a "+enemy.name))
        
        if enemy.type=="boss":
            if defeated[0]==0:
                enemy.health = enemy.health*1//2
                enemy.stamina = enemy.stamina*1//2
                enemy.strengh = enemy.strengh*1//2
            elif defeated[0]==1:
                enemy.health = enemy.health*2//3
                enemy.stamina = enemy.stamina*2//3
                enemy.strengh = enemy.strengh*2//3
            elif defeated[0]==2:
                enemy.health = enemy.health*3//4
                enemy.stamina = enemy.stamina*3//4
                enemy.strengh = enemy.strengh*3//4
        if hero.lvl >= 10:
            enemy.health = enemy.health*(defeated[0]-3)//2
            enemy.stamina = enemy.stamina*(defeated[0]-3)//2
            enemy.strengh = enemy.strengh*(defeated[0]-3)//2
    
        hero.st ,hero.charge,hero.bleed,hero.dodge,hero.stun = hero.stamina,False,False,False,False
        enemy.hp,enemy.st,enemy.charge,enemy.stun            = enemy.health,enemy.stamina,False,False
        if defeated[0] < 10:
            hero.hp = hero.health
        else:
            hero.hp += (hero.health-hero.hp)//2
        hero.bleed = None
        # > print table > print text > ask for a move > generate a move with ai > generate a response > change variables > set text
        outcome = res(None,None,None,None,None,None,"",)
        while hero.hp > 0 and enemy.hp > 0:
            clr()
            print("a - attack | d - defend | r - run | c - charge | s - special")
            print("         +--------+-------+     +---------+-------+")
            print("         |  ",hero.hp,"hp |",hero.st,"st  |     |  ",enemy.hp,"hp  |",enemy.st,"st  |")
            print("         +----------------+     +-----------------+")
            print("         |    ",hero.name,"    |     |",enemy.name,"|")
            print("         +----------+-----+     +-----------+-----+")
            print("         | strengh  | ",hero.strengh," |     | strengh   | ",enemy.strengh," |")
            print("         +----------+-----+     +-----------+-----+")
            print("         | stamina  | ",hero.stamina," |     | stamina   | ",enemy.health," |")
            print("         +----------+-----+     +-----------+-----+")
            print("         | health   | ",hero.health," |     | health    | ",enemy.stamina," |") #visual combat
            print("         +----------+-----+     +-----------+-----+")
            print("         lvl",hero.lvl,"                 lvl",enemy.lvl,"")
            print("        ",hero.special,("#####" if hero.charge == True else ("/////" if hero.dodge==True else "     ")),"           ",(enemy.special if enemy.special != False else ""),("#####" if enemy.charge == True else "     "))
            if developer == True:
                print(">>> enemy:",enemy.move)
                print(">>> hero:",hero.move)
                print(">>> hero hp:",outcome.herohp)
                print(">>> hero st:",outcome.herost)
                print(">>> hero charge:",outcome.herocharge)
                print(">>> enemy hp:",outcome.enemyhp)
                print(">>> enemy st:",outcome.enemyst)
                print(">>> enemy charge:",outcome.enemycharge)
                print(">>> move ai:",enemy.devmove)
            print()
            print(outcome.string)
            print(("enemy is bleeding" if hero.bleed == True else ""))
            print(("hero is stunned" if hero.stun  == True else ""))
            print(("enemy is stunned" if enemy.stun == True else ""))
            print()
            
            # ai
            if   difficulty == 0:
                if   enemy.moveban == "r":
                    enemy.move = "d"
                    enemy.moveban = "d"
                    enemy.devmove = "defence"
                elif enemy.moveban == "d":
                    enemy.move = "r"
                    enemy.moveban = None
                    enemy.devmove = "running #1"
                else:
                    enemy.move = "r"
                    enemy.moveban = "r"
                    enemy.devmove = "running #2"
                    
                    
            elif difficulty == 1:
                if enemy.st <= 1:
                    enemy.move = "r"
                    enemy.devmove = "1 or less st"
                elif enemy.charge != False and enemy.type == "boss" and enemy.st >= 2:
                    enemy.move = "a" if enemy.movehistory in ["d","c"] else ("d" if enemy.movehistory == "c" else "c")
                    enemy.devmove = "pseudo random uncharged"
                elif enemy.charge != True and enemy.st >= 2:
                    enemy.move = "a" if enemy.movehistory != "a" else "d"
                    enemy.devmove = "pseudo random charged"
                else:
                    enemy.move = "r"
                    enemy.devmove = "run in case of emergency"
                
            
            
            elif difficulty == 2:
                pass
                if enemy.stun == True:
                    enemy.move = "stun"
                    enemy.stun = False
                    enemy.devmove = "stunned"
                    
                if enemy.moveban != "r" and enemy.st == 0:
                    enemy.move = "r"
                    enemy.devmove = "0 stamina"
                elif enemy.type == "boss" and enemy.charge == False and enemy.st == 0:
                    enemy.move = "r" if enemy.movehistory != "r" else "c"
                    enemy.devmove = "0 stamina and can charge"
                elif enemy.type == "boss" and enemy.charge == True:
                    enemy.move = "s"
                    enemy.devmove = "using a special"
                
                elif enemy.charge != False and enemy.type == "boss" and enemy.st >= 2: #pseudo random uncharged
                    enemy.move = "a" if enemy.movehistory in ["d","c"] else ("d" if enemy.movehistory == "c" else "c")
                    enemy.devmove = "pseudo random uncharged"
                elif enemy.charge != True and enemy.st >= 2: #pseudo random charged
                    enemy.move = "a" if enemy.movehistory != "a" else "d"
                    enemy.devmove = "pseudo random charged"
                else: #in case of emergency
                    enemy.move = "r"
                    enemy.devmove = "run in case of emergency"
            
            
            elif difficulty == 3:
                if enemy.stun == True:
                    enemy.move = "stun"
                    enemy.stun = False
                    enemy.devmove = "stunned"
                    
                elif enemy.moveban != "r" and enemy.st == 0 and hero.st <= 1: #0 stamina AND it's safe to run
                    enemy.move = "r"
                    enemy.devmove = "0 stamina AND it's safe to run"
                elif enemy.moveban != "a" and enemy.st >= 2 and hero.hp <= enemy.strengh and hero.st == 0: #able to attack AND will kill the hero AND and hero can't defend
                    enemy.move = "a"
                    enemy.devmove = "able to attack AND will kill the hero AND and hero can't defend"
                elif enemy.moveban != "d" and enemy.st >= 1 and hero.st >= 2 and enemy.hp <= hero.strengh: #able to defend AND hero is able to kill AND hero will kill
                    enemy.move = "d"
                    enemy.devmove = "able to defend AND hero is able to kill AND hero will kill"
        
                elif enemy.moveban != "s" and enemy.id == "b01" and enemy.charge == True and enemy.health-enemy.hp >= enemy.st and hero.st <= 1: #can effectivly heal AND won't get hit
                    enemy.move = "s"
                    enemy.devmove = ""
                elif enemy.moveban != "s" and enemy.id == "b01" and enemy.charge == True and enemy.st >= 2 and enemy.st+enemy.hp-enemy.strengh > 0 and enemy.hp-enemy.strengh <= 0: #can heal AND hero will kill AND heal can save
                    enemy.move = "s"
                    enemy.devmove = "can effectivly heal AND won't get hit"
                elif enemy.moveban != "s" and enemy.id == "b02" and enemy.charge == True and enemy.health-(enemy.hp-(enemy.hp/2 + enemy.hp%2/2)) >= hero.hp: #can fireball AND will kill the hero
                    enemy.move = "s"
                    enemy.devmove = "can fireball AND will kill the hero"
        
                elif enemy.moveban != "r" and enemy.st <= 1: #recharge from 1 stamina
                    enemy.move = "r"
                    enemy.devmove = "recharge from 1 stamina"
                elif enemy.moveban != "a" and enemy.st >= 2 and hero.st == 0: #will hit the enemy
                    enemy.move = "a"
                    enemy.devmove = "will hit the enemy"
                elif enemy.moveban != "s" and enemy.id == "b00" and enemy.charge == True and hero.charge == True: #will waste the hero's special
                    enemy.move = "s"
                    enemy.devmove = "will waste the hero's special"
        
                elif enemy.moveban != "c" and enemy.type == "boss" and hero.st <= 1 and enemy.charge == False: #charge safely
                    enemy.move = "c"
                    enemy.devmove = "charge safely"
                elif enemy.moveban != "s" and enemy.id == "b01" and enemy.health-enemy.hp+2 <= enemy.st and hero.st <= 2: #heal with overheal 2 and less AND won't be hit
                    enemy.move = "s"
                    enemy.devmove = "heal with overheal 2 and less AND won't be hit"
                elif enemy.moveban != "s" and hero.id == "b02" and enemy.health-(enemy.hp-(enemy.hp/2 + enemy.hp%2/2)) >= enemy.health/2: #fireball with more han half possible damage
                    enemy.move = "s"
                    enemy.devmove = "fireball with more than half possible damage"
                    
                elif enemy.charge != False and enemy.type == "boss": #charging
                    enemy.move = "c"
                    enemy.devmove = "charging"
                elif enemy.charge != True: #pseudo random
                    enemy.move = "a" if enemy.movehistory != "a" else "d"
                    enemy.devmove = "pseudo random charged"
                else: #in case of emergency
                    enemy.move = "r"
                    enemy.devmove = " run in case of emergency"
        
            if enemy.movehistory == "":
                enemy.movehistory = enemy.move
                enemy.moveban = ""
            else:
                if enemy.movehistory == enemy.move:
                    enemy.moveban = enemy.move
                else:
                    enemy.movehistory = enemy.move
                    enemy.moveban = ""
                
                
            #hero move
            hero.move = None
            while hero.move == None:
                if hero.stun == True:
                    hero.stun = False
                    hero.move = "stun"
                
                hero.move_test = input("enter your move: [a/d/r/c/s] ")
                
                if hero.move_test != hero.moveban:
                    if hero.move_test == "a":
                        if hero.st >= 2:
                            hero.move = hero.move_test
                        else:
                            print("low stamina!")
    
                    if hero.move_test == "d":
                        if hero.st >= 1:
                            hero.move = hero.move_test
                        else:
                            print("low stamina!")
    
                    if hero.move_test == "r":
                        hero.move = hero.move_test
    
                    if hero.move_test == "c":
                        if hero.charge == False:
                            hero.move = hero.move_test
                        else:
                            print("already charged!")
    
                    if hero.move_test == "s":
                        if hero.charge == True:
                            hero.move = hero.move_test
                        else:
                            print("not charged!")
                else:
                    print("cannot used 3 same moves in row")
                    
                if hero.move_test == "suicide":
                    raise GameExit("you have commited suicide")
                
            if hero.movehistory == "":
                hero.movehistory = hero.move
                hero.moveban = ""
            else:
                if hero.movehistory == hero.move:
                    hero.moveban = hero.move
                else:
                    hero.movehistory = hero.move
                    hero.moveban = ""
            #move combo and calculation
    #=============================================================================
            response = { "a" :{ "a" :res((-enemy.strengh/2), -2, hero.charge, -hero.strengh/2, -2, enemy.charge, "both hero and enemy have attacked",), "d" :res(0, -2, hero.charge, 0, -1, enemy.charge, "hero's attack was defended by the enemy",), "r" :res(0, -2, hero.charge, -hero.strengh, -enemy.st+enemy.stamina, enemy.charge, "hero has attacked the enemy while it was running away"), "c" :res(0, -2, hero.charge, -hero.strengh, 0, True, "hero has attacked the enemy while it was charging"), "s0":res(0, -2, hero.charge, 0, 0, False, "hero was scared away from attacking", enemyinfo="scare.True"), "s1":res(0, -2, hero.charge, -hero.strengh+enemy.st, -enemy.st, False, "hero has attacked the enemy while it was healing itself"), "s2":res(-(enemy.health-(enemy.hp-(enemy.hp/2 + enemy.hp%2/2))), -2, hero.charge, -(enemy.hp/2 + enemy.hp%2/2)-hero.strengh, 0, False, "hero has attacked the enemy but was hit by a fireball"), "stun":res(0, -2, hero.charge, -hero.strengh, 0, enemy.charge, "hero ran away while the enemy was stunned"), }, "d" :{ "a" :res(0, -1, hero.charge, 0, -2, enemy.charge, "hero has defended the enemy's attack"), "d" :res(0, -1, hero.charge, 0, -1, enemy.charge, "both hero and enemy have defended"), "r" :res(0, -1, hero.charge, 0, -enemy.st+enemy.stamina, enemy.charge, "hero has defended while the enemy was running away"), "c":res(0, -1, hero.charge, 0, 0, True, "hero has defended while the enemy was charging"), "s0":res(0, -1, hero.charge, 0, 0, False, "hero was scared away from defending", enemyinfo="scare.True"), "s1":res(0, -1, hero.charge, enemy.st, -enemy.st, False, "hero has defended while the enemy was healing itself"), "s2":res(-(enemy.health-(enemy.hp-(enemy.hp/2 + enemy.hp%2/2))), -1, hero.charge, -(enemy.hp/2 + enemy.hp%2/2), 0, False, "hero has defended but was hit by a fireball"), "stun":res(0, -1, hero.charge, 0, 0, enemy.charge, "hero defended while the enemy was stunned"), }, "r" :{ "a" :res(-enemy.strengh, -hero.st+hero.stamina, hero.charge, 0, -2, enemy.charge, "hero was attacked while running away"), "d" :res(0, -hero.st+hero.stamina, hero.charge, 0, -1, enemy.charge, "hero ran away while the enemy was defending"), "r" :res(0, -hero.st+hero.stamina, hero.charge, 0, -enemy.st+enemy.stamina, enemy.charge, "both hero and enemy ran away"), "c" :res(0, -hero.st+hero.stamina, hero.charge, 0, 0, True, "hero ran away while the enemy was charging"), "s0":res(0, 0, hero.charge, 0, 0, False, "hero was scared away from running away", enemyinfo="scare.True"), "s1":res(0, -hero.st+hero.stamina, hero.charge, enemy.st, -enemy.st, False, "hero ran away while the enemy was healing itself"), "s2":res(-(enemy.health-(enemy.hp-(enemy.hp/2 + enemy.hp%2/2))), -hero.st+hero.stamina, hero.charge, -(enemy.hp/2 + enemy.hp%2/2), 0, False, "hero was running away but was hit by a fireball"), "stun":res(0, -hero.st+hero.stamina, hero.charge, 0, 0, enemy.charge, "hero ran away while the enemy was stunned"), }, "c":{ "a" :res(-enemy.strengh, 0, True, 0, -2, enemy.charge, "hero was attacked while it was charging"), "d" :res(0, 0, True, 0, -1, enemy.charge, "hero has charged while the enemy was defending"), "r" :res(0, 0, True, 0, -enemy.st+enemy.stamina, enemy.charge, "hero was charging while the enemy was running away"), "c" :res(0, 0, True, 0, 0, True, "both hero and enemy have charged"), "s0":res(0, 0, hero.charge, 0, 0, False, "hero was scared away from charging", enemyinfo="scare.True"), "s1":res(0, 0, True, enemy.st, -enemy.st, False, "hero has charged while the enemy was healing"), "s2":res(-(enemy.health-(enemy.hp-(enemy.hp/2 + enemy.hp%2/2))), 0, True, -(enemy.hp/2 + enemy.hp%2/2), 0, False, "hero has charged but was hit by a fireball"), "stun":res(0, 0, True, 0, 0, enemy.charge, "both hero and enemy are stunned"), }, "s0":{ "a" :res(-enemy.strengh, 0, False, 0, -2, enemy.charge, "hero has caused the enemy to be bleeding and was attacked", heroinfo="bleed.True"), "d" :res(0, 0, False, 0, -1, enemy.charge, "hero has caused the enemy to be bleeding while it was defending", heroinfo="bleed.True"), "r" :res(0, 0, False, 0, -enemy.st+enemy.stamina, enemy.charge, "hero has caused the enemy to be bleeding while it was running away ", heroinfo="bleed.True"), "c" :res(0, 0, False, 0, 0, True, "hero has caused the enemy to be bleeding while it was charging", heroinfo="bleed.True"), "s0":res(0, 0, False, 0, 0, False, "hero was scared away from making the enemy bleed", enemyinfo="scare.True"), "s1":res(0, 0, False, enemy.st, -enemy.st, False, "hero has caused the enemy to be bleeding while it was healing itself", heroinfo="bleed.True"), "s2":res(-(enemy.health-(enemy.hp-(enemy.hp/2 + enemy.hp%2/2))), 0, False, -(enemy.hp/2 + enemy.hp%2/2), 0, False, "hero has caused the enemy to be bleeding but was hit by a fireball", heroinfo="bleed.True"), "stun":res(0, 0, hero.charge, 0, 0, enemy.charge, "hero has caused the enemy to be bleeding while it was stunned", heroinfo="bleed.True"), }, "s1":{ "a" :res(0, 0, False, 0, 0, enemy.charge, "hero has dodged enemy's attack "), "d" :res(0, 0, False, 0, -1, enemy.charge, "hero has prepared to dodge enemy's attack while it was defending", heroinfo="dodge.True"), "r" :res(0, 0, False, 0, -enemy.st+enemy.stamina, enemy.charge, "hero has prepared to dodge enemy's attack while it was running away", heroinfo="dodge.True"), "c" :res(0, 0, False, 0, 0, True, "hero has prepared to dodge enemy's attack while it was charging", heroinfo="dodge.True"), "s0":res(0, 0, False, 0, 0, False, "hero was scared from away preparing to dodge", enemyinfo="scare.True"), "s1":res(0, 0, False, enemy.st, -enemy.st, False, "hero has prepared to dodge enemy's attack while it was healing", heroinfo="dodge.True"), "s2":res(-(enemy.health-(enemy.hp-(enemy.hp/2 + enemy.hp%2/2))), 0, False, -(enemy.hp/2 + enemy.hp%2/2), 0, False, "hero has prepared to dodge enemy's attack while but was hit by a fireball", heroinfo="dodge.True"), "stun":res(0, 0, hero.charge, 0, 0, enemy.charge, "hero has prepared to dodge enemy's attack while it was stunned", heroinfo="dodge.True"), }, "s2":{ "a" :res(-enemy.strengh, 0, False, (-hero.strengh*2 if hero.special_lvl==1 else (-hero.strengh*3 if hero.special_lvl==2 else (-enemy.hp+1 if enemy.hp>hero.strengh else (-hero.strengh)))), -2, enemy.charge, "hero threw a punch at the enemy while being attacked"), "d" :res(0, 0, False, (-hero.strengh*2 if hero.special_lvl==1 else (-hero.strengh*3 if hero.special_lvl==2 else (-enemy.hp+1 if enemy.hp>hero.strengh else (-hero.strengh)))), -1, enemy.charge, "hero threw a punch at the enemy while it was defending"), "r" :res(0, 0, False, (-hero.strengh*2 if hero.special_lvl==1 else (-hero.strengh*3 if hero.special_lvl==2 else (-enemy.hp+1 if enemy.hp>hero.strengh else (-hero.strengh)))), -enemy.st+enemy.stamina, enemy.charge, "hero threw a punch at the enemy while it was running away"), "c" :res(0, 0, False, (-hero.strengh*2 if hero.special_lvl==1 else (-hero.strengh*3 if hero.special_lvl==2 else (-enemy.hp+1 if enemy.hp>hero.strengh else (-hero.strengh)))), 0, True, "hero threw a punch at the enemy while it was charging"), "s0":res(0, 0, False, 0, 0, False, "hero was scared away from punching", enemyinfo="scare.True"), "s1":res(0, 0, False, (-hero.strengh*2 if hero.special_lvl==1 else (-hero.strengh*3 if hero.special_lvl==2 else (-enemy.hp+1 if enemy.hp>hero.strengh else (-hero.strengh))))+enemy.st, -enemy.st, False, "hero threw a punch at the enemy while it was healing itself"), "s2":res(-(enemy.health-(enemy.hp-(enemy.hp/2 + enemy.hp%2/2))), 0, False, (-hero.strengh*2 if hero.special_lvl==1 else (-hero.strengh*3 if hero.special_lvl==2 else (-enemy.hp+1 if enemy.hp>hero.strengh else (-hero.strengh))))-(enemy.hp/2 + enemy.hp%2/2), 0, False, "hero threw a punch at the enemy but was hit by a fireball"), "stun":res(0, 0, hero.charge, (-hero.strengh*2 if hero.special_lvl==1 else (-hero.strengh*3 if hero.special_lvl==2 else (-enemy.hp+1 if enemy.hp>hero.strengh else (-hero.strengh)))), 0, enemy.charge, "hero threw a punch at the enemy while it was stunned"), }, "stun":{ "a" :res(-enemy.strengh, 0, hero.charge, 0, -2, enemy.charge, "hero was attacked while being stunned"), "d" :res(0, 0, hero.charge, 0, -1, enemy.charge, "hero is stunned while enemy is defending"), "r" :res(0, 0, hero.charge, 0, -enemy.st+enemy.stamina, enemy.charge, "hero is stunned while enemy is running away"), "c":res(0, 0, hero.charge, 0, 0, True, "hero is stunned while the enemy was charging"), "s0":res(0, 0, hero.charge, 0, 0, False, "hero is stunned,... again???", enemyinfo="scare.True"), "s1":res(0, 0, hero.charge, enemy.st, -enemy.st, False, "hero is stunned while enemy is healing itself"), "s2":res(-(enemy.health-(enemy.hp-(enemy.hp/2 + enemy.hp%2/2))), 0, hero.charge, -(enemy.hp/2 + enemy.hp%2/2), 0, False, "hero is stunned while being hit by a fireball"), "stun":res(0, 0, hero.charge, 0, 0, enemy.charge, "both hero and enemy are stunned"), }, }
    #=============================================================================
            if hero.move == "s":
                hero.move = "s0" if hero.id=="h00" else ("s1" if hero.id=="h01" else "s2")
            outcome = response[hero.move][enemy.move]
            hero.hp += outcome.herohp
            hero.st += outcome.herost
            hero.charge = outcome.herocharge
            enemy.hp += outcome.enemyhp
            enemy.st += outcome.enemyst
            enemy.charge = outcome.enemycharge
            
            hero.bleed = outcome.bleed if hero.bleed != True else True
            hero.dodge = outcome.dodge if hero.bleed != True else True
            hero.stun = outcome.scare
            
            if hero.bleed == True and hero.special_lvl == 1:
                enemy.hp -= 1
                print("ENEMY IS BLEEDING, AWW YEEEEAAAAAH")
            if hero.bleed == True and hero.special_lvl == 2:
                enemy.hp -= 2
            if hero.bleed == True and hero.special_lvl == 3:
                enemy.hp -= 2
                enemy.st -= 1
                hero.st  += 1
                
            if hero.dodge == True and enemy.move == "a" and hero.special_lvl == 1:
                hero.hp += enemy.strengh
                hero.dodge = False
            if hero.dodge == True and enemy.move == "a" and hero.special_lvl == 2:
                hero.hp += enemy.strengh
                enemy.hp -= enemy.strengh
                hero.dodge = False
            if hero.dodge == True and enemy.move == "a" and hero.special_lvl == 3:
                hero.hp += enemy.strengh
                enemy.hp -= enemy.strengh
                enemy.stun = True
                hero.dodge = False
            
            if hero.special_lvl == 5:
                hero.hp += 2
                hero.hp = hero.health if hero.hp>=hero.health else hero.hp
            
            hero.hp  = int(hero.hp )
            enemy.hp = int(enemy.hp)
            
        clr()
        print("a - attack | d - defend | r - run | c - charge | s - special")
        print("         +--------+-------+     +---------+-------+")
        print("         |  ",hero.hp,"hp |",hero.st,"st  |     |  ",enemy.hp,"hp  |",enemy.st,"st  |")
        print("         +----------------+     +-----------------+")
        print("         |    ",hero.name,"    |     |",enemy.name,"|")
        print("         +----------+-----+     +-----------+-----+")
        print("         | strengh  | ",hero.strengh," |     | strengh   | ",enemy.strengh," |")
        print("         +----------+-----+     +-----------+-----+")
        print("         | stamina  | ",hero.stamina," |     | stamina   | ",enemy.health," |")
        print("         +----------+-----+     +-----------+-----+")
        print("         | health   | ",hero.health," |     | health    | ",enemy.stamina," |") #visual combat
        print("         +----------+-----+     +-----------+-----+")
        print("         lvl",hero.lvl,"                 lvl",enemy.lvl,"")
        print("        ",hero.special,("#####" if hero.charge == True else "     "),"         ",(enemy.special if enemy.special != False else ""),("#####" if enemy.charge == True else "     "))
        print()
        print(hero.name,"has defeated a",enemy.name,"\nyou may continue through the dungeon")
                                       
                                       
        hero.xp += enemy.lvl
        hero.xp_current += enemy.lvl
        if enemy.type == "enemy":
            defeated[1] += 1
        elif enemy.type == "boss":
            defeated[0] += 1
        else:
            defeated[1] += 1
        noclear = True
            
    clr()
    diff = "baby"if difficulty==0 else("easy"if difficulty==1 else("normal"if difficulty==2 else "hard"))
    if not endless:
        print("GAME OVER")
    else:
        print("THE END")
        print("")
    print("cause of death: attack from",enemy.name)
    print("died at stage",sum(defeated))
    print("difficulty:",difficulty)
    print("enemy generation seed:",seed)
    print()
    print("hero:",hero.name)
    print("level:",hero.lvl)
    if hero.lvl<10:
        print("strengh:",    str(hero.strengh),"/ 4")
        print("stamina:",    str(hero.stamina),"/ 8")
        print("health:" ,    str(hero.health) ,"/ 8")
        print("special:",str(hero.special_lvl),"/ 5")
    else:
        print("enemy buff:",(defeated[0]-3)/2)
    print()
    print("score:",hero.xp*difficulty if hero.xp*difficulty!=69 else "nice")
    if input("press enter to go back to the main screen, enter exit to exit ") == "exit":
        raise GameExit("exiting game")
