# Promotion when having 3 of product A's in the cart

from promotion import Promotion
from invalid_cart import InvalidCart

class ThreeOfAFor130(Promotion):
        def value(self, productList, cart):
                if not "A" in cart or cart["A"] < 3:
                        return 0
                if not "A" in productList:
                        raise InvalidCart()
                count = cart["A"]
                nominalPrice = count * productList["A"]
                promotedPrice = 130 + (count - 3) * productList["A"]
                discount = nominalPrice - promotedPrice
                return -discount 

