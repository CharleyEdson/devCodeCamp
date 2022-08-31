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

Clients_destination = choose_destination()
Clients_restaurant = choose_restaurant()


