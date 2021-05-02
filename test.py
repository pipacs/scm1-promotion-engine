# Unit test runner for SCM Coding Test 1: Promotion Engine

from promotion import Promotion
from promotion_engine import PromotionEngine
from three_of_a_for_130 import ThreeOfAFor130
from two_of_b_for_45 import TwoOfBFor45

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
 
        # Tests of individual promotions
        testCase("Testing 'Three of A for 130 with 5 A'", productList, activePromotions, {"A": 5}, 230)
        testCase("Testing 'Three of A for 130 with 2 A'", productList, activePromotions, {"A": 2}, 100)
        testCase("Testing 'Two of B for 45' with 1 B", productList, activePromotions, {"B": 1}, 30)
        testCase("Testing 'Two of B for 45' with 5 B", productList, activePromotions, {"B": 5}, 120)

        # Tests in the coding excercise
        testCase("Testing Cart A", productList, activePromotions, {"A": 1, "B": 1, "C": 1}, 100)
        testCase("Testing Cart B", productList, activePromotions, {"A": 5, "B": 5, "C": 1}, 370)
        testCase("Testing Cart C", productList, activePromotions, {"A": 3, "B": 5, "C": 1, "D": 1}, 280)