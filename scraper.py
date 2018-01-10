
import urllib.request

from bs4 import BeautifulSoup

stock_request=input("enter the stock code of the stock you want to see \n")
webpage='https://www.bloomberg.com/quote/'+stock_request+':US'

page=urllib.request.urlopen(webpage)
soup=BeautifulSoup(page, 'html.parser')
company_name=soup.find('h1', attrs={'class':'companyName__99a4824b'})
price_box=soup.find('span' ,attrs={'class':'priceText__1853e8a5'})
price_change_box=soup.find('span' ,attrs={'class':'changeAbsolute__395487f7'})
price_percent_change_box=soup.find('span', attrs={'class':'changePercent__2d7dc0d2'})
try:
    price=price_box.text.strip()
    name=company_name.text.strip()
    price_change=price_change_box.text.strip()
    price_percent_change=price_percent_change_box.text.strip()
    print('\n'+name)
    print(price)
    print(price_change)
    print(price_percent_change)
except Exception:
    print("No stock under that name found!")


