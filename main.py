from config.constants import *
from config.test3 import *

#Create a function that realizes the actions of the module Navigation but inclides the user interface in the console
def news():
    while True:
        
        #We print the options that we include in this proyect and print this and the cuestions that we need
        print("-------Welcome to the news downloader-------")
        print("-------The paper news that we have are: ------")
        print("1-La jornada")
        print("2-El Economista")
        print("3-El universal")
        print("4-Diario oficial de la federacion---")
        
        #In this part of the code we check that the values of the answers are correct and in the case of we are not the conditionals block return an error message
        option = input("Please select a number of paper to download ").strip()
        if option == "1" or option == "2" or option =="3" or option =="4":  
            print("Ok")
        else:
            print("Please select a correct number")
            continue
        
        amount = int(input("Enter a amount of news to download "))
        if amount < 35:
            print("Correct amount")
        else:
            print("Please enter a minor amount")            
            continue
        
        image_option = input("Do you want to download the images from the papernews? (y/n)").strip()
        if image_option == "y" or image_option == "n":
            print("Ok")
        elif option == "4":
            print("The Diario oficial de la federacion does not have image available")
        else:
            print("Please enter a correct value")
            continue
            
        if option == "1":
            print("You selected 'La jornada'")
            option = jornada
        elif option == "2":
            print("You selected 'El Economista'")
            option = economista
        elif option == "3":
            print("You selected 'El universal'")
            option = universal
        elif option == "4":
            print("You selected 'Diario oficial de la federacion'")
            option = dof
        
        #And finally we have the implementation of the logic that we have in the Navigation
        nav = Navigation()
        if image_option == "y":
            nav2 = image_management(nav.driver, "Image")     
            nav2.get_img(amount, option["img"])
            time.sleep(4)
            pass
        else:
            pass
        time.sleep(2)
        nav.get_url_navigator(option["url"])    
        nav.latest_news(option["xpath"])
        nav.title_news(option["title"], amount)
        time.sleep(5)
        
        break
news()
