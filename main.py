from random import randint
from time import sleep


Hercules = { 'Attributes': {
        "Health": 75,
        "Attack_Power": 3},
    'Attacks': {
        "Flex_on_em": 6,
        "Slam": 5,
        "God_juice": 8,
        "Greek_thunder": 9}

    }

#print(Hercules['Attributes']['Attack_Power'])

#Enemies

Nemean_Lion = { 'Attributes': {
        "Name": 'Nemean Lion',
        "Health": 25,
        "Attack_Power": 2},
    'Attacks': {
        "Roar": 3,
        "Slam": 2,
        "Lion's Mane": 5,
        "Paw": 1}
}

Nine_headed_Lernaean_Hydra = { 'Attributes': {
        "Name": 'Nine Headed Lernaean Hydra',
        "Health": 30,
        "Attack_Power": 2.2},
    'Attacks': {
        "Roar": 3,
        "Slam": 2,
        "Hydra Water": 6,
        "Paw": 1}
}

Cerberus = { 'Attributes': {
        "Name": 'Cerberus',
        "Health": 40,
        "Attack_Power": 2.5},
    'Attacks': {
        "Roar": 3,
        "Slam": 2,
        "Cerberus_special": 7,
        "Paw": 1}
}
#Scene 1
def beginning_of_story():
    print("You are Hercules, the greatest of the Greek Heroes! You have been tasked by King Eurystheus to slay the vicious Nemean Lion, defeat the impossible nine-headed Lernaean Hydra, and capture the guard dog of the underworld—Cerberus.")
    sleep(1)
    print("Our story begins with Hercules making his journey to the first of his great tasks as commissioned by King Eurystheus!")
    sleep(2)
#Scene 2-after this is battle scene
def battle_scene_with_Nemean_Lion():
    print("After a long journey, you have finally spotted Nemean Lion.")
    sleep(2)
    print('Hercules: "Nemean Lion! I have come to end your rain of terror!"')
    sleep(2)
    print('Nemean Lion: "We shall see about that Hercules!')

#Scene 3 - attack scene against Nemean Lion

#Scene 4 - 
def post_battle_scene_1():
    print("Exhausted, Hercules must rest before continuing on to his next opponent.")
    print("....")
    sleep(1)
    print("...The next day...")
    print("Hercules: On to the next one!")
    print("Hercules begins his travels once more.")

#Scene 5- Battle scene with Lernaean Hydra
def battle_scene_with_Lernaean_Hydra():
    print("Hercules: At last, Lernaean Hydra, your time is done!")
    print("Lernaean Hydra: HA HA HA! You amuse me Hercules. I will put an end to your good luck immediately.")
    print("Hercules: ... Bring it on...")

#Scene 6- atack scene with Hydra

#Scene 7-Post battle scene
def post_battle_scene_2():
    print("...bloodied, Hercules is even more tired after the first fight.")
    sleep(1)
    print("...He must rest and recove for the harrows that awaits him...")
    sleep(1)

#scene 8
def battle_scene_with_Cerberus():
    print("Hercules: Cerberus!!! You're done spreading fear to the world. I will end you today!")
    print("...")
    sleep(1)
    print("Cerberus: Don't amuse me Hercules. You are a puny man. You don't stand a chance against me!")
    print("Hercules: Then let's do this, what are you waiting for!")

#Scene 9-attack scene

#scene 10
def end_game():
    print("Hercules has done it!")
    print("He has vanquashed all of his enemies!")
    print("*Returning to King Eurystheus*")
    sleep(5)
    print("The king: Hercules, my boy. You have done your country a great service in deed. You are a god among men. We salute you.")
    print("The King: Please accept your payment.")
    print("Hercules: No payment necessary Sire. I just want to return to Meg.")
    print("... And so ends Hercule's magnificent tale of the 3 enemies.")
    print('.....')
    print('.....')
    print('FIN')

def Attack(Hercules, Enemy):
    Hercules_health = Hercules['Attributes']['Health']
    Enemy_health = Enemy['Attributes']['Health']
    Enemy_name = Enemy['Attributes']['Name']
    print(f"It's time for battle against, {Enemy_name}")
    sleep(1)
    print("....Hercules know's it time to battle to the death!")
    print("........")
    sleep(1)
    print("**The battle commences**")
    sleep(2)
    while Hercules_health >= 0 and Enemy_health >= 0:
        
        
        print("Hercules has " + str(Hercules_health) + " health left")
        
        print(Hercules['Attacks'])
        attack = input("Type the name of the Attack which you want to use: ")
        print("You've chosen the move: " + attack)
        Enemy_health = Enemy_health - (Hercules['Attacks'][attack] * Hercules['Attributes']['Attack_Power'])
        if Enemy_health <= 0:
            print(f"{Enemy_name} has been slain! Congratulations!")
            break
        print(f"Great hit!, The {Enemy_name} only has " + str(Enemy_health) + " left!")
        print(f"It's {Enemy_name}'s turn to attack!")
        enemy_attack_number = randint(0,3)
        enemy_attacks_list = list(Enemy["Attacks"])
        enemy_attack = enemy_attacks_list[enemy_attack_number]
        print(f"{Enemy_name} used the attack " + enemy_attack + "!")
        Hercules_health = Hercules_health - (Enemy['Attacks'][enemy_attack] * Enemy['Attributes']['Attack_Power'])
        print("That was a brutal attack!")
        
       

#----------------------------------------------------
#Game begins


def RunGame():
    beginning_of_story()
    battle_scene_with_Nemean_Lion()
    Attack(Hercules, Nemean_Lion)
    post_battle_scene_1()
    battle_scene_with_Lernaean_Hydra()
    Attack(Hercules, Nine_headed_Lernaean_Hydra)
    post_battle_scene_2()
    battle_scene_with_Cerberus()
    Attack(Hercules, Cerberus)
    end_game()

RunGame()




