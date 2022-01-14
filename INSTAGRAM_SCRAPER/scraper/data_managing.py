from selenium.webdriver.common.by import By
from .navigation import Navigation
import requests
import os

class Data_manager:
	def get_imgs(self, driver, images):
		publications = driver.find_element(By.CSS_SELECTOR, "article.ySN3v").find_elements(By.CSS_SELECTOR, "div.eLAPa")
		for publication in publications:
			url = publication.find_element(By.TAG_NAME, "img").get_attribute('src')
			if url not in images:
				images.append(url)

	def save_imgs(self, driver, images):
		img_saved = 0
		if (Navigation.have_access(Navigation, driver)):
			profile = driver.find_element(By.TAG_NAME, "h2").text
			if not (os.path.exists(f"scraped_data\{profile}")):
				os.makedirs(f"scraped_data\{profile}")
			for url in images:
				try:
					file = requests.get(url, allow_redirects=True)
					open(f"scraped_data\{profile}\{profile}-{img_saved}.jpg", 'wb').write(file.content)
				except:
					continue
				img_saved += 1
		print(f"Process Status: DONE - {img_saved}/{len(images)} images saved")
