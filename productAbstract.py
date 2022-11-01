from abc import ABC, abstractmethod
from itertools import product

class Product():
    productId = 0
    productName = ""
    productImage = ""
    productDescription = ""
    productLine = ""

class ProductAbstract(ABC):

    @abstractmethod
    def createProduct(self, product : Product):
        pass

    @abstractmethod
    def editProduct(self):
        pass

    @abstractmethod
    def getProductById(self, productById):
        pass

    @abstractmethod
    def getAllProducts(self):
        pass

    @abstractmethod
    def uploadProductImage(self, productImage):
        pass

    @abstractmethod
    def deleteProduct(self):
        pass

class ProductManager(ProductAbstract):
    def createProduct(self, product: Product):
        print(f"All Product Information \n")
        print(f"Product Name: {product.productName}")
        print(f"Product Line: {product.productLine}")
        print(f"Product ID: {product.productId}")
        print(f"Product image: {product.productImage}")
        print(f"From the product line, this is the product description {product.productDescription}")
    
    def editProduct(self):
        print(f"Editing this product")
    
    def getProductById(self, productById):
        return super().getProductById(productById)
    
    def getAllProducts(self):
        print(f"Getting all products from this product line")

    def uploadProductImage(self, productImage):
        print(f"Product Image")
    
    def deleteProduct(self):
        print(f"This product has been deleted")
    
productManager = ProductManager()
productManager.getAllProducts()

product = Product()
product.productId = 23
product.productName = "Handbag"
product.productLine = "Armani"
product.productImage = "Procut Image"
product.productDescription = "This is a quality handbag, made of leather, it will last you forever and is a perfect investment"


productManager.createProduct(product)