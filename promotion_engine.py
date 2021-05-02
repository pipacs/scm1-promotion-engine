# Promotion engine

from promotion import Promotion
from invalid_cart import InvalidCart

class PromotionEngine:
        def __init__(self, productList, activePromotions):
                """
                Initialize with a product list and a list of active promotions.
                
                Parameters:
                - productList: Product unit prices mapped by SKU ID
                - activePromotions: List of Promotion instances
                """
                self.productList = productList
                self.activePromotions = activePromotions
                
                # Set to true to apply the first promotion only, as mentioned in the coding excercise:
                self.applyFirstPromotionOnly = False

        def calculateTotalPrice(self, cart):
                """
                Calculate the cart's total value by applying the promotions in activePromotions
 
                Parameters:
                - cart: Product counts mapped by SKU ID

                Returns: Actual price of the cart

                Throws: InvalidCart if the cart contains invalid items
                """
                price = self.calculateNominalPrice(cart)
                for promotion in self.activePromotions:
                        discount = promotion.calculateDiscount(self.productList, cart)
                        price += discount
                        if self.applyFirstPromotionOnly and discount != 0:
                                break 
                return price

        def calculateNominalPrice(self, cart):
                """
                Calculate the nominal price of the cart, without applying any promotions
                
                Parameters:
                - cart: Product counts mapped by SKU ID

                Returns: Nominal price of the cart

                Throws: InvalidCart if the cart contains invalid items
                """
                total = 0
                for (sku, count) in cart.items():
                        if not sku in self.productList.keys():
                                raise InvalidCart()
                        total += self.productList[sku] * count 
                return total
