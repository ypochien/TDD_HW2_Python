# coding=utf-8
import unittest

from PotterShoppingCart import PotterShoppingCart


class PotterShoppingCartTEST(unittest.TestCase):
    def test_Buy_Ep1_Should_Be_100(self):
        """
        Scenario: 第一集買了一本，其他都沒買，價格應為100*1=100元
        :return:
        """

        # Arrange
        target = PotterShoppingCart.PotterShoppingCart()
        target.pick_up({"Name": "HollyPoter 1", "Cost": 100})

        # Act
        actual = target.calculate_total_amount()

        # Assert
        expected = 100
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
