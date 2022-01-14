from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException

class Navigation:
	def open_instagram(self, driver):
		driver.implicitly_wait(3)
		driver.set_window_size(670, 1024)
		driver.get("https://www.instagram.com/")
		time.sleep(1)

	def log_in(self, driver, user_name, password):
		user_name_box = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
		user_pass_box = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
		user_name_box.send_keys(user_name)
		user_pass_box.send_keys(password)
		time.sleep(0.5)
		WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.y3zKF"))).click()

	def close_pop_ups(self, driver):
		WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
		WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

	def search(self, driver, look_up_for, profile_amount):
		search_bar = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder = "Search"]')))
		search_bar.send_keys(look_up_for)
		results = driver.find_element(By.CLASS_NAME, "fuqBx ").find_elements(By.CSS_SELECTOR, "a.-qQT3")
		profile_amount = len(results) if profile_amount>len(results) else profile_amount
		for result in results[:profile_amount]:
			print(result.find_element(By.CLASS_NAME, "uL8Hv").text) #result name
			print(result.get_attribute('href'))						#result link
		pages_to_scrap = [result.get_attribute('href') for result in results[:profile_amount]]
		return pages_to_scrap

	def have_access(self, driver):
		try:
			driver.find_element(By.CSS_SELECTOR, "h2.rkEop")
		except NoSuchElementException:
			return True
		return False

