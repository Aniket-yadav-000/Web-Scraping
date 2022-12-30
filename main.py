# import all the requirement 

import requests
from bs4 import BeautifulSoup
from csv import writer

# web scraping project...

url = "https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi&otracker=nmenu_sub_Electronics_0_Mi"
page = requests.get(url)

soup = BeautifulSoup(page.content,'html.parser')
lists = soup.find_all('div',class_="_3pLy-c row")

# making a new file 
with open('flipkart.csv','w',encoding='utf8',newline='') as f: 
  thewriter = writer(f)
# giving header to csv file
  header = ['Name', 'Description', 'Price']
  thewriter.writerow(header)
  for item in lists:
    name = item.find('div',class_="_4rR01T").text.replace('\n','')
    description = item.find('li',class_="rgWa7D").text.replace('\n','')
    price = item.find('div',class_="_30jeq3 _1_WHN1").text.replace('\n','')
  
# writing content from website into csv
    info = [name,description,price]
    thewriter.writerow(info)
  
  

  



