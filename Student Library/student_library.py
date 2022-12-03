class Library:
    
    def __init__(self,listOfBooks):
        self.books = listOfBooks
    
    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        i = 1
        for book in self.books:
            print(f'{i} {book}')
            i = i+1
    
    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days.")
            self.books.remove(bookName)
        else:
            print("Sorry,the book has already been issued to someone else. Please wait untol the book is returned")

    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for returning this books.")
        
        
        
        
class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow")
        return self.book
    
    def returnBook(self):
        self.book = input("Enter the name of the book you want to return")
        return self.book


if __name__ == '__main__':
    centralLibrary = Library(['Dsa','Django','Java','Blockchain'])
    student = Student()
    
    while(True):
        welcomeMsg = ''' Welcome to Central Library
        Please choose an option:
        1. Lisitng all the books
        2. Request a book
        3. Return a book
        4. Exit the libraryclearc
        '''
        print(welcomeMsg)
        a = int(input("Enter you choice: "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            book = student.requestBook()
            centralLibrary.borrowBook(book.capitalize())    
        elif a == 3:
            book = input(f"Enter the name of the book you want to return").capitalize()
            centralLibrary.returnBook(book)
        elif a == 4:
            print('Thanks for choosing us')
            exit()
        else:
            print("Please enter valid choice")    
                
