destinations = ["Paris", "Barcelona", "Tokyo", "Quito", "Hermosa Beach"]
restaurants = ["La Quixote", "La Pan", "Sushitogo", "Brother's Burritos"]
transportion = ["Airplane", "Cruise", "Train", "Car", "Bike"]
entertainment = ["The Louve", "Drink wine and eat tapas", "Go to the hot springs", "Go to El Panecillo", "Go to the beach"]

print("Welcome to the Day Trip Generator! Not sure of where to travel? Don't worry, we can help with that, you have come to the right place! Sit back and enjoy :)")


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
    
        for transport in transportion:
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
    
        for entertain in entertainment:
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

def finalize_day_trip():
    print("Congrats! We have completed generating your day trip. Now let's just confirm that this is the trip you wanted.")
    print("Destination: " + Clients_destination)
    print("Transportation: " + Clients_transport)
    print("Restaurant: " + Clients_restaurant)
    print("Entertainment: " + Clients_entertainment)

