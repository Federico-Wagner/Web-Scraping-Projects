#from selenium.webdriver.common.by import By
from .navigation import *
import requests
import os

def save_imgs(driver, urls):
	"""
	This function will download all images from the given URLs and store them inside a folder named as the profile they
	come from.
	"""
	img_saved = 0
	if (have_access(driver)):
		profile = driver.find_element(By.TAG_NAME, "h2").text
		print(f"Saving {profile}'s images")
		if not (os.path.exists(f"scraped_data\{profile}")):
			os.makedirs(f"scraped_data\{profile}")
		for url in urls:
			try:
				file = requests.get(url, allow_redirects=True)
				open(f"scraped_data\{profile}\{profile}-{img_saved}.jpg", 'wb').write(file.content)
			except:
				continue
			img_saved += 1
	print(f"Process Status: DONE - {img_saved}/{len(urls)} images saved")
