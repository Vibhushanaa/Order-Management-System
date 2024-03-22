#Product Class

class Product:
    def __init__(self, productId: int, productName: str, description: str, price: float, quantityInStock: int, type: str):
        self.productId = productId
        self.productName = productName
        self.description = description
        self.price = price
        self.quantityInStock = quantityInStock
        self.type = type


    #Mutattors
    
    def setProductId(self, productId: int) -> None:
        self.productId = productId

    
    def setProductName(self, productName: str) -> None:
        self.productName = productName

    def setDescription(self, description: str) -> None:
        self.description = description

    def setPrice(self, price: float) -> None:
        self.price = price

    
    def setQuantityInStock(self, quantityInStock: int) -> None:
        self.quantityInStock = quantityInStock

   
    def setType(self, type: str) -> None:
        self.type = type

    #Accessors
    def getProductId(self) -> int:
        return self.productId
    
    def getProductName(self) -> str:
        return self.productName
    
    def getDescription(self) -> str:
        return self.description
    
    def getPrice(self) -> float:
        return self.price
    
    def getQuantityInStock(self) -> int:
        return self.quantityInStock

    def getType(self) -> str:
        return self.type

#Electronics
        
class Electronics(Product):
    def __init__(self, productId: int, productName: str, description: str, price: float, quantityInStock: int, type: str, brand: str, warrantyPeriod: int):
        super().__init__(productId, productName, description, price, quantityInStock, type)
        self.brand = brand
        self.warrantyPeriod = warrantyPeriod
   
   # Muttators
        
    def setBrand(self, brand: str) -> None:
        self.brand = brand

    def setWarrantyPeriod(self, warrantyPeriod: int) -> None:
        self.warrantyPeriod = warrantyPeriod

    #Accessors
        
    def getBrand(self) -> str:
        return self.brand
    
    def getWarrantyPeriod(self) -> int:
        return self.warrantyPeriod

#Class Clothing
class Clothing(Product):
    def __init__(self, productId: int, productName: str, description: str, price: float, quantityInStock: int, type: str, size: str, color: str):
        super().__init__(productId, productName, description, price, quantityInStock, type)
        self.size = size
        self.color = color

    def getSize(self) -> str:
        return self.size

    def setSize(self, size: str) -> None:
        self.size = size

    def getColor(self) -> str:
        return self.color

    def setColor(self, color: str) -> None:
        self.color = color

#Class User
        
class User:
    def __init__(self, userId: int, username: str, password: str, role: str):
        self.userId = userId
        self.username = username
        self.password = password
        self.role = role

    def getUserId(self) -> int:
        return self.userId

    def setUserId(self, userId: int) -> None:
        self.userId = userId

    def getUsername(self) -> str:
        return self.username

    def setUsername(self, username: str) -> None:
        self.username = username

    def getPassword(self) -> str:
        return self.password

    def setPassword(self, password: str) -> None:
        self.password = password

    def getRole(self) -> str:
        return self.role

    def setRole(self, role: str) -> None:
        self.role = role

