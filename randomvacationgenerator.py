# Developer Objectives (5 points each objective)

# As a developer, I want to make at least three commits with descriptive messages. (DONE)
# As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainments in their own separate lists. (DONE)
# As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing! (DONE)

# User Objectives (5 points each objective)

# As a user, I want a destination to be randomly checked for my day trip. (DONE)
# As a user, I want a restaurant to be randomly selected for my day trip. (DONE)
# As a user, I want a mode of transportation to be randomly selected for my day trip. (DONE)
# As a user, I want a form of entertainment to be randomly selected for my day trip. (DONE)

# User Objectives (10 points each objective) - Preferably write the two separate 

# As a user, I want to be able to confirm that my day trip is "complete" once I like all of the random selections. (DONE)
# As a user, I want to display my completed trip in the console. (DONE)

# User Objectives (15 points each objective)

# As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don't like one or more of those things. (DONE)





# List for possible vacation destinations
vacation_destinations = ["Aruba", "Bermuda", "Chile", "Denmark"]

# Lists of Aruban options
Aruba_restaurants = ["Water's Edge Restaurant & Bar Aruba", "Fred Royal Aruba", "L.G. Smith's Steak & Chop House", "Ike's Bistro"]
Aruba_transportation = ["plane", "boat", "submarine"]
Aruba_entertainment = ["ATV Off Road Exploring and Snorkeling", "Aruba Aloe Factory", "Renaissance Island", "The Butterfly Farm"]

# Lists of Bermudan options
Bermuda_restaurants = ["La Trattoria", "Beluga Sushi Bar", "1609 Bar and Restaurant", "Flanagan's Irish Pub"]
Bermuda_transportation = ["plane", "boat"]
Bermuda_entertainment = ["Bermuda Acquarium and Crystal Caves", "Horshoe Bay Beach", "Hartley Helmet Diving", "Shipwreck Snorkeling"]

# Lists of Chilean options 
Chile_restaurants = ["Restaurante 040", "Borago", "99 Restaurante", "Ambrosia"]
Chile_transportation = ["plane", "boat", "car"]
Chile_entertainment = ["Torres Del Paine In Patagonia", "Isla Magdalena", "Street Art In Valparaiso", "Cajon Del Maipo"]

# Lists of Danish options
Denmark_restaurants = ["Basso Kobenhavn", "Restaurant Krebsegaarden", "Den Lille Fede Restaurant", "Restaurant Maven"]
Denmark_transportation = ["plane", "train", "car", "boat", "bus", "cycling"]
Denmark_entertainment = ["Copenhagen Zoo", "Denmark National Park", "Rabjerg Mile", "Egeskov Castle in Funen"]

# Initiation
import random 

yesList = ["Yes","yes","Y","y"]
result = ["","","",""]
name = ""
guests = ""
vacation = ""
restaurant = ""
transportation = ""
entertainment = ""

# User and number of guests
def userName():
    print("\n")
    return_name = input("Welcome to Global Tours, your premium travel agency! This is our vacation randomizer, great if you are unsure about where you would like to go. Please enter your first and last name:")
    print("\n")
    return return_name 
    
def userGuests(): 
    print("\n")
    return_guests = int(input(f"Welcome {name}, how many people will be traveling in your group?"))
    print("\n")
    return return_guests
    
# Generate random location  
def userVacation():
    user_destination = random.choice(vacation_destinations)
    result[0] = user_destination
    print("\n")
    vacation_choice = input(f"We have chosen {user_destination} as your dream vacation spot, is this ok with you? Y/N")
    print("\n")
    return vacation_choice

# Generate random restaurant
def userRestaurant():
    restaurant_list = samplePicker("restaurant")
    user_restaurant = random.choice(restaurant_list)
    result[1] = user_restaurant
    print("\n")
    restaurant_choice = input(f"We have chosen {user_restaurant} as your ideal restaurant spot, is this ok with you? Y/N")
    print("\n")
    return restaurant_choice

# Generate random transportation 
def userTransportation():
    transportation_list = samplePicker("transportation")
    user_transportation = random.choice(transportation_list)
    result[2] = user_transportation
    print("\n")
    transportation_choice = input(f"We have chosen {user_transportation} as your preferred transportation option, is this ok with you? Y/N")
    print("\n")
    return transportation_choice

# Generate random entertainment 
def userEntertainment():
    entertainment_list = samplePicker("entertainment")
    user_entertainment = random.choice(entertainment_list)
    result[3] = user_entertainment
    print("\n")
    entertainment_choice = input(f"We have chosen {user_entertainment} as your entertainment option, is this ok with you? Y/N")
    print("\n")
    return entertainment_choice

# Utility
def samplePicker(sampleTypeContext):
    if sampleTypeContext == "restaurant":
        match result[0]:
            case "Aruba":
                return Aruba_restaurants
            case "Bermuda":
                 return Bermuda_restaurants
            case "Chile":
                 return Chile_restaurants
            case "Denmark":
                 return Denmark_restaurants
    elif sampleTypeContext == "transportation":
        match result[0]:
            case "Aruba":
                return Aruba_transportation
            case "Bermuda":
                 return Bermuda_transportation
            case "Chile":
                 return Chile_transportation
            case "Denmark":
                 return Denmark_transportation
    elif sampleTypeContext == "entertainment":
        match result[0]:
            case "Aruba":
                return Aruba_entertainment
            case "Bermuda":
                 return Bermuda_entertainment
            case "Chile":
                 return Chile_entertainment
            case "Denmark":
                 return Denmark_entertainment

# User input for vacation choices 
def vacationChoice():
    vacation = userVacation()
    if vacation in yesList:
        print("An excellent vacation choice!")
    else:
        print("That's ok, we have other options.")
        vacationChoice()

def restaurantChoice():
    restaurant = userRestaurant()
    if restaurant in yesList:
        print("An excellent restaurant choice!")
    else:
        print("That's ok, we have other options.")
        restaurantChoice()

def transportationChoice():
    transportation = userTransportation()
    if transportation in yesList:
        print("An excellent transportation choice!")
    else:
        print("That's ok, we have other options.")
        transportationChoice()

def entertainmentChoice():
    entertainment = userEntertainment()
    if entertainment in yesList:
        print("An excellent entertainment choice!")
    else: 
        print("That's ok, we have other options.")
        entertainmentChoice()

# Recursive trip confirmation
def tripChoices():
    vacationChoice()
    restaurantChoice()
    transportationChoice()
    entertainmentChoice()
    print("\n")
    user_confirmation = input("Would you like to confirm your trip now? Y/N")
    print("\n")
    if user_confirmation in yesList: 
       print(f"Great! You will be arriving in {result[0]} by {result[2]} where you will enjoy {result[3]}. You will end your trip by dining at the local favorite, {result[1]}!")
       print("\n")
       end = input()
    else:
        print("That's ok, we can start over.")
        tripChoices()

# Calling functions
name = userName()
guests = userGuests()
tripChoices()
