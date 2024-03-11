from config.constants import *
def news():
    while True:
        print("-------Welcome to the news downloader-------")
        print("-------The paper news that we have are: ------")
        print("1-La jornada")
        print("2-El Economista")
        print("3-El universal")
        print("4-Diario oficial de la federacion---")
        
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
        else:
            print("Please enter a correct value")
            continue
            
        if option == "1":
            print("You selected 'La jornada'")
        elif option == "2":
            print("You selected 'El Economista'")
        elif option == "3":
            print("You selected 'El universal'")
        elif option == "4":
            print("You selected 'Diario oficial de la federacion'")
            
        break
news()