## dunder / special/ magic methods
## eg. __str__ 
## eg. __len__

class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages 

    def __str(self):
        ## returns the string representation of a user defined class/object
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        ## returns the len of of a user defined class/object
        return self.pages