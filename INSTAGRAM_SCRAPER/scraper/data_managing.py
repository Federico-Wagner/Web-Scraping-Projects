from .navigation import *
import requests
import os
import multiprocessing

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
		img_saved = multi_proces(urls, profile)		# multiprocessing implementation
	print(f"Process Status: DONE - {img_saved}/{len(urls)} images saved")

def multi_proces(urls, profile):
	"""
	Function to implement multiprocessing to the Download and Save operations
	"""
	img_saved = 0
	if __name__ != '__main__':			# line needed for the sake of getting this NOT to crash
		processes = []
		for url in urls:				# Creates one process for each image it will download
			try:
				process = multiprocessing.Process(target=download_save, args=[url, profile, img_saved])
				processes.append(process)
				img_saved += 1
			except:
				continue
		for proce in processes:
			proce.start()
		for proce in processes:
			proce.join()
	return img_saved

def download_save(url, profile,img_saved):
	file = requests.get(url, allow_redirects=True)  # Download
	open(f"scraped_data\{profile}\{profile}-{img_saved}.jpg", 'wb').write(file.content)  # Save

