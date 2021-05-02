# Promotion to apply when a given number of a given product has a special price

from promotion import Promotion
from invalid_cart import InvalidCart

class Multiples(Promotion):
        def __init__(self, sku, batchSize, batchPrice):
                """
                Initialize.

                Parameters:
                - sku: Product SKU ID
                - batchSize: The number of products where the special price should apply
                - batchPrice: The special price for `batchSize` number of products
                """
                super().__init__()
                self.sku = sku 
                self.batchSize = batchSize
                self.batchPrice = batchPrice

        def calculateDiscount(self, productList, cart):
                if not self.sku in cart:
                        return 0
                if not self.sku in productList:
                        raise InvalidCart()
                count = cart[self.sku]
                nominalPrice = count * productList[self.sku]
                batchCount = count // self.batchSize
                remainingCount = count - batchCount * self.batchSize
                promotedPrice = batchCount * self.batchPrice + remainingCount * productList[self.sku]
                discount = nominalPrice - promotedPrice
                return -discount 
