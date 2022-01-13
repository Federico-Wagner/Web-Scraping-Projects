from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Navigation:
	def set_scraper_search(self, LOCKING_FOR, DEBUG, driver):
		"""
		This function opens the scraping browser, redirects it to the page to scrap and uses the search box built in the page
		"""
		driver.implicitly_wait(3)
		driver.set_window_size(960, 1024)
		driver.get("https://www.carrefour.com.ar/")
		self.close_add(self, driver)

		time.sleep(5)
		try:
			search_box = WebDriverWait(driver,15).until(EC.visibility_of(driver.find_element(
				By.ID, "downshift-1-input")))
			print("search box founded")
		except:
			raise ValueError("error en barra de busqueda")
		search_box.send_keys(LOCKING_FOR)
		search_box.send_keys(Keys.ENTER)
		time.sleep(5)
		self.current_url(self, DEBUG, driver)

	def current_url(self, DEBUG, driver):
		if DEBUG == True:
			print(driver.current_url)

	def close_add(self, driver):
		"""
		Function to close the add pop up
		"""
		try:
			close_add = WebDriverWait(driver,15).until(EC.visibility_of(driver.find_element(
				By.XPATH,"/html/body/div[6]/div[3]/div/div[2]/button")))
			close_add.click()
			print("add closed")
		except:
			print("No add founded")

	def load_page(self, ART_LIMIT, driver):
		"""
		This function will display all products on the screen
		"""
		ART_LIMIT = 800 if ART_LIMIT == 0 else ART_LIMIT	#Carrefour's page limit
		current, total = self.articles_loaded(self, driver)
		i = 0
		while (current < ART_LIMIT) and (current < total):
			self.press_show_more_button(self, driver)
			time.sleep(3 + i * 0.1)  # time increments due to page load speed goes down as we load more data to the page
			current, total = self.articles_loaded(self, driver)
			i += 1

	def articles_loaded(self, driver):
		"""
		This function returns current and total amount of products that are being displayed.
		"""
		try:
			page_section = driver.find_element(
				By.XPATH, "/html/body/div[3]/div/div[1]/div/div[6]/div/div/section")
			art_show_row = page_section.find_element(By.CSS_SELECTOR, "div.c-muted-2")
			art_show = art_show_row.find_element(By.CSS_SELECTOR, "span.b")
			print("Productos cargados:", art_show.text)
			art_aumont = (art_show.text).split(' ')
			total = int(art_aumont[2].replace('.', ''))
			current = int(art_aumont[0].replace('.', ''))
			if len(art_aumont) >1:
				return (current, total)
			else:
				return (total,total)
		except:
			raise ValueError("coudn't find 'art_show' variable on the web page")

	def press_show_more_button(self, driver):
		"""
		This function identifies the "show more button" and hits it
		"""
		try:
			page_section = driver.find_element(
				By.XPATH, "/html/body/div[3]/div/div[1]/div/div[6]/div/div/section")
			show_more_row = page_section.find_element(By.CSS_SELECTOR, "div.vtex-flex-layout-0-x-flexRow--fetch")
			show_more_button = show_more_row.find_element(By.CSS_SELECTOR, "button.pointer[tabindex='0']")
			return show_more_button.send_keys(Keys.ENTER)
		except:
			raise ValueError("error on pressing show more button")

	def page_scroll_up_down(self, driver):
		"""
		This function scrolls al the page up down to ensure every article is correctly loaded
		"""
		page_height = driver.execute_script("return document.body.scrollHeight")
		driver.execute_script("window.scrollTo(0,0)")
		for scroll in range(0,(int(page_height/800))):
			driver.execute_script(f"window.scrollTo(0, {800*scroll})")
			time.sleep(1)

	def close_nav_func(self, close_nav, driver):
		if close_nav:
			driver.close()
