# coding=utf-8


class PotterShoppingCart:
    def __init__(self):
        self.books = []

    def pick_up(self, book):
        self.books.append(book)

    def calculate_total_amount(self):
        total_amount = sum([book['Cost'] for book in self.books])
        discount_map = {1: 1, 2: 0.95, 3: 0.9}
        return total_amount * discount_map.get(len(self.books), 1)
