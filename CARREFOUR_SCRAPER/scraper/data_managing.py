import numpy as np
import pandas as pd
from datetime import date

class Data_manager:
	def manage_scraped_row(self, art_price, art_desc, DEBUG, data):
		"""
		This function sorts the data scraped to prettify the data output
		"""
		row = []
		for price in art_price:		#CASE: no descount price published
			if len(art_price) == 1:
				row.append(np.NaN)
			elif len(art_price) == 0: #CASE: no price published
				for _ in range(2):
					row.append(np.NaN)
			row.append(price.text)
		for name in art_desc:
			row.append(name.text)
		if DEBUG == True:
			print(row)
		data.append(row)

	def save(self, LOCKING_FOR, data):
		"""
		This function converts the "data" array and stores into an .csv file named as the search and the date it was scraped
		"""
		print('-' * 20, 'DataFrame: Saving', '-' * 20)
		df = pd.DataFrame(data=data, columns=["precio-dto", "precio-lista", "descripcion"])
		today = date.today().strftime('%d-%m-%Y')
		df.to_csv("scraped_data/"+LOCKING_FOR + '_' + today + '.csv')
		print("DONE")
