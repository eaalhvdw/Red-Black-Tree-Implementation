from abc import abstractmethod
from abstract_tree import Tree as Tree

# Abstrakt basal klasse, som beskriver en binær træstruktur, og som
# nedarver fra den abstrakte træstruktur klasse.
# Der kan ikke oprettes instanser af denne klasse, da den er abstrakt.
# Alle abstrakte metoder implementeres i konkrete underklasser 
# af denne klasse.
class BinaryTree(Tree):
    
    # Metoden returnerer den position, som indkapsler 
    # venstrebarnet til elementet på position p.
    # Hvis elementet på position p ikke har et 
    # venstre barn, returneres None.
    @abstractmethod
    def left(self, p):
        pass
    
    # Metoden returnerer den position, som indkapsler 
    # højrebarnet til elementet på position p.
    # Hvis elementet på position p ikke har et 
    # højre barn, returneres None.
    @abstractmethod
    def right(self, p):
        pass
    
    # Metoden returnerer den position, som 
    # indkapsler søskendeelementet
    # til elementet på position p.
    # Hvis elementet på position p 
    # ikke har en søskende, 
    # returneres None.
    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
    
    # Implementation af en abstrakt metode 
    # nedarvet fra træstrukturklassen.
    # Metoden genererer en iteration 
    # over alle de positioner, der 
    # indkapsler børnenene til 
    # elementet på position p.
    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
    
    # Denne metode overrider en nedarvet metode, for
    # at gøre inorder gennemløb af træet default.
    # Metoden returnerer en iteration over alle træets 
    # positioner, ved at gennemløbe træet inorder.
    def positions(self):
        return self.inorder()
    
    # Metoden genererer en inorder iteration 
    # over alle positionerne i træet.
    def inorder(self):
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p
    
    # Denne private hjælpemetode genererer en inorder iteration over 
    # alle positionerne i det undertræ, der har sin rod på position p.
    def _subtree_inorder(self, p):
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other
