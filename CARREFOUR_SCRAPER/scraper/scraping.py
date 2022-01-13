from selenium.webdriver.common.by import By
import time
from .data_managing import Data_manager

class Scraper:
	def page_scrap(self, driver, DEBUG, data):
		"""
		This function scrapes all articles that where loaded on the page
		"""
		time.sleep(3) #extra time to load the last products
		articulos = (driver.find_elements(By.TAG_NAME, 'article'))[1:]
		print('-' * 20, "Got", len(articulos), "products", '-' * 20)
		print('-' * 20, "Sorting Data", '-' * 20)
		for articulo in articulos:
			art_price = articulo.find_elements(By.CLASS_NAME,'lyracons-carrefourarg-product-price-1-x-currencyContainer')
			art_desc = articulo.find_elements(By.TAG_NAME, 'h1')
			Data_manager.manage_scraped_row(Data_manager, art_price, art_desc, DEBUG, data)
