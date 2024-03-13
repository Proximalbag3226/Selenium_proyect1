from config.constants import *
from config.test3 import *
import re

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
        
        word_name = input("Please enter a name of the word document for the news ").strip()
        no_permitted = re.compile(r'[!@#$%^&*()<>?/\|}{~:]')
        if bool(no_permitted.search(word_name)) == True:
            print("The name of the word document can't have special caracters")
            continue
        else:
            print("Ok correct name")
            name = word_name
        
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
        elif image_option == "y" and option == "4":
            pass
        else:
            pass
        time.sleep(2)
        nav.get_url_navigator(option["url"])    
        nav.latest_news(option["xpath"])
        nav.title_news(option["title"], amount)
        time.sleep(5)
        word = WordDocumentCreator(name)
        word.add_heading(f"The news of the day from {option} is in here")
        word.add_paragraph(titles)
        word.save_document()
        time.sleep(3)
        
        repeat = input("Do you want to try again? (y/n)").strip()
        if repeat == "y":
            news()
        elif repeat == "n":
            print("Have a nice day")
            break
        else:
            print("Select a correct option")
            pass
news()
