# Promotion when having 3 of product A's in the cart

from promotion import Promotion
from invalid_cart import InvalidCart

class TwoOfBFor45(Promotion):
        def value(self, productList, cart):
                if not "B" in cart:
                        return 0
                if not "B" in productList:
                        raise InvalidCart()
                count = cart["B"]
                nominalPrice = count * productList["B"]
                promotedCount = count // 2
                remainingCount = count - promotedCount * 2
                promotedPrice = promotedCount * 45 + remainingCount * productList["B"]
                discount = nominalPrice - promotedPrice
                return -discount 

