from cgitb import strong 
from requests import get 
from bs4 import BeautifulSoup 
 
URL = "https://ek.ua/ua/list/22/"   
 
page = get(URL) 
 
soup = BeautifulSoup(page.content,  "html.parser") 
 
 
with open("katalog.csv", "w", encoding="UTF=8") as file: 
        prod_list = soup.find(class_="main-part-content") 
        form = prod_list.find("form") 
        for div in form.find("div"): 
            table_1 = div.find("table") 
            tr = table_1.find("tr") 
            table_2 = tr.find("table") 
            a = table_2.find("a") 
            name_a = a.find(text=True, recursive=False)
            tr = table_1.find("tr")
            td = tr.find("td")
            div = td.find("div")
            span = div.find("span")
            name_span = span.find(text=True, recursive=False)
            file.write(f"{name_a} -- {name_span}")


     

 


   




