from random import randint


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
        "Health": 25,
        "Attack_Power": 2},
    'Attacks': {
        "Roar": 3,
        "Slam": 2,
        "Lion's Mane": 5,
        "Paw": 1}
}

Nine_headed_Lernaean_Hydra = { 'Attributes': {
        "Health": 30,
        "Attack_Power": 2.2},
    'Attacks': {
        "Roar": 3,
        "Slam": 2,
        "Hydra Water": 6,
        "Paw": 1}
}

Cerberus = { 'Attributes': {
        "Health": 40,
        "Attack_Power": 2.5},
    'Attacks': {
        "Roar": 3,
        "Slam": 2,
        "Cerberus_special": 7,
        "Paw": 1}
}




def Attack(Hercules, Enemy):
    Hercules_health = Hercules['Attributes']['Health']
    Enemy_health = Nemean_Lion['Attributes']['Health']
    print("It's time for battle against, the Vicious Nemean Lion")
    print("Hercules know's it time to battle to the death!")
    while Hercules_health >= 0 and Enemy_health >= 0:
        
        
        print("Hercules has " + str(Hercules_health) + " health left")
        
        print(Hercules['Attacks'])
        attack = input("Type the name of the Attack which you want to use")
        print("You've chosen the move: " + attack)
        Enemy_health = Enemy_health - (Hercules['Attacks'][attack] * Hercules['Attributes']['Attack_Power'])
        if Enemy_health <= 0:
            print("The foe has fainted! Congratulations!")
            break
        print("Great hit!, The enemy only has " + str(Enemy_health) + " left!")
        print("It's the Enemies turn to attack!")
        enemy_attack_number = randint(0,3)
        enemy_attacks_list = list(Nemean_Lion["Attacks"])
        enemy_attack = enemy_attacks_list[enemy_attack_number]
        print("The enemy used the attack " + enemy_attack + "!")
        Hercules_health = Hercules_health - (Nemean_Lion['Attacks'][enemy_attack] * Nemean_Lion['Attributes']['Attack_Power'])
        print("That was a brutal attack!")
        print("Hercules has " + str(Hercules_health) + " health left!!")
        #So far I have now randomized the enemie's attack


Attack(Hercules, Cerberus)



#----------------------------------------------------
#Game begins
print("")

