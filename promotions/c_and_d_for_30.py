# Promotion to apply when products C and D are in the shopping cart both

from promotion import Promotion
from invalid_cart import InvalidCart

class CAndDFor30(Promotion):
        def calculateDiscount(self, productList, cart):
                if not ("C" in cart and "D" in cart):
                        return 0
                if not "C" in productList or not "D" in productList:
                        raise InvalidCart()

                cCount = cart["C"]
                cUnitPrice = productList["C"]
                dCount = cart["D"]
                dUnitPrice = productList["D"]
                promotedCount = min(cCount, dCount)

                nominalPrice = cCount * cUnitPrice + dCount * dUnitPrice
                promotedPrice = (cCount - promotedCount) * cUnitPrice + (dCount - promotedCount) * dUnitPrice + promotedCount * 30
                return nominalPrice - promotedPrice
