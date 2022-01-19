from selenium.webdriver.common.by import By
import time

def scrap_profile(driver, max_photos):
	"""
	This function navigates through the profile scrolling down and taking every image URL
	*tricky function due to the way instagram has optimised the profile page, when loading new publications, it tooks
	out old ones from the HTML*
	"""
	images_url = []
	page_height = driver.execute_script("return document.body.scrollHeight")
	last_page_height = 0
	i = 1
	img_count = 0
	while (last_page_height < page_height) and (img_count < max_photos):
		driver.execute_script(f"window.scrollTo(0,{2000*i})") 					# Scroll Down
		time.sleep(2)  															# load time
		last_page_height = page_height
		page_height = driver.execute_script("return document.body.scrollHeight")
		img_count += 12															# amount of new pub loaded for each scroll
		get_imgs_urls(driver, images_url) if i % 4 == 0 else None				# optimization
		i += 1
	get_imgs_urls(driver, images_url)
	print("got imgs: ", len(images_url))
	return images_url

def get_imgs_urls(driver, images):
	"""Function in charge of taking images URLs"""
	try:
		publications = driver.find_element(By.CSS_SELECTOR, "article.ySN3v").find_elements(By.CSS_SELECTOR, "div.eLAPa")
	except:
		raise ValueError("Couldn't get publications")
	for publication in publications:
		url = publication.find_element(By.TAG_NAME, "img").get_attribute('src')
		if url not in images:
			images.append(url)
