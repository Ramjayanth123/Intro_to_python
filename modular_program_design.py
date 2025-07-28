def addBook(inventory):
    book = input('Enter the book name: ')
    author = input('Enter the author name: ')
    inventory[book]=author
    return "Book added"
def search(book):
    if book in inventory:
        print(f'Book Found:{book}') 
    else:
        print( "Book not found")
def display_inventory():
    print('Inventory: ')
    for book,author in inventory.items():
        print(f"Book: {book} | Author: {author}")
inventory={}
while True:
    print(
        '''
        Welcome to Book management library. What are you here for
        1. Add Book
        2. Search Book
        3. Display Inventory
        4. Enter q to exit
'''
    )
    choice = int(input('Enter your Choice: '))
    if choice ==1:
        print(addBook(inventory))
    elif choice==2:
        what_to_search = input('Enter your book name to search: ')
        search(what_to_search)
    elif choice==3:
        display_inventory()
    else:
        print("Terminating")
        break
