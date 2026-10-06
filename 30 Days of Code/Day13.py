# Book is an abstract base class with an abstract display method. MyBook extends it with
# a price and implements display to print the title, author, and price.

from abc import ABCMeta, abstractmethod

class Book(object, metaclass=ABCMeta):

    def __init__(self, title, author):

        self.title = title
        self.author = author

    @abstractmethod
    def display(self):
        pass

class MyBook(Book):

    def __init__(self, title, author, price):

        super().__init__(title, author)
        self.price = price

    def display(self):

        print(f"Title: {self.title}")

        print(f"Author: {self.author}")

        print(f"Price: {self.price}")

if __name__ == '__main__':

    title = input()
    author = input()

    price = int(input())

new_novel1 = MyBook(title, author, price)

new_novel1.display()