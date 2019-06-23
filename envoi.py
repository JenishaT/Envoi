import time
import random
import string
from journeyer import journeyer
from Location import location

locations = [location("1234", "Karachi"), location("4321", "Lahore"), location("7652", "Peshawar"), location("6763", "Kashmir"), location("7352", "Islamabad"), location("4524", "Faisalabad")]
journeyers = [journeyer("Nilmani Y", "1234", "7352", "415123456"), journeyer("Sheeza A", "1234", "4321", "647123456"), journeyer("Morsal S", "7652", "7352", "415097532"), journeyer("Fatima J", "6763", "7352", "415094942"), journeyer("Jenisha T", "4321", "7352", "415097532")]

def homepage():
    prompt = input("")
    
    if (prompt.lower() == "hi envoi"):
            print("Hello welcome to Envoi! \nIf you want something delivered text \"1\". \nIf you're a journeyer text \"2\".")
            
            choice = input("")
            
            while choice != "1" and choice != "2":
                print("Invalid Option! Please text one to the following: \n \"1\" : to get something delivered \n \"2\" : sign in as a journeyer")
                choice = input("")
            
            
            if choice == "1":
                request_delivery()
                
            elif choice == "2":
                print("If you already have a Journeyer account text \"1\" to Login \n Text \"2\" to create an account")
                opt = input("")
                if opt == "1":
                    #login()
                    print("The login function hasn't been implemented yet")
                elif opt == "2":
                    #signup()
                    print("The signup function hasn't been implemented yet")
            
def find_name(code):
    for loc in locations:
        if loc.code == code:
            return loc.name
    return ""

def print_locations():
    for loc in locations:
        print(loc.name + ": " + loc.code)    
    
def get_pickup_dropoff():
    print("Text the Envoi PIN of the pick up location. \nText \"3\" to view the list of PINs")
    
    pickup = input("")
    pickup_name = ""
    
    if pickup == "3":
        print_locations()
    else:
        pickup_name = find_name(pickup)
        while pickup_name == "":
            print("Invalid PIN, Refer to the list and enter the correct pick up location: \n")
            print_locations()
            
            pickup = input("")
            pickup_name = find_name(pickup)
            
    print("Text the Envoi PIN of the drop off location. \nText \"3\" to view the list of PINs")
    
    drop = input("")
    drop_name = ""
    
    if drop == "3":
        print_locations()
    else:
        drop_name = find_name(drop)
        while drop_name == "":
            print("Invalid PIN, Refer to the list and enter the correct drop off location: \n")
            print_locations()
            
            drop = input("")
            drop_name = find_name(drop)
            print("Text the Envoi PIN of the drop off location. \nText \"3\" to view the list of PINs")
            
            drop = input("")
            drop_name = ""
            
            if drop == "3":
                print_locations()
            else:
                drop_name = find_name(drop)
                while drop_name == "":
                    print("Invalid PIN, Refer to the list and enter the correct drop off location: \n")
                    print_locations()
                    
                    drop = input("")
                    drop_name = find_name(drop) 
                    
    return pickup_name, drop_name, pickup, drop
    
def match_journeyer(pickup, drop):
    for journeyer in journeyers:
        if journeyer.depart == pickup and journeyer.destination == drop:
            return journeyer.name, journeyer.number
    return "", ""
        
def request_delivery():
    
    pickup_name, drop_name, pickup, drop = get_pickup_dropoff()
                    
    print("You would like to deliver a package from \"" + pickup_name + "\" to \"" +  drop_name + "\"?  \nText \"1\", if this is correct. \nOtherwise text \"2\", to re-enter the PINS" ) 
    
    correct = input("")
    
    if correct == "2":
        pickup_name, drop_name = get_pickup_dropoff()
    elif correct == "1":
        name, number = match_journeyer(pickup, drop)
        if name == "" or number == "":
            print("Sorry there is no one availiable to make a delivery from \"" + pickup_name + "\" to \"" +  drop_name + "\" at the moment")
            
        else:
            print("Congratulations! You have been matched with " + name + ". \nPlease contant " + name + " at " + number + ".")
            return
              
homepage()
