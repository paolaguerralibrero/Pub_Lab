# from customer import Customer

class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def add_drink(self, drink):
        self.drinks.append(drink)

    def drinks_count(self):
        return len(self.drinks)

    def increase_till(self, amount):
        self.till += amount

    def sell_drink(self, customer, drink):
        if customer.drunkenness <= 40:  
            customer.wallet -= drink.price
            self.till += drink.price
        else: 
            return "You're too drunk, pal!"

    def verify_age(self, customer):
        if customer.age >= 18:
            return True

    def get_a_drink(self, customer, drink):
        customer.drunkenness = 0
        customer.drunkenness += drink.alcohol_level
        return customer.drunkenness


