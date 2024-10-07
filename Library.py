# define the book class
class Book:
    # defining and initializing attributes (constructor)
    def __init__(self, title, author, year, price, stoplist=False):
        self.title = title
        self.author = author
        self.year = year
        self.price = price
        self.stoplist = stoplist #defaults to False
        
    # defining the get_info method
    def get_info(self):
        """prints: author, title, year, price, stoplist"""
        book_info = f'Author: {self.author},\nTitle: {self.title},\nYear: {self.year},\nPrice: {self.price},\nStoplist: {self.stoplist}'
        print(book_info)
    
    # defining a method that finds the most expensive book in a list of books
    def find_most_expensive(book_list):
        """finds the most expensive book in the given list"""
        return max(book_list, key=lambda x: x.price)
        
    
    
    # defining the stoplist method
    def set_stoplist(self, boolean):
        """sets the boolean values for the book's stoplist"""
        # updating th estoplist attribute to the boolean value passed as a parameter
        self.stoplist = boolean
    
    
    # defining the censor method
    def censor(self, author_name, boolean):
        """takes a name of an author and a boolean value and checks the book for which it is called"""
        # checls if the current author matches the author_name provided
        if self.author == author_name:
            self.stoplist = boolean
            
    