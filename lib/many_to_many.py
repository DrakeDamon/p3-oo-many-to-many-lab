class Author:
    def __init__(self, name=''):
        self.name = name
        self.contract_list = []  # This stores contracts related to this author

    def contracts(self):
        return self.contract_list  # This returns the list of contracts
    
    def books(self):
        # Create a list of books by going through the contracts
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)  # Creates a new contract and associates it
        return contract  # Return the newly created contract
    
    def total_royalties(self):
        total = 0  # Start with a total of 0
        for contract in self.contract_list:  # Loop through each contract in the author's contract list
            total += contract.royalties  # Add the royalties from each contract to the total
        return total  # Return the sum of all royalties


class Book:
    def __init__(self, title=''):
        self.title = title
        self.contract_list = []  # Add a contract_list for each book to store contracts


    def contracts(self):
        return self.contract_list  # This returns the list of contracts related to this book
    
    def authors(self):
        return [contract.author for contract in self.contracts()]  # Return authors from the contracts


class Contract:
    all = []  # Class-level list to store all contracts
    
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        # Validate if author is an instance of Author
        if isinstance(author, Author):
            author.contract_list.append(self)  # Add this contract to the author's list
        else:
            raise TypeError('Author must be an instance of the Author class')

        # Validate if book is an instance of Book
        if isinstance(book, Book):
            book.contract_list.append(self)  # Add this contract to the book's list
        else:
            raise TypeError('Book must be an instance of the Book class')

        # Validate if the date is a string
        if not isinstance(date, str):
            raise TypeError('Date must be a string')

        # Validate if the royalties are an integer
        if not isinstance(royalties, int):
            raise TypeError('Royalties must be an integer')

        # Append the contract to the class-level Contract.all list
        Contract.all.append(self)  # This is important to store each contract for sorting
        
    @classmethod
    def contracts_by_date(cls, specific_date=None):
        if specific_date:
        # Filter the contracts by the specific date
            return [contract for contract in cls.all if contract.date == specific_date]
    # Sort all contracts by date if no specific date is provided
        return sorted(cls.all, key=lambda contract: contract.date)