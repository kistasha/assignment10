# importing the library module
import Library
# creating a list of different books 
book_list = [Library.Book("The Alchemist","Paulo Coehlo", 1988, 12.99), Library.Book("The Da Vinci Code","Dan Brown", 2003, 14.25), Library.Book("One Hundred Years of Solitude","Gabriel García Márquez", 1967, 15.99), Library.Book("Rich Dad Poor Dad","Robert T. Kiyosaki", 1997, 16.99)]

# running the class methods for the books and for the list as a whole >>
print()
# get_info
print("Information about the books:")
for book in book_list:
    book.get_info()
    print()
    
# finding most expensive
print()
print()
most_expensive = Library.Book.find_most_expensive(book_list)
print("The most expensive book from the list is " + most_expensive.title + " by " + most_expensive.author)      
    
# set_stoplist
print()
print()
print("Testing the stoplist method:")
book_list[1].set_stoplist(True) # setting stoplist for The Da Vinci Code
book_list[1].get_info()

# censor
print()
print()
print("Censoring books by Paulo Coehlo:")
for book in book_list:
    book.censor("Paulo Coehlo", True)
    book.get_info() # printing out the info to see the changes
    print()