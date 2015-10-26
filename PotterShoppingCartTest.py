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

    def test_Buy_Ep1_And_Ep2_Should_Be_190(self):
        """
        Scenario: 第一集買了一本，第二集也買了一本，價格應為100*2*0.95=190
        :return:
        """
        target = PotterShoppingCart.PotterShoppingCart()
        target.pick_up({"Name": "HollyPoter 1", "Cost": 100})
        target.pick_up({"Name": "HollyPoter 2", "Cost": 100})

        # Act
        actual = target.calculate_total_amount()

        expected = 190
        self.assertEqual(expected, actual)

    def test_Buy_Ep1_Ep2_Ep3_Should_Be_270(self):
        """
        Scenario: 一二三集各買了一本，價格應為100*3*0.9=270
        :return:
        """
        target = PotterShoppingCart.PotterShoppingCart()
        target.pick_up({"Name": "HollyPoter 1", "Cost": 100})
        target.pick_up({"Name": "HollyPoter 2", "Cost": 100})
        target.pick_up({"Name": "HollyPoter 3", "Cost": 100})

        # Act
        actual = target.calculate_total_amount()

        expected = 270
        self.assertEqual(expected, actual)

    def test_Buy_Ep1_Ep2_Ep3_Ep4_Should_Be_320(self):
        """
        Scenario: 一二三四集各買了一本，價格應為100*4*0.8=320
                :return:
        """
        target = PotterShoppingCart.PotterShoppingCart()
        target.pick_up({"Name": "HollyPoter 1", "Cost": 100})
        target.pick_up({"Name": "HollyPoter 2", "Cost": 100})
        target.pick_up({"Name": "HollyPoter 3", "Cost": 100})
        target.pick_up({"Name": "HollyPoter 4", "Cost": 100})

        # Act
        actual = target.calculate_total_amount()

        expected = 320
        self.assertEqual(expected, actual)

    def test_Buy_Ep1_Ep2_Ep3_Ep4_Ep5_Should_Be_375(self):
        """
        Scenario: 一次買了整套，一二三四五集各買了一本，價格應為100*5*0.75=375
        :return:
        """
        target = PotterShoppingCart.PotterShoppingCart()
        target.pick_up({"Name": "HollyPoter 1", "Cost": 100})
        target.pick_up({"Name": "HollyPoter 2", "Cost": 100})
        target.pick_up({"Name": "HollyPoter 3", "Cost": 100})
        target.pick_up({"Name": "HollyPoter 4", "Cost": 100})
        target.pick_up({"Name": "HollyPoter 5", "Cost": 100})

        # Act
        actual = target.calculate_total_amount()

        expected = 375
        self.assertEqual(expected, actual)

    def test_Buy_One_Ep1_One_Ep2_And_Two_Ep3_Should_Be_370(self):
        """
        Scenario: 一二集各買了一本，第三集買了兩本，價格應為10030.9 + 100 = 370
        :return:
        """
        target = PotterShoppingCart.PotterShoppingCart()
        target.pick_up({"Name": "HollyPoter 1", "Cost": 100})
        target.pick_up({"Name": "HollyPoter 2", "Cost": 100})
        target.pick_up({"Name": "HollyPoter 3", "Cost": 100})
        target.pick_up({"Name": "HollyPoter 3", "Cost": 100})

        # Act
        actual = target.calculate_total_amount()

        expected = 370
        self.assertEqual(expected, actual)

    def test_Buy_One_Ep1_Two_Ep2_And_Two_Ep3_Should_Be_460(self):
        """
        Scenario: 第一集買了一本，第二三集各買了兩本，價格應為100*3*0.9 + 100*2*0.95 = 460
        :return:
        """
        target = PotterShoppingCart.PotterShoppingCart()
        target.pick_up({"Name": "HollyPoter 1", "Cost": 100})
        target.pick_up({"Name": "HollyPoter 2", "Cost": 100})
        target.pick_up({"Name": "HollyPoter 2", "Cost": 100})
        target.pick_up({"Name": "HollyPoter 3", "Cost": 100})
        target.pick_up({"Name": "HollyPoter 3", "Cost": 100})

        # Act
        actual = target.calculate_total_amount()

        expected = 460
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
