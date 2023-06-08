from bs4 import BeautifulSoup
import requests

url = "https://www.avito.ru/"

def search_announcements(product: int = None, city: int = 'all', delivery: int = '0'):
	if product != None:
		f = open('temp.txt', 'w')
		r = open('temp.txt')
		request = requests.get(url + str(city) + '?q=' + str(product) + '&d=' + str(delivery))
		if str(request) == '<Response [200]>':		
			bs = BeautifulSoup(request.text, "html.parser")
			all_links = bs.find_all('div', class_='iva-item-titleStep-pdebR')
			for link in all_links:
				a = link.find('a', href=True)
				if a:
					f.write(" "+'https://www.avito.ru' + a['href'])
			f.close()	
			x = r.read().split()
			return x
		else:
			return request
	else:
		return 'Вы не ввели название продукта!'
			
def get_price(link: int = None):
	if link != None:
		request = requests.get(link)
		if str(request) == '<Response [200]>':
			bs = BeautifulSoup(request.text, "html.parser")
			prices = bs.find_all('span', class_='styles-module-size_xxxl-A2qfi')
			for price in prices:
				z = price.text.replace('₽', '')
				return z
		else:
			return request
    			
	else:
		return 'Вы не ввели ссылку на продукт!'

def site_status():
	request = requests.get(url)
	return request
