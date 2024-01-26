from config.navigator import Navigation
from config.navigator import ChromeWindow as cw
from config.constants import universal

with Navigation() as nv:
    nv.get_url()
    nv.latest_news()
    new_window = cw()
    new_window.new_page(universal)
