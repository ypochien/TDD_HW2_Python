# coding=utf-8

class PotterShoppingCart:
    def __init__(self):
        self.books = []

    def pick_up(self, book):
        self.books.append(book)

    def calculate_total_amount(self):
        temp_books = self.books
        discount_amount = 0.0
        while len(temp_books) > 0:
            distinct_books = {v['Name']: v for v in temp_books}.values()
            discount_amount += self.__calculate_discount_by_books(distinct_books)
            for x in distinct_books:
                temp_books.remove(x)

        return discount_amount

    @staticmethod
    def __calculate_discount_by_books(distinct_books):
        total_amount = sum([book['Cost'] for book in distinct_books])
        discount_map = {1: 1, 2: 0.95, 3: 0.9, 4: 0.8, 5: 0.75}
        return total_amount * discount_map.get(len(distinct_books), 1)
