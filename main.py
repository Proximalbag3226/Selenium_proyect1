from config.navigator import Navigation
from config.navigator import ChromeWindow as cw
from config.constants import universal

print("The options that we have to obtain the most recent news are: ")

print("1.La Jornada"
    "\n2.-El Universal"
    "\n3.-El Economista"
    "\n4.-Diario oficial de la federacion")

newspaper = input("Chose one option")

with Navigation() as nv:
    nv.get_url()
    nv.latest_news()
    new_window = cw()
    new_window.new_page(universal)
