from config.navigator import Navigation
from config.navigator import ChromeWindow as cw
from config.constants import *
from config.navigator import WordDocumentCreator

def news():
    while True:    
        print("The options that we have to obtain the most recent news are: ")

        print("1.La Jornada"
            "\n2.-El Universal"
            "\n3.-El Economista"
            "\n4.-Diario oficial de la federacion")

        newspaper = input("Chose one option ").strip()
        amount = int(input("Enter the amount of news that you want to receive ").strip())      
        if amount == 0:
            print("The amount of news it must be may to 0")

        if newspaper not in ["1", "2", "3", "4"]:
            print("Ingrese una opcion correcta")
            continue
        
        if newspaper == "1":
            option = jornada
            with Navigation() as nv:
                nv.get_url(option)
                nv.latest_news('//*[@id="header-ljn"]/div[2]/a')
                t1 = nv.title_news('.nota-titulo.mb-1 a', amount)
        elif newspaper == "2":
            option = universal
            with Navigation() as nv:
                nv.get_url(option)
                nv.latest_news('//*[@id="header-ljn"]/div[2]/a')
                t1 = nv.title_news('.nota-titulo.mb-1 a', amount)
        elif newspaper == "3":
            option == economista
        elif newspaper == "4":
            option == dof
            
        with Navigation() as nv:
            nv.get_url(jornada)
            nv.latest_news('//*[@id="header-ljn"]/div[2]/a')
            t1 = nv.title_news('.nota-titulo.mb-1 a', amount)
            
            word_creator = WordDocumentCreator("mi_documento_clase.docx")
            word_creator.add_heading("Título del Documento", level=1)
            word_creator.add_paragraph(t1)

            word_creator.save_document()

        break

news()