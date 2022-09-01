from tkinter import Y
import random


destinations = ["Paris", "Barcelona", "Tokyo", "Quito", "Hermosa Beach"]
restaurants = ["La Quixote", "La Pan", "Sushitogo", "Brother's Burritos"]
transportations = ["Airplane", "Cruise", "Train", "Car", "Bike"]
entertainments = ["Traveling to the Louve", "Drinking wine and eat tapas", "Going to the hot springs", "Going to El Panecillo", "Going to the beach"]



def rand_destination():
    random_num = random.randint(0,4) #if I want, make a list so that the random number has to loop through all the destinations before repeating. can use pop
    destination = destinations[random_num]
    return destination

def rand_restaurant():
    random_num = random.randint(0,3)
    restaurant = restaurants[random_num]
    return restaurant

def rand_transportations():
    random_num = random.randint(0,4)
    transportation_for_the_day = transportations[random_num]
    return transportation_for_the_day

def rand_entertainemnt():
    random_num = random.randint(0,4)
    entertainemnt = entertainments[random_num]
    return entertainemnt

def confirm_destination():
    destination_confirmation = False
    while destination_confirmation == False:
        randomized_destination = rand_destination()
        destination_reponse = input(f"We have selected {randomized_destination} for your destination. Does this suit your fancy? Enter y/n: ")
        if destination_reponse == 'y':
            destination_confirmation == True
            print("Awesome! Glad you have decided on a place. Let's move on!")
            return randomized_destination
        else:
            destination_confirmation = False
            print("Oh, sorry you didn't like your destination. No worries, we can try something else!")

def confirm_restuarants():
    restaurant_confirmation = False
    while restaurant_confirmation == False:
        randomized_restaurant = rand_restaurant()
        restaurant_reponse = input(f"We have selected {randomized_restaurant} for your Restaurant. Does this suit your fancy? Enter y/n: ")
        if restaurant_reponse == 'y':
            restaurant_confirmation == True
            print("Awesome! Glad you have decided on a Restaurant. Bone-Apple-Tee. Let's move on!")
            return randomized_restaurant
        else:
            restaurant_confirmation = False
            print("Oh, sorry you didn't like your Restaurant. No worries, we can try something else!")

def confirm_transportations():
    transportation_confirmation = False
    while transportation_confirmation == False:
        randomized_transportation = rand_transportations()
        transportation_reponse = input(f"We have selected {randomized_transportation} for your mode of transportation. Does this suit your fancy? Enter y/n: ")
        if transportation_reponse == 'y':
            transportation_confirmation == True
            print("Awesome! Glad you have decided on transportation. Will be there in no time! Let's move on!")
            return randomized_transportation
        else:
            transportation_confirmation = False
            print("Oh, sorry you didn't like your mode of transportation. No worries, we can try something else!")


def confirm_entertainment():
    entertainment_confirmation = False
    while entertainment_confirmation == False:
        randomized_entertainment
        randomized_entertainment = rand_entertainemnt()
        entertainment_reponse = input(f"We have selected {randomized_entertainment} for your entertainment. Does this suit your fancy? Enter y/n: ")
        if entertainment_reponse == 'y':
            entertainment_confirmation == True
            print("Awesome! Glad you have decided on entertainment. Let's move on!")
            return randomized_entertainment
        else:
            entertainment_confirmation = False
            print("Oh, sorry you didn't like your entertainment of choice. No worries, we can try something else!")




#----------------------------------------------------------------------------------------#
# This will start everything
print("Welcome to the Day Trip Generator! Not sure of where to travel? Don't worry, we can help with that, you have come to the right place! Sit back and enjoy :)")

    
confirmed_destination = confirm_destination()
confirmed_transport = confirm_transportations()
confirmed_restaurant = confirm_restuarants()
confirmed_entertainment = confirm_entertainment()


   
def display_tentative_trip():
    print("Congrats! We have completed generating your day trip. Now let's just confirm that this is the trip you wanted.")
    print("Destination: " + confirmed_destination)
    print("Transportation: " + confirmed_transport)
    print("Restaurant: " + confirmed_restaurant)
    print("Entertainment: " + confirmed_entertainment)



display_tentative_trip()

confirmed_trip = "no"
while confirmed_trip =='no':
    confirmed_trip = input("Would you like to finalize this once in a lifetime trip? Type y/n: ")
    if confirmed_trip == 'y':
        print("Prepare for your dream Vacation to come alive! You will be arriving in " + confirmed_destination + " by " + confirmed_transport + ", where you will spend the day " + confirmed_entertainment + ". You will end this amazing day dining in style at " + confirmed_restaurant + " a local favorite.")
    else:
        print("Not to worry, we will try again")
        confirmed_trip = 'no'
        confirmed_destination = confirm_destination()
        confirmed_transport = confirm_transportations()
        confirmed_restaurant = confirm_restuarants()
        confirmed_entertainment = confirm_entertainment()
        display_tentative_trip()







