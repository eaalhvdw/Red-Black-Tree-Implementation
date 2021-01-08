from empty_exception import Empty as Empty
from linked_binary_tree import LinkedBinaryTree as LinkedBinaryTree
from abstract_map_base import MapBase as MapBase

# Denne konkrete underklasse implementerer 
# et sorteret map med en binær træstruktur. 
# Klassen nedarver både fra LinkedBinaryTree 
# klassen og MapBase klassen.
class TreeMap(LinkedBinaryTree, MapBase):
    
    # Denne klasse udvider den nedarvede
    # klasse fra LinkedBinaryTree.
    class Position(LinkedBinaryTree.Position):
        
        # Metoden returnerer nøglen fra
        # dette mapitems nøgle-værdi par.
        def key(self):
            return self.element()._key
        
        # Metoden returnerer værdien fra
        # dette mapitems nøgle-værdi par.
        def value(self):
            return self.element()._value
    
    # Denne private metode søger i det undertræ der
    # har p som rod, efter en knude, som har et item
    # med nøglen k. Hvis denne findes, returneres
    # positionen for denne knude. Hvis der ikke
    # findes en knude med denne nøgle,
    # returneres i stedet positionen
    # for den sidst besøgte knude.
    def _subtree_search(self, p, k):
        if k == p.key():
            return p
        elif k < p.key():
            if self.left(p) is not None:
                return self._subtree_search(self.left(p), k)
        else:
            if self.right(p) is not None:
                return self._subtree_search(self.right(p), k)
        return p

    # Denne private metode returnerer
    # positionen for det første item i
    # det undertræ, der har p som rod.
    def _subtree_first_position(self, p):
        walk = p
        while self.left(walk) is not None:
            walk = self.left(walk)
        return walk

    # Denne private metode returnerer
    # positionen for det sidste item i
    # det undertræ, der har p som rod.
    def _subtree_last_position(self, p):
        walk = p
        while self.right(walk) is not None:
            walk = self.right(walk)
        return walk
    
    # Metoden returnerer det første element i
    # træet eller None, hvis træet er tomt.
    def first(self):
        if len(self) > 0:
            return self._subtree_first_position(self.root())
        else:
            return None

    # Metoden returnerer det sidste element i
    # træet eller None, hvis træet er tomt.
    def last(self):
        if len(self) > 0:
            return self._subtree_last_position(self.root())
        else:
            return None

    # Metoden validerer position p, søger
    # efter den position, som kommer lige før
    # p i et inorder gennemløb af træet, og
    # returnerer den fundne position.
    def before(self, p):
        self._validate(p)
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            return above
            
    # Metoden her gør det tilsvarende 
    # som forrige metode, denne blot 
    # for den position der kommer lige 
    # efter p i nøglernes narturlige 
    # orden, inorder. Den position der
    # kommer lige efter p returneres.
    def after(self, p):
        self._validate(p)
        if self.right(p):
            return self._subtree_first_position(self.right(p))
        else:
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.right(above):
                walk = above
                above = self.parent(walk)
        return above
    
    # Denne metode søger efter den
    # position i træet, som har nøglen
    # k og returnerer enten positionen
    # for nøglen, eller None, hvis træet 
    # er tomt.
    def find_position(self, k):
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(), k)
            return p
        
    # Metoden validerer positionen p og
    # sletter det item der er indkapslet 
    # i p. Har p både et højre og et
    # venstre barn, erstattes det 
    # slettede item af det item 
    # som er i det ældste barn
    # af ps venstre undertræ.
    # Til sidst rebalanceres træet.
    def delete(self, p):
        self._validate(p) 
        if self.left(p) and self.right(p):
            replacement = self._subtree_last_position(self.left(p))
            self._replace(p, replacement.element())
            p = replacement
        parent = self.parent(p)
        self._delete(p)
        self._rebalance_delete(parent)
        
    # Denne metode, som er en del 
    # af et standard map interface, 
    # søger i træet efter nøglen k
    # og returnerer enten værdien
    # til nøglen eller en key error,
    # hvis nøglen ikke findes.
    # Hvis træet er tomt, returneres
    # i stedet en Empty error.
    def __getitem__(self, k):
        if self.is_empty():
            raise Empty('Tree is empty')
        else:
            p = self._subtree_search(self.root(), k)
            if k != p.key():
                raise KeyError('Key Error: ' + repr(k))
            return p.value()
    
    # Denne metode, som er en del 
    # af et standard map interface,
    # erstatter den værdi som er 
    # tilknyttet nøglen k, hvis 
    # denne findes. Er træet tomt 
    # eller er der ingen nøgle der 
    # matcher nøglen k, indsættes 
    # et nyt item i træet med
    # nøglen k og værdien v.
    def __setitem__(self, k, v):
        if self.is_empty():
            leaf = self._add_root(self._Item(k, v))
        else:
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                p.element()._value = v
                return
            else:
                item = self._Item(k, v)
                if p.key() < k:
                    leaf = self._add_right(p, item)
                else:
                    leaf = self._add_left(p, item)
        self._rebalance_insert(leaf)
        
    # Denne metode, som er en del 
    # af et standard map interface,
    # sletter det item der har det
    # nøgle-værdi-par, som indeholder 
    # nøglen k. Hvis træet er tomt 
    # returneres en empty error.
    def __delitem__(self, k):
        if not self.is_empty():
             p = self._subtree_search(self.root(), k)
             if k == p.key():
                 self.delete(p)
                 return
        raise Empty('Tree is empty')
        
    # Denne metode, som er en del 
    # af et standard map interface,
    # genererer en iteration over 
    # alle positioner i træet og
    # returnerer for hver position 
    # nøglen fra det item som er 
    # indkapslet på positionen.
    def __iter__(self):
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after(p)
    
    # Denne metode, som er en del 
    # af et sorteret map interface,
    # genererer en iteration over
    # alle positioner i træet, i
    # omvendt rækkefølge, startende
    # med den sidste position i 
    # træet, sluttende med den 
    # første position. For hver
    # position i træet, returneres
    # nøglen i det item, som er 
    # indkapslet på positionen.
    def __reversed__(self):
        p = self.last()
        while p is not None:
            yield p.key()
            p = self.before(p)
    
    # Denne metode, som er en del 
    # af et sorteret map interface,
    # returnerer enten det nøgle-
    # værdi-par, som har den mindste
    # nøgle i træet eller en Empty error, 
    # hvis træet er tomt.
    def find_min(self):
        if self.is_empty():
            raise Empty("Tree is empty")
        else:
            p = self.first()
            return (p.key(), p.value())
    
    # Denne metode, som er en del 
    # af et sorteret map interface,
    # returnerer enten det nøgle-
    # værdi-par, som har den største 
    # nøgle i træet eller en Empty
    # error, hvis træet er tomt.
    def find_max(self):
        if self.is_empty():
            raise Empty("Tree is empty")
        else:
            p = self.last()
            return (p.key(), p.value())
        
    # Denne metode, som er en del 
    # af et sorteret map interface,
    # søger i træet efter nøglen k,
    # og returnerer det nøgle-værdi
    # par, som har den største nøgle, 
    # hvor nøgle enten er lig med 
    # eller mindre end k. 
    # Hvis træet er tomt, returneres 
    # en Empty error. Hvis nøglen k 
    # ikke findes, returneres None.
    def find_le(self, k):
        if self.is_empty():
            raise Empty("Tree is empty")
        else:
            p = self.find_position(k)
            if k < p.key():
                p = self.before(p)
            if p is None:
                return None
            else:
                return (p.key(), p.value())
    
    # Denne metode, som er en del 
    # af et sorteret map interface,
    # søger i træet efter nøglen k,
    # og returnerer det nøgle-værdi
    # par, som har den største nøgle,
    # hvor nøglen er mindre end k.
    # Hvis træet er tomt, returneres 
    # en Empty error. Hvis nøglen k
    # ikke findes, returneres None.
    def find_lt(self, k):
        if self.is_empty():
            raise Empty("Tree is empty")
        else:
            p = self.find_position(k)
            if not p.key() < k:
                p = self.before(p)
            if p is None:
                return None
            else:
                return (p.key(), p.value())
    
    # Denne metode, som er en del 
    # af et sorteret map interface,
    # søger i træet efter nøglen k,
    # og returnerer det nøgle-værdi
    # par, som har den mindste nøgle, 
    # hvor nøgle enten er lig med 
    # eller større end k. 
    # Hvis træet er tomt, returneres 
    # en Empty error. Hvis nøglen k
    # ikke findes, returneres None.
    def find_ge(self, k):
        if self.is_empty():
            raise Empty("Tree is empty")
        else:
             p = self.find_position(k)
             if p.key() < k:
                 p = self.after(p)
             if p is None:
                 return None
             else:
                 return (p.key(), p.value())
    
    # Denne metode, som er en del 
    # af et sorteret map interface,
    # søger i træet efter nøglen k,
    # og returnerer det nøgle-værdi
    # par, som har den mindste nøgle,
    # hvor nøglen er større end k.
    # Hvis træet er tomt, returneres
    # en Empty error. Hvis nøglen 
    # k ikke findes, returneres None.
    def find_gt(self, k):
        if self.is_empty():
            raise Empty("Tree is empty")
        else:
            p = self.find_position(k)
            if not k < p.key():
                p = self.after(p)
            if p is None:
                return None
            else:
                return (p.key(), p.value())
    
    # Denne metode, som er en del 
    # af et sorteret map interface,
    # genererer en iteration over
    # de nøgle-værdi par, hvis nøgler
    # er større end eller lig med 
    # start_k og mindre, end stop_k.
    # Hvis start_k er None, begynder
    # iterationen med det nøgle-værdi
    # par, som har den mindste nøgle
    # i træet. Hvis stop_k er None, 
    # fortsætter iterationen helt 
    # frem til og med det nøgle-værdi 
    # par, som har den største nøgle
    # i træet. Hvis træet er tomt, 
    # returneres en Empty error.
    def find_range(self, start_k, stop_k):
        if not self.is_empty():
            if start_k is None:
                p = self.first()
            else:
                p = self.find_position(start_k)
                if p.key() < start_k:
                    p = self.after(p)
            while p is not None and (stop_k is None or p.key() < stop_k):
                yield (p.key(), p.value())
                p = self.after(p)
        raise Empty("Tree is empty")
                
    # Denne private metode er en hook, 
    # som de underklasser, der er balancerede 
    # træer, kan implementere og benytte ved
    # balancering efter indsættelse af et nyt
    # item på position p.
    def _rebalance_insert(self, p):
        pass
    
    # Denne private metode er en hook, 
    # som de underklasser, der er balancerede
    # træer, kan implementere og benytte ved
    # balancering efter sletning af et nyt 
    # item på position p.
    def _rebalance_delete(self, p):
        pass
    
    # Denne private metode er en hook,
    # som benyttes af en underklasse, som
    # implementerer et Splay tree. 
    # Denne metode bruges til at
    # føre statistik over, hvilke
    # items der bliver tilgået oftest,
    # således at disse items kan bringes 
    # tættere på roden for at optimere
    # kørselstiden for søgning i træet.
    def _rebalance_access(self, p):
        pass
    
    # Denne private metode understøtter
    # balancering af træet, ved at gen-
    # oprette forbindelse mellem en
    # barneknude og en forælderknude.
    # En boolean, make_left_child
    # bestemmer, om barneknuden
    # skal være venstre- eller 
    # højrebarn af forælderknuden.
    # OBS: Barneknuden kan være None.
    def _relink(self, parent, child, make_left_child):
        if make_left_child:
            parent._left = child
        else:
            parent._right = child
        if child is not None:
            child.p_parent = parent
    
    # Denne private metode understøtter
    # også balancering af træet. Her
    # roteres position p op over dens 
    # forælder.
    # OBS: Når denne metode kaldes, 
    # skal man først sikre sig, at
    # p ikke er roden af træet.
    def _rotate(self, p):
        x = p._node
        y = x._parent
        z = y._parent
        if z is None:
            self._root = x
            x._parent = None
        else:
            self._relink(z, x, y == z._left)
            if x == y._left:
                self._relink(y, x._right, True)
                self._relink(x, y, False)
            else:
                self._relink(y, x._left, False)
                self._relink(x, y, True)
    
    # Denne private metode understøtter
    # også balancering af træet. Her
    # udføres en treknude restrukturering
    # af x, dens forælder og dens
    # bedsteforælder, ved at lave
    # en dobbelt rotation. Metoden 
    # returnerer den position, som 
    # bliver roden af det restruktu-
    # rerede undertræ.
    # OBS: Når denne metode kaldes,
    # skal man først sikre sig, at x
    # har en bedsteforælder.
    def _restructure(self, x):
        y = self.parent(x)
        z = self.parent(y)
        if (x == self.right(y)) == (y == self.right(z)):
            self._rotate(y)
            return y
        else:
            self._rotate(x)
            self._rotate(x)
            return x