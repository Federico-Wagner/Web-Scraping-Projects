from selenium import webdriver
from .data_managing import *
from .scraping import *
from .navigation import *

import time
class Instagram_scraper:
	def __init__(self, user_name, password, look_up_for,max_photos, profile_amount, DEBUG=False, close_nav=False):
		self.PATH = "scraper\chromedriver.exe"
		self.driver = webdriver.Chrome(self.PATH)
		self.user_name = user_name
		self.password = password
		self.DEBUG = DEBUG
		self.close_nav = close_nav
		self.look_up_for = look_up_for
		self.profile_amount = profile_amount
		self.max_photos = max_photos

	def scrap(self):
		"""
		Scraper Work-Flow
		"""
		open_instagram(self.driver)
		log_in(self.driver, self.user_name, self.password)
		close_pop_ups(self.driver)
		for profile in self.look_up_for:
			pages_to_scrap = search(self.driver, profile, self.profile_amount)
			for page in pages_to_scrap:
				open_profile(self.driver, page)
				if have_access(self.driver, page):
					profile_data = scrap_profile(self.driver, self.max_photos)

					start = time.perf_counter()
					save_imgs(self.driver, profile_data)
					end = time.perf_counter()
					print("Time: ", end - start, "seconds")
