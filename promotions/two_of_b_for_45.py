# Promotion when having 3 of product A's in the cart

from promotion import Promotion
from invalid_cart import InvalidCart
from multiples import Multiples

class TwoOfBFor45(Multiples):
        def __init__(self):
                Multiples.__init__(self, "B", 2, 45)
