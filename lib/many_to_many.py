class Author:
    all = []
    def __init__(self, name):
        self.name = name
        self.add_to_all(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
   
    def total_royalties(self):
        return sum([contract.royalties for contract in Contract.all if contract.author == self])
    
    @classmethod
    def add_to_all(cls,thing):
        cls.all.append(thing)
    pass


class Book:
    all = []
    def __init__(self, title):
        self.title = title
        self.add_to_all(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]
    
    
    @classmethod
    def add_to_all(cls,thing):
        cls.all.append(thing)
    pass


class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        if isinstance(author, Author):
            self.author = author
        else:
            raise Exception
        
        if isinstance(book, Book):
            self.book = book
        else:
            raise Exception
        
        if type(date) == str:
            self.date = date
        else:
            raise Exception
        
        if type(royalties) == int:
            self.royalties = royalties
        else:
            raise Exception
        
        self.add_to_all(self)

    def contracts_by_date():
        return sorted(Contract.all, key = lambda contract:contract.date)

    @classmethod
    def add_to_all(cls,thing):
        cls.all.append(thing)
    pass