"""
First attempt
#try passing in functions as parameters
def confirm_trip(destination, transport, restaurant, entertainment):
    confirmed_trip = "no"
    while confirmed_trip =='no':
        confirmed_trip = input("Would you like to finalize this once in a lifetime trip? Type y/n")
        if confirmed_trip == 'y':
            print("Prepare for your dream Vacation to come alive! You will be arriving in " + destination + " by " + transport + ", where you will spend the day " + entertainment + ". You will end this amazing day dining in style at " + restaurant + " a local favorite.")
            break
        else:
            print("Not to worry, we will try again")



        confirmed_trip == 'n'
        
        confirmed_destination = confirm_destination()
        confirmed_transport = confirm_transportations()
        confirmed_restaurant = confirm_restuarants()
        confirmed_entertainment = confirm_entertainment()
        display_tentative_trip()

confirm_trip(confirmed_destination, confirmed_transport, confirmed_restaurant, confirmed_entertainment)"""









"""
print(rand_transportations())
print(rand_destination())
print(rand_restaurant())
print(rand_entertainemnt())
"""


"""

def choose_destination():
    confirmation = False
    while confirmation is False:
    
        for destination in destinations:
            chosen_destination = input(f"We have selected {destination} for your destination. Does this suit your fancy? Enter y/n: ")
            if chosen_destination == 'y':
                
                print("Awesome! Glad you have decided on a place. Let's move on!")
                final_destination = destination
                confirmation = True
                return final_destination
                break
            else:
                print("Oh, sorry you didn't like your destination. No worries, we can try something else!")


def choose_restaurant():
    confirmation = False
    while confirmation is False:
    
        for restaurant in restaurants:
            chosen_restaurant = input(f"We have selected {restaurant} for your destination. Does this suit your fancy? Enter y/n: ")
            if chosen_restaurant == 'y':
                
                print("Awesome! Glad you have decided on a Restaurant. Bone-Apple-Tee. Let's move on!")
                final_restaurant = restaurant
                confirmation = True
                return final_restaurant
                break
            else:
                print("Oh, sorry you didn't like your restaurant. No worries, we can try something else!")

def choose_transportation():
    confirmation = False
    while confirmation is False:
    
        for transport in transportations:
            chosen_transport = input(f"We have selected {transport} for your destination. Does this suit your fancy? Enter y/n: ")
            if chosen_transport == 'y':
                
                print("Awesome! Glad you have decided on a mode of transport. Safe travels! Let's move on!")
                final_transport = transport
                confirmation = True
                return final_transport
                break
            else:
                print("Oh, sorry you didn't like your mode of transportation. No worries, we can try something else!")

def choose_entertainment():
    confirmation = False
    while confirmation is False:
    
        for entertain in entertainments:
            chosen_entertain = input(f"We have selected {entertain} for your destination. Does this suit your fancy? Enter y/n: ")
            if chosen_entertain == 'y':
                
                print("Awesome! Glad you have decided on your entertainment. This will be a true delight! Let's move on!")
                final_entertain = entertain
                confirmation = True
                return final_entertain
                break
            else:
                print("Oh, sorry you didn't like your entertainment pick. No worries, we can try something else!")

Clients_destination = choose_destination()
Clients_restaurant = choose_restaurant()
Clients_transport = choose_transportation()
Clients_entertainment = choose_entertainment()

def display_tentative_trip():
    print("Congrats! We have completed generating your day trip. Now let's just confirm that this is the trip you wanted.")
    print("Destination: " + Clients_destination)
    print("Transportation: " + Clients_transport)
    print("Restaurant: " + Clients_restaurant)
    print("Entertainment: " + Clients_entertainment)

display_tentative_trip()

def confirm_trip():
    confirmed_trip = input("Would you like to finalize this once in a lifetime trip?")
    if confirmed_trip == 'y':
        print(f"Prepare for your dream vacation to come alive! YOu will be arriving in {Clients_destination} by {Clients_transport}, where you will spend the day {confirm_entertainment}. You will end this amazing day dining in style at {confirmed_restaurant}, a local favorite.")
    else:
        confirmed_trip == 'N'
        print("Not to worry, we will try again")
        Clients_destination = choose_destination()
        Clients_restaurant = choose_restaurant()
        Clients_transport = choose_transportation()
        Clients_entertainment = choose_entertainment()
        display_tentative_trip()

confirm_trip()

#line 94 clients destination isn't being substaniated before it's getting called. Need to fix.'

"""