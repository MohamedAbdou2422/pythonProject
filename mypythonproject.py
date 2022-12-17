import requests
from bs4 import BeautifulSoup as bss4
# my project url
url = requests.get("https://2b.com.eg/ar/home-appliances/tvs.html")
soup= bss4(url.content,"html.parser")
#product details include productname,productPrice,ProductRate,ProductAvaliabilty
myproducts=soup.find_all("div",{"class":"product details product-item-details"})
#loop to get the title,price,rate,notavailable for every product
for i in myproducts:
    #get title of product
   Tvs_title=i.find("strong",{"class","product name product-item-name"})
    #get price of product
   Tvs_price=i.find("div",{"class":"price-box price-final_price"})
    #get rate of product
   Tvs_ratings=i.find("div",{"class":"rating-result"})
    #get the availabilityOfProduct
   print("the product title:")
   print(f"{Tvs_title.text}".replace('\n',''))
   print(f"the product price:{Tvs_price.text}".replace('\n',''))
   print(f"the product rate:{Tvs_ratings.text}".replace('\n',''))
