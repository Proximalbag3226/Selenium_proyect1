from config.navigator import Navigation
from config.navigator import ChromeWindow as cw
from config.constants import *
from config.navigator import *
from test3 import * 

def news():
    while True:    
        print("The options that we have to obtain the most recent news are: ")
        print("1.La Jornada"
            "\n2.-El Universal"
            "\n3.-El Economista"
            "\n4.-Diario oficial de la federacion")

        newspaper = input("Chose one option ").strip()
        images = input("Do you want to download the images of the news? y/n").strip().lower()
        if images == "y" or "n":
            images_option = "download"
        elif images != str:
            print("Please introduce a correct value")
        else:
            print("Please select a correct option")

        if newspaper not in ["1", "2", "3", "4"]:
            print("Please select a correct option")
            continue
          
        if newspaper == "1":
            option = jornada
        elif newspaper == "2":
            option = universal
        elif newspaper == "3":
            option == economista
        elif newspaper == "4":
            option == dof
            
        with Navigation() as nv:
            nv.get_url(option)
            nv.latest_news('//*[@id="header-ljn"]/div[2]/a')
            new_window = cw()
            new_window.new_page(universal)
            break

news()