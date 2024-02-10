from config.navigator import Navigation as nv
from config.constants import *
from config.navigator import WordDocumentCreator

def get_newspaper_info(newspaper_option, amount):
    if newspaper_option == "1":
        nv.get_url("https://www.jornada.com.mx", jornada)
        nv.latest_news(xpath_jornada)
        return nv.title_news(title_jornada, amount)
    elif newspaper_option == "2":
        nv.get_url(universal)
        return nv.title_news(title_universal, amount)
    elif newspaper_option == "3":
        nv.get_url(economista)
        return nv.title_news(title_economista, amount)
    elif newspaper_option == "4":
        nv.get_url(dof)
        return nv.title_news(amount)
    else:
        raise ValueError("Invalid newspaper option")

def news():
    while True:    
        print("The options that we have to obtain the most recent news are: ")

        print("1. La Jornada"
              "\n2. El Universal"
              "\n3. El Economista"
              "\n4. Diario oficial de la federacion")

        newspaper = input("Choose an option: ").strip()
        amount = int(input("Enter the amount of news you want to receive: ").strip())      
        if amount == 0:
            print("The amount of news must be greater than 0")
            continue
        
        if newspaper not in ["1", "2", "3", "4"]:
            print("Please enter a valid option")
            continue
        
        try:
            newspaper_info = get_newspaper_info(newspaper, amount)
            
            word_creator = WordDocumentCreator("mi_documento_clase.docx")
            word_creator.add_heading("Title of the Document", level=1)
            word_creator.add_paragraph(newspaper_info)
            word_creator.save_document()
            
            break
        except Exception as e:
            print(f"Error: {e}")

news()
