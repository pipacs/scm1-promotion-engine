# Promotion engine

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

        def calculateTotalPrice(self, cart):
                """Calculate the cart's total value by applying the first valid promotion in activePromotions"""
                return 0
