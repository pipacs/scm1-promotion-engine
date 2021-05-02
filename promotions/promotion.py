# Base Promotion type

class Promotion:
        """A promotion that can be applied to a shopping cart"""

        def calculateDiscount(self, productList, cart):
                """
                Calculate the discount for the given cart and product list.
                
                Parameters:
                - productList: Product unit prices mapped by SKU ID
                - cart: Product counts mapped by SKU ID

                Returns: The discount to apply to the cart's nominal value
                """
                return 0
