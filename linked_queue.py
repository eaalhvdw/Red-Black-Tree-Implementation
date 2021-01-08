from empty_exception import Empty as Empty

# Linket kø klasse implementeret med en enkelt 
# linket liste efter FIFO køprincippet.
# Bruges til metoden for breadth-first 
# søgning i Tree klassen.
class LinkedQueue:
    
    # Privat, indre klasse, som beskriver en enkelt linket knude, 
    # som har en reference til et element og en reference
    # til den næste knude i køen.
    class _Node:
        __slots__ = '_element', '_next'
        
        # Konstruktør til oprettelse af en knude.
        def __init__(self, element, next):
            self._element = element
            self._next = next
    
    # Konstruktør til oprettelse af en tom linket kø.
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        
    # Metoden returnerer antallet af knuder i køen. 
    def __len__(self):
        return self._size
    
    # Metoden returnerer True, hvis køen er tom.
    def is_empty(self):
        return self._size == 0
    
    # Metoden returnerer det element, som refereres af den første knude, 
    # hovedet i køen, medmindre køen er tom. Er køen tom, returneres 
    # en instans af den brugerdefinerede hjælpeklasse Empty, med en 
    # fejlmeddelelse.
    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element
    
    # Metoden tilføjer en ny knude bagerst i køen og referencen 
    # til halen i køen opdateres til den nye knude.
    # I det tilfælde, at køen var tom før knudens 
    # indsættelse, bliver knuden hovedet i køen.
    # Køens størrelse øges med en.
    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
            self._head._next = newest
            self._tail = newest
        else:
            self._tail._next = newest
            self._tail = self._tail._next
        self._size += 1
    
    # Metoden fjerner og returnerer den forreste knude, hovedet, i køen
    # og referencen til hovedet i køen opdateres til næste knude i køen. 
    # I det tilfælde, at køen er tom, returneres i stedet en instans af 
    # hjælpeklassen Empty, med en fejlmeddelelse.
    # Køens størrelse mindskes med en, hvis en knude blev fjernet.
    # I det tilfælde, at den forreste knude var den sidste i køen,
    # opdateres referencen til halen med None, da der
    # ikke er flere knuder i køen at referere til.
    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        removed = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None    
        return removed
    
    # Metoden printer elementerne i køen til konsollen.
    def print_queue(self):
        if self._head:
            temp = self._head
            while temp is not None:
                print(temp._element, end=" -> ")
                temp = temp._next
        else:
            print("Queue is empty")
