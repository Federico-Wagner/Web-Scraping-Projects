from selenium import webdriver
from .scraping import Scraper
from .navigation import Navigation
from .data_managing import Data_manager

class Carrefour_scraper:
	def __init__(self,LOCKING_FOR, ART_LIMIT ,DEBUG=False, close_nav=True):
		self.PATH = "chromedriver.exe"
		self.driver = webdriver.Chrome(self.PATH)
		self.LOCKING_FOR = LOCKING_FOR
		self.DEBUG = DEBUG
		self.ART_LIMIT = ART_LIMIT
		self.data = []
		self.close_nav = close_nav

	def scrap(self):
		"""
		Scraper Work-Flow
		"""
		Navigation.set_scraper_search(Navigation, self.LOCKING_FOR, self.DEBUG, self.driver)
		Navigation.load_page(Navigation, self.ART_LIMIT, self.driver)
		Navigation.page_scroll_up_down(Navigation, self.driver)
		Scraper.page_scrap(Scraper, self.driver, self.DEBUG, self.data)
		Data_manager.save(Data_manager, self.LOCKING_FOR, self.data)
		Navigation.close_nav_func(Navigation, self.close_nav, self.driver)
