from scraper import main

#################### USER EDITABLE PART (START) ####################
LOCKING_FOR = "bebidas"		#Enter product
PRODUCT_LIMIT = 150			#for faster develping- defoult value: 0
#################### USER EDITABLE PART (END) ####################

busqueda = main.Carrefour_scraper(LOCKING_FOR, PRODUCT_LIMIT, DEBUG=False, close_nav=True)
busqueda.scrap()
