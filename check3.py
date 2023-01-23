
from ast import main
import requests
from bs4 import BeautifulSoup
from csv import writer


File = open("out2.csv", "a")
File_header = ['Prod.Title ','Reting','Availability']
thewrite = writer(File)
thewrite.writerow(File_header)



def main(URL):
	
	HEADERS = ({'User-Agent':
				'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
				'Accept-Language': 'en-US, en;q=0.5'})

	webpage = requests.get(URL, headers=HEADERS)
	soup = BeautifulSoup(webpage.content, "lxml")


		# Creating the Soup Object containing all data
	soup = BeautifulSoup(webpage.content, "lxml")


		# retrieving product title
	try:
			# Outer Tag Object
			title = soup.find("span",
							attrs={"id": 'productTitle'})
			# Inner NavigableString Object
			title_value = title.string
			# Title as a string value
			title_string = title_value.strip().replace(',', '')

	except AttributeError:
			title_string = "NA"
	print("product Title = ", title_string)
	File.write(f"{title_string},") # saving the title in the file



		# retrieving price
	try:
			price = soup.find(
				"span", attrs={'class': 'a-offscreen'}).string.strip().replace(',', '')
	except AttributeError:
			price = "NA"
	print("Products price = ", price)

	# saving
	# File.write(f"{price},")



	# retrieving product rating
	try:
			rating = soup.find('i', attrs={
							'class': 'a-icon a-icon-star a-star-4-5'}).string.strip().replace(',', '')

	except AttributeError:
			rating = soup.find(
							"span", attrs={'class': 'a-icon-alt'}).string.strip().replace(',', '')

	except:
				rating = "NA"
	print("Overall rating = ", rating)

	File.write(f"{rating},")


	#Review_count
	try:
			review_count = soup.find(
				"span", attrs={'id': 'acrCustomerReviewText'}).string.strip().replace(',', '')

	except AttributeError:
			review_count = "NA"
	print("Total reviews = ", review_count)
	File.write(f"{review_count},")


	try:
		asin = soup.find(
				attrs={'class': 'a-size-base-prodDetAttrValue'})

		# asin = soup.find(
		# 		attrs={'id': 'productDetails_detailBullets_section1','class': 'a-size-base prodDetAttrValue'})

	except ArithmeticError:
		asin = "NA"
	print("ASIN = ",asin)

	File.write(f"{asin},\n")

		# closing the file
	File.close()

if __name__ == '__main__':
#   opening our url file to access URLs
	file = open("url.txt", "r")

# iterating over the urls
	for links in file.readlines():
		main(links)

