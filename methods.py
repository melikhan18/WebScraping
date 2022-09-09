def getProductName(cimriProducts):
    productNameList = []
    for cimriProduct in cimriProducts:
        product = cimriProduct.find("article")
        productName = product.find("a" , {"class" : "link-detail"}).get("title")
        productNameList.append(productName)
    return productNameList


def getProductUrl(cimriProducts):
    productUrlList = []
    for cimriProduct in cimriProducts:
        product = cimriProduct.find("article")
        productUrl = product.find("a" , {"class" : "link-detail"}).get("href")
        productUrl = "https://www.cimri.com/" + productUrl
        productUrlList.append(productUrl)
    return productUrlList

def getProductImage(cimriProducts):
    productImageList = []
    for cimriProduct in cimriProducts:
        product = cimriProduct.find("article")
        productImage = product.find("div" , {"class" : "image-wrapper"})\
            .find("div", {"class" , "m50b2p-0 iHtcZy"}).find("img").get("data-src")
        productImage = "https:" + productImage
        productImageList.append(productImage)
    return productImageList

productList = {}
productsList = []
products = {}
def getProducts(productNameList, productUrlList,productImageList ):
    
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

