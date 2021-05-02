# Unit test runner for SCM Coding Test 1: Promotion Engine

from promotion import Promotion
from promotion_engine import PromotionEngine

class ThreeOfAFor130(Promotion):
        pass

class TwoOfBFor45(Promotion):
        pass

class CAndDFor30(Promotion):
        pass 

def testCase(name, productList, activePromotions, cart, expected):
        """Test applying active promotions to a cart"""
        promotionEngine = PromotionEngine(productList, activePromotions)
        actual = promotionEngine.calculateTotalPrice(cart)
        if expected == actual:
                print(name, "PASSED")
        else:
                print(name, "FAILED: Expected %f, actual: %f" % (expected, actual))
        

if __name__ == "__main__":
        productList = {
                "A": 50,
                "B": 30,
                "C": 20,
                "D": 15
        }
        activePromotions = [
                ThreeOfAFor130(),
                TwoOfBFor45(),
                CAndDFor30(),
        ]
        cartA = {
                "A": 1,
                "B": 1,
                "C": 1
        }
        cartB = {
                "A": 5,
                "B": 5,
                "C": 1,
        }
        cartC = {
                "A": 3,
                "B": 5,
                "C": 1,
                "D": 1,
        }
        testCase("Testing Cart 1", productList, activePromotions, cartA, 100)
        testCase("Testing Cart 2", productList, activePromotions, cartB, 370)
        testCase("Testing Cart 3", productList, activePromotions, cartC, 280)