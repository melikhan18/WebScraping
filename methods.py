productNameList = []
def getProductName(cimriProducts):
    
    for cimriProduct in cimriProducts:
        product = cimriProduct.find("article")
        productName = product.find("a" , {"class" : "link-detail"}).get("title")
        productNameList.append(productName)
    return productNameList

productUrlList = []
def getProductUrl(cimriProducts):
    
    for cimriProduct in cimriProducts:
        product = cimriProduct.find("article")
        productUrl = product.find("a" , {"class" : "link-detail"}).get("href")
        productUrl = "https://www.cimri.com/" + productUrl
        productUrlList.append(productUrl)
    return productUrlList
productImageList = []
def getProductImage(cimriProducts):
    
    for cimriProduct in cimriProducts:
        product = cimriProduct.find("article")
        productImage = product.find("div" , {"class" : "image-wrapper"})\
            .find("div", {"class" , "m50b2p-0 iHtcZy"}).find("img").get("data-src")
        productImage = "https:" + productImage
        productImageList.append(productImage)
    return productImageList

productList = {}



def getProducts(productNameList, productUrlList,productImageList):
    productsList = []
    products = {}
    productIndex = 0
    for product in productNameList:
        productList["product" + str(productIndex)] = [
            productNameList[productIndex],
            productUrlList[productIndex],
            productImageList[productIndex]]
        productIndex += 1
    products["products"] = productList
    productsList.append(products)
    return productsList

