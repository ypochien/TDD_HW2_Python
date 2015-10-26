# coding=utf-8


class PotterShoppingCart:
    def __init__(self):
        self.books = []

    def pick_up(self, book):
        self.books.append(book)

    def calculate_total_amount(self):
        return sum([book['Cost'] for book in self.books])
