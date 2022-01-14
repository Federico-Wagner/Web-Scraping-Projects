from selenium import webdriver
from .scraping import Scraper
from .navigation import Navigation
from .data_managing import Data_manager

class Instagram_scraper:
	def __init__(self, user_name, password, look_up_for, profile_amount=1, DEBUG=False, close_nav=False):
		self.PATH = "scraper\chromedriver.exe"
		self.driver = webdriver.Chrome(self.PATH)
		self.user_name = user_name
		self.password = password
		self.DEBUG = DEBUG
		self.close_nav = close_nav
		self.look_up_for = look_up_for
		self.profile_amount = profile_amount

	def scrap(self):
		"""
		Scraper Work-Flow
		"""
		Navigation.open_instagram(Navigation, self.driver)
		Navigation.log_in(Navigation, self.driver, self.user_name, self.password)
		Navigation.close_pop_ups(Navigation, self.driver)
		for profile in self.look_up_for:
			pages_to_scrap = Navigation.search(Navigation, self.driver, profile, self.profile_amount)
			for page in pages_to_scrap:
				self.images = []
				Scraper.scrap_page(Scraper, page, self.driver, self.images)
				Data_manager.save_imgs(Data_manager, self.driver, self.images)
