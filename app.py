from bs4 import BeautifulSoup
import requests
import json
from methods import getProductImage, getProductName, getProductUrl,getProducts

url='https://www.cimri.com/saat-moda-taki?page=1'

def startProject(url):
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    cimriProducts = soup.findAll("div" , {"id" : "cimri-product"})

    getProduct = getProducts(
    getProductName(cimriProducts),
    getProductUrl(cimriProducts),
    getProductImage(cimriProducts)
    )
        
    return getProduct
index = 1
while(index < 50):
    getProduct = startProject(url)
    url = url.replace("?page=" + str(index) , "?page=" + str(index+1))
    print("Şuanda veri çekilen adres : " + url)
    index += 1

with open("sample.json", "w") as outfile:
    json.dump(getProduct, outfile)