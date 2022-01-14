from scraper import main

#################### USER EDITABLE PART (START) ####################
user_name = "fede.wag"
password = "fedemara"
look_up_for = ["cami","sofi","ana"]  #"cami.corrales.5"	#"crystalycrystalina"
profiles_to_scrap= 4

#################### USER EDITABLE PART (END) ####################

busqueda = main.Instagram_scraper(user_name, password, look_up_for, profiles_to_scrap, DEBUG=False, close_nav=True)
busqueda.scrap()
