from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from .data_managing import Data_manager
from .navigation import Navigation
import time

class Scraper:
	def scrap_page(self, page, driver, images):
		driver.get(page)
		if (Navigation.have_access(Navigation, driver)):
			self.scrap_page_image_publications(Scraper, driver, images)
		else:
			print(f"Profile it's not public {page}")

	def scrap_page_image_publications(self, driver, images):
		page_height = driver.execute_script("return document.body.scrollHeight")
		last_page_height = 0
		i = 1
		while (last_page_height < page_height):
			driver.execute_script(f"window.scrollTo(0,{2000*i})")
			time.sleep(2)  # load time
			last_page_height = page_height
			page_height = driver.execute_script("return document.body.scrollHeight")
			Data_manager.get_imgs(Scraper, driver,images)
			i += 1
		print("got imgs: ", len(images))

