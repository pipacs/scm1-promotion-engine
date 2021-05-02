# Promotion when having 3 of product A's in the cart

from multiples import Multiples
from invalid_cart import InvalidCart

class ThreeOfAFor130(Multiples):
        def __init__(self):
                Multiples.__init__(self, "A", 3, 130)
