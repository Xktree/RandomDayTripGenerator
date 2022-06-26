# Developer Objectives (5 points each objective)

# As a developer, I want to make at least three commits with descriptive messages. 
# As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainments in their own separate lists. (DONE)
# As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!

# User Objectives (5 points each objective)

# As a user, I want a destination to be randomly checked for my day trip. 
# As a user, I want a restaurant to be randomly selected for my day trip. 
# As a user, I want a mode of transportation to be randomly selected for my day trip. 
# As a user, I want a form of entertainment to be randomly selected for my day trip. 

# User Objectives (10 points each objective) - Preferably write the two separate 

# As a user, I want to be able to confirm that my day trip is "complete" once I like all of the random selections. 
# As a user, I want to display my completed trip in the console. 

# User Objectives (15 points each objective)

# As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don't like one or more of those things. 





# List for possible vacation destinations
vacation_destinations = ["Aruba", "Bermuda", "Chile", "Denmark"]

# Lists of Aruban options
Aruba_restaurants = ["Water's Edge Restaurant & Bar Aruba", "Fred Royal Aruba", "L.G. Smith's Steak & Chop House", "Ike's Bistro"]
Aruba_mode_of_transporation = ["plane", "boat", "submarine"]
Aruba_entertainment = ["ATV Off Road Exploring and Snorkeling", "Aruba Aloe Factory", "Renaissance Island", "The Butterfly Farm"]

# Lists of Bermudan options
Bermuda_restaurants = ["La Trattoria", "Beluga Sushi Bar", "1609 Bar and Restaurant", "Flanagan's Irish Pub"]
Bermuda_mode_of_transportation = ["plane", "boat"]
Bermuda_entertainment = ["Bermuda Acquarium and Crystal Caves", "Horshoe Bay Beach", "Hartley Helmet Diving", "Shipwreck Snorkeling"]

# Lists of Chilean options 
Chile_restaurants = ["Restaurante 040", "Borago", "99 Restaurante", "Ambrosia"]
Chile_mode_of_transportation = ["plane", "boat", "car"]
Chile_entertainment = ["Torres Del Paine In Patagonia", "Isla Magdalena", "Street Art In Valparaiso", "Cajon Del Maipo"]

# Lists of Danish options
Denmark_restaurants = ["Basso Kobenhavn", "Restaurant Krebsegaarden", "Den Lille Fede Restaurant", "Restaurant Maven"]
Denmark_mode_of_transportation = ["plane", "train", "car", "boat", "bus", "cycling"]
Denmark_entertainment = ["Copenhagen Zoo", "Denmark National Park", "Rabjerg Mile", "Egeskov Castle in Funen"]

# Initiation
import random 

yesList = ["Yes","yes","Y","y"]
result = ["","","",""]
name = ""
vacation = ""
restaurant = ""
transportation = ""
entertainment = ""

# User and number of guests
def userName():
    return_name = input("Welcome to Global Tours, your premium travel agency! This is our vacation randomizer, great if you are unsure about where you would like to go. Please enter your first and last name:")
    print("\n")
    guests = int(input("Welcome {}, how many people will be traveling in your group?".format(return_name)))
    print("\n")
    print("How exciting, we have some amazing vacation options!")
    return return_name 

# Generate random location  
def userVacation():
    # user_destination = random(vacation_destinations, 1)
    user_destination = random.choice(vacation_destinations)
    result[0] = user_destination
    vacation_choice = input(f"We have chosen {user_destination} as your dream vacation spot, is this ok with you? Y/N")
    return vacation_choice

def userRestaurant():
    restaurant_list = randomSamplePicker("restaurant")
    print(restaurant_list)
    user_restaurant = random.choice(restaurant_list)
    restaurant_choice = input(f"We have chosen {user_restaurant} as your dream restaurant spot, is this ok with you? Y/N")
    return restaurant_choice

# def randomSamplePicker(sampleTypeContext):
#     return_result = ["HIIIIIIIIII"]
#     if sampleTypeContext == "restaurant":
#         if result[0] == "Aruba":  
#             return_result = return_result + Aruba_restaurants
#         elif result[0] == "Bermuda":
#             return_result = return_result + Bermuda_restaurants
#         elif result[0] == "Chile":
#             return_result = return_result + Chile_restaurants
#         elif result[0] == "Denmark":
#             return_result = return_result + Denmark_restaurants
#         else:
#             return_result = return_result + ["sdfasdf\sd","qweqweqweqweqweqweqweqwe"]
#     return return_result

def randomSamplePicker(sampleTypeContext):
    if sampleTypeContext == "restaurant":
        if result[0] == "Aruba":  
            return Aruba_restaurants
        elif result[0] == "Bermuda":
            return Bermuda_restaurants
        elif result[0] == "Chile":
            return Chile_restaurants
        elif result[0] == "Denmark":
            return Denmark_restaurants

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
    transporation = userTransportation()
    if transportation in yesList:
        print("An excellent transportation choice!")
    else:
        print("That's ok, we have other options.")
        transportationChoice()

# name = userName()
vacationChoice()
restaurantChoice()
transportationChoice()

