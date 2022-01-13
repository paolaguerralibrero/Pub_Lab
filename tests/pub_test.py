import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Lion", 200.00)

    def test_pub_has_name(self):
        self.assertEqual("The Lion", self.pub.name)

    def test_check_till_amount(self):
        self.assertEqual(200.00, self.pub.till)

    def test_till_is_not_empty(self):
        self.pub.increase_till(50)
        self.assertEqual(250.00, self.pub.till)

    def test_add_drink(self):
        drink1 = Drink("Stella", 5.00, 4)
        drink2 = Drink("Tennent's", 3.50, 2)
        self.pub.add_drink(drink1)
        self.pub.add_drink(drink2)
        self.assertEqual(2, self.pub.drinks_count())

    def test_check_drink_name(self):
        drink1 = Drink("Stella", 5.00, 4)
        self.pub.add_drink(drink1)
        self.assertEqual("Stella", self.pub.drinks[0].name)

    def test_sell_drink(self):
        drink1 = Drink("Stella", 5.00, 4)
        person = Customer("Cleyra", 100.00, 32, 0)
        self.pub.sell_drink(person, drink1)
        self.assertEqual(205.00, self.pub.till)

    def test_check_age(self):
        person = Customer("Delia", 200, 28, 0)
        self.pub.verify_age(person)
        self.assertEqual(True, self.pub.verify_age(person))

    def test_drunkenness_level(self):
        person = Customer("Paola", 10, 34, 0)
        drink1 = Drink("Stella", 5.00, 4)
        self.pub.get_a_drink(person, drink1)
        self.assertEqual(4, self.pub.get_a_drink(person, drink1))

    def test_if_customer_too_drunk(self):
        person = Customer("Paola", 10, 34, 50)
        drink1 = Drink("Stella", 5.00, 4)
        self.pub.sell_drink(person, drink1)
        self.assertEqual("You're too drunk, pal!", self.pub.sell_drink(person, drink1))
