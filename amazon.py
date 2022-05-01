import time
import requests
from bs4 import BeautifulSoup


#BAZI ÜRÜNLERDE PRİCE ETİKETİNDEN DOLAYI ÇALIŞMAYABİLİYOR.
def Amazon(url,price):
    
    header ={                                                                 #Bilgisayarın User-Agentini kullandık.
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"

    }

    page = requests.get(url,headers=header)                                    #Amazon sayfasına istek attık.
    htmlPage = BeautifulSoup(page.content,'html.parser')                       #Amazon sayfasını html kodlarını aldık.
    productTitle = htmlPage.find("span", attrs={"id":"productTitle"}).getText() #Ürünün adını aldık
    productPrice = htmlPage.find("span", attrs={"class":"a-offscreen"}).getText()  #Ürünün fiyatını aldık.
    convertedPrice = float(productPrice.replace("$","").replace(",","."))


    if (convertedPrice <  price ):                                             #if-else koyarak indirimde bildirim gelicektir
        print(productTitle,"-","Ürün indirimdedir.")
    
    else :
        print(productTitle,"-","Ürün indirimde değildir.")



a ="https://www.amazon.com/Duracell-Alkaline-Batteries-Convenient-Resealable/dp/B07RN9SJ4L/ref=sr_1_1_sspa?keywords=amazonbasics&pd_rd_r=9f368aa1-e9fc-4a33-b496-0fc3311b2746&pd_rd_w=WgjT0&pd_rd_wg=BQK6T&pf_rd_p=9349ffb9-3aaa-476f-8532-6a4a5c3da3e7&pf_rd_r=GB9SYZBCZFWM5HHHH83V&qid=1647421424&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFGWjdMWEtQQVRQT1ImZW5jcnlwdGVkSWQ9QTA0MzgyMDExRjYzNTVLUzUyN01EJmVuY3J5cHRlZEFkSWQ9QTA4NjY4MTgxT0ZKRVhWNDhSRFJaJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="

Amazon(a,50)