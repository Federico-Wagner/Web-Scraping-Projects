from scraper import main

if __name__ == '__main__':
	#################### USER EDITABLE PART (START) ###################
	user_name = "fede.wag"														# Your INSTAGRAM's USER NAME
	password = "fedemara"														# Your INSTAGRAM's PASSWORD
	look_up_for = ["porsche","audi","McLaren"]
	profiles_to_scrap_per_search = 1									# Profiles to scrap for each search
	max_photos = 250  												  	# Limits the amount of photos to scrap for each profile
	##################### USER EDITABLE PART (END) #####################

	search = main.Instagram_scraper(user_name, password, look_up_for,max_photos, profiles_to_scrap_per_search, DEBUG=False, close_nav=False).scrap()

