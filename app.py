from bs4 import BeautifulSoup
import requests
import json
from methods import getProductImage, getProductName, getProductUrl,getProducts


url='https://www.cimri.com/cep-telefonu'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
cimriProducts = soup.findAll("div" , {"id" : "cimri-product"})

getProduct = getProducts(
    getProductName(cimriProducts),
    getProductUrl(cimriProducts),
    getProductImage(cimriProducts)
    )

with open("sample.json", "w") as outfile:
    json.dump(getProduct, outfile)