from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import numpy as np
import pandas as pd
from datetime import date
import time

class Carrefour_scraper:
	def __init__(self,LOCKING_FOR, ART_LIMIT ,DEBUG=False, close_nav=True):
		self.PATH = "C:\webDriver\chromedriver.exe"
		self.driver = webdriver.Chrome(self.PATH)
		self.LOCKING_FOR = LOCKING_FOR
		self.DEBUG = DEBUG
		self.ART_LIMIT = ART_LIMIT
		self.data = []
		self.close_nav = close_nav

	def scrap(self):
		self.set_scraper_search()
		self.load_page()
		self.page_scrap()
		self.save()

	def set_scraper_search(self):
		"""
		This function opens the scraping browser, redirects it to the page to scrap and uses the search box built in the page
		"""
		self.driver.get("https://www.carrefour.com.ar/")
		time.sleep(0.5)
		if self.DEBUG == True:
			print(self.driver.current_url)
		search_box = self.driver.find_element(By.ID, "downshift-1-input")
		search_box.send_keys(self.LOCKING_FOR)
		search_box.send_keys(Keys.ENTER)
		time.sleep(7)
		if self.DEBUG == True:
			print(self.driver.current_url)

	def art_loaded(self):
		"""
		This function it's a fix for alocating the amount of products that are beeing displayed on the page among
		diferent searchs on this page html structure varies.
		"""
		try:
			art_show = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div/div[6]/div/div/section/div[2]/div/div[3]/section/div/div/div/div[7]/div/span/span")
		except:
			art_show = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div/div[6]/div/div/section/div[2]/div/div[2]/section/div/div/div/div[7]/div/span/span")
		return (art_show)

	def load_page(self):
		"""
		This page will hit the "show more" button built in the page until all the products are loaded
		"""
		art_show = self.art_loaded()
		print("Productos cargados:", art_show.text)
		art_aumont = (art_show.text).split(' ')
		total = int(art_aumont[2].replace('.', ''))
		i = 0
		while (int(art_show.text.split(' ')[0]) < self.ART_LIMIT) and (int(art_show.text.split(' ')[0]) < total):
			try:
				show_more_button = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div/div[6]/div/div/section/div[2]/div/div[3]/section/div/div/div/div[9]/div/div/div/div/div/button")
			except:
				show_more_button = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div/div[6]/div/div/section/div[2]/div/div[2]/section/div/div/div/div[9]/div/div/div/div/div/button")
			show_more_button.send_keys(Keys.ENTER)
			time.sleep(3.5 + i * 8 / 80)  # time increments due to page load speed goes down as we load more data to the page
			art_show = self.art_loaded()
			if len(art_show.text.split(' '))>1:
				total = int(art_show.text.split(' ')[2]) #refresh total because of page bug
			print("Productos cargados:", art_show.text)
			i += 1

	def page_scrap(self):
		"""
		This function scrapes all articles that where loaded on the page
		"""
		articulos = (self.driver.find_elements(By.TAG_NAME, 'article'))[1:]
		print('-' * 20, "Got", len(articulos), "products", '-' * 20)
		for articulo in articulos:
			row = []
			art_price = articulo.find_elements(By.CLASS_NAME,'lyracons-carrefourarg-product-price-1-x-currencyContainer')
			art_desc = articulo.find_elements(By.TAG_NAME, 'h1')
			for price in art_price:
				if len(art_price) == 1:
					row.append(np.NaN)
				row.append(price.text)
			for name in art_desc:
				row.append(name.text)
			if self.DEBUG == True:
				print(row)
			self.data.append(row)
		if self.close_nav:
			self.driver.close()

	def save(self):
		"""
		This function converts the "data" array and stores into an .csv file named as the search and the date it was scraped
		"""
		print('-' * 20, 'DataFrame: Saving', '-' * 20)
		df = pd.DataFrame(data=self.data, columns=["precio-dto", "precio-lista", "descripcion"])
		today = date.today().strftime('%d-%m-%Y')
		df.to_csv(self.LOCKING_FOR + '_' + today + '.csv')
		print("DONE")


vinos = Carrefour_scraper('mermelada',125,DEBUG=False,close_nav=False)

vinos.scrap()