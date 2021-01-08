from abc import abstractmethod
from linked_queue import LinkedQueue as LinkedQueue

# Abstrakt basal klasse, som beskriver en træstruktur.
# Der kan ikke oprettes instanser af denne klasse, da den er abstrakt.
# Abstrakte metoder implementeres i underklasser af denne klasse.
class Tree:
    
    # Abstrakt indre klasse, der 
    # beskriver en position i træet.
    class Position:
        
        # Metoden returnerer det element, som
        # er indkapslet på denne position.
        @abstractmethod
        def element(self):
            pass 
        
        # Denne private metode returnerer True, hvis den anden position 
        # repræsenterer den samme plads i træet, og indkapsler 
        # det samme element, som denne position.
        @abstractmethod
        def __equals__(self, other):
            pass
        
        # Denne private metode returnerer True, hvis den anden position 
        # ikke repræsenterer den samme plads i træet, og ikke indkapsler 
        # det samme element, som denne position.
        def __ne__(self, other):
            return not (self == other)
        
    # Metoden returnerer rodens position.
    # Hvis træet er tomt, returneres None.
    @abstractmethod
    def root(self):
        pass
    
    # Metoden returnerer positionen 
    # for forælderelementet til
    # elementet på posistion p.
    # Hvis elementet på position p
    # er roden, returneres None.
    @abstractmethod
    def parent(self, p):
        pass
    
    # Metoden returnerer antallet af børn
    # til elementet på position p.
    @abstractmethod
    def num_children(self, p):
        pass
    
    # Metoden laver en iteration 
    # over børneelementerne til
    # elementet på position p.
    @abstractmethod
    def children(self, p):
        pass
    
    # Metoden returnerer antallet 
    # af positioner i træet.
    @abstractmethod
    def __len__(self):
        pass
    
    # Metoden returnerer True, hvis position
    # p er positionen for roden af træet.
    def is_root(self, p):
        return self.root() == p
    
    # Metoden returnerer True, hvis
    # elementet på position p
    # ikke har nogen børn.
    def is_leaf(self, p):
        return self.num_children(p) == 0
    
    # Metoden returnerer True, hvis træet er tomt.
    def is_empty(self):
        return len(self) == 0
    
    # Metoden returnerer dybden af træet 
    # fra position p til rodens position.
    # Dybden er antallet af niveauer der 
    # er mellem rodens position og position p.
    # Hvis p er None eller hvis p ikke findes
    # i træet, returneres None.
    def depth(self, p):
        if p is None:
            return None
        elif self.is_root(p):
            return 0
        else:
            if self.parent(p):
                return 1 + self.depth(self.parent(p))
            else: # special case: p was not found in the tree.
                return None
        
    # Metoden returnerer højden af det undertræ, 
    # som har sin rod på position p.
    # Hvis position p er None, returneres
    # højden af hele træet.
    # Hvis træet er tomt, returneres None.
    def height(self, p = None):
        if p is None:
            p = self.root()
        if p:
            return self._height(p)
        else:
            return None
    
    # Denne private hjælpemetode returnerer højden af
    # det undertræ, som har sin rod på position p.
    def _height(self, p):
        if self.is_leaf(p):
            return 0
        else:
            for c in self.children(p):
                return 1 + max(self._height(c))
                
    # Metoden genererer en iteration over alle positioner i træet 
    # og returnerer for hver position elementet på positionen.
    def __iter__(self):
        for p in self.positions():
            yield p.element()
    
    # Metoden returnerer en iteration over alle træets 
    # positioner, ved at gennemløbe træet preorder.
    def positions(self):
        return self.preorder()
    
    # Metoden genererer en preorder iteration 
    # over alle positionerne i træet.
    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p
                
    # Denne private hjælpemetode genererer en preorder iteration over 
    # alle positionerne i det undertræ, der har sin rod på position p.
    def _subtree_preorder(self, p):
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other
    
    # Metoden genererer en postorder iteration 
    # over alle positionerne i træet.
    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p
    
    # Denne private hjælpemetode genererer en postorder iteration over 
    # alle positionerne i det undertræ, der har sin rod på position p.
    def _subtree_postorder(self, p):
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p
    
    # Metoden genererer en breadth-first iteration 
    # over alle positionerne i træet.
    def breadthfirst(self):
        if not self.is_empty():
            queue = LinkedQueue()
            queue.enqueue(self.root())
            while not queue.is_empty():
                p = queue.dequeue()
                yield p
                for c in self.children(p):
                    queue.enqueue(c)
  