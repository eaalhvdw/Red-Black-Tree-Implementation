from abstract_binary_tree import BinaryTree as BinaryTree

# Denne konkrete underklasse til den abstrakte binære træstruktur 
# implementerer et binært træ med en enkelt linket liste.
class LinkedBinaryTree(BinaryTree):
    
    # Denne private klasse, beskriver en enkelt linket knude, 
    # som har referencer til et element og hhv. sin 
    # forælder, sit venstre og sit højre barn.
    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'
    
        # Konstruktør til oprettelse af en knude.
        def __init__(self, element, parent = None, left = None, right = None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
    
    # Implementation af en abstrakt indre klasse, 
    # som her er direkte nedarvet fra BinaryTree 
    # klassen, som har nedarvet den fra Tree klassen.
    # Tree klassen har implementeret metoden 
    # __not_equals__, som er modstykket til metoden 
    # __equals__ i denne klasse.
    # Klassen beskriver en position i træet, 
    # som indkapsler en knude.
    class Position(BinaryTree.Position):
        
        # Konstruktør til oprettelse af en position i træet.
        # Denne konstruktør bør ikke kaldes af brugere.
        def __init__(self, container, node):
            self._container = container
            self._node = node
        
        # Metoden returnerer det element, som
        # bliver opbevaret i knuden på denne position.
        def element(self):
            return self._node._element
        
        # Denne private metode returnerer True, hvis den anden position 
        # repræsenterer den samme plads i træet, og indkapsler 
        # den samme knude, som denne position.
        def __equals__(self, other):
            return type(other) is type(self) and other._node is self._node
    
    # Konstruktør til oprettelse af et tomt binært træ.
    def __init__(self):
        self._root = None
        self._size = 0
    
    # Denne private hjælpemetode indkapsler en knude i
    # en position og returnerer positionen.
    # Hvis knuden der er givet som 
    # argument er None, returneres None.
    def _make_position(self, node):
        if node is None:
            return None
        else:
            return self.Position(self, node)
    
    # Denne private hjælpemetode validerer en given position.
    # Hvis positionen er valid, returneres den knude, 
    # som opbevares på positionen.
    # Hvis positionen ikke kan validereres,
    # returneres en passende fejlmeddelselse.
    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node
    
    # Metoden returnerer antallet af positioner i træet.
    def __len__(self):
        return self._size
    
    # Metoden indkapsler rodknuden i en 
    # position og returnerer positionen.
    # Hvis træet er tomt, returneres None.
    def root(self):
        return self._make_position(self._root)
    
    # Metoden validerer positionen p, 
    # indkapsler forælderknuden til 
    # knuden på positionp i en position 
    # og returnerer forælderknudens position.
    # Hvis knuden på position p
    # er roden, returneres None.
    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)
    
    # Metoden validerer positionen p, 
    # indkapsler den venstre barneknude
    # til knuden på position p i en position 
    # og returnerer barneknudens position.
    # Hvis knuden på position p ikke har 
    # et venstre barn, returneres None.
    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)
    
    # Metoden validerer positionen p, 
    # indkapsler den højre barneknude
    # til knuden på position p i en position 
    # og returnerer barneknudens position.
    # Hvis knuden på position p ikke har
    # et højre barn, returneres None.
    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)
    
    # Metoden validerer positionen p 
    # og returnerer antallet af børn 
    # til knuden på position p, 
    # hvis valideringen lykkedes.
    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count
        
    # Denne private metode laver en ny knude, som indeholder 
    # elementet e. Den nye knude indkapsles i en position, 
    # der tilføjes som rod til et tomt træ.
    # Træets størrelse sættes til 1.
    # Metoden returnerer rodens position.
    # Hvis træet ikke er tomt, returneres 
    # i stedet en fejlmeddelelse.
    def _add_root(self, e):
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)
    
    # Denne private metode validerer positionen p,
    # laver en ny knude, som indeholder elementet
    # e samt en reference til knuden på position 
    # p som sin forælderknude. 
    # Den nye knude bliver indkapslet i en position
    # og tilføjes træet som venstre barn af knuden 
    # på position p.
    # Træets størrelse øges med en.
    # Metoden returnerer den nye knudes position.
    # Hvis position p ikke kan valideres eller
    # hvis knuden på position p allerede 
    # har et venstre barn, returneres i
    # stedet en passende fejlmeddelelse.
    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)
    
    # Denne private metode validerer positionen p,
    # laver en ny knude, som indeholder elementet
    # e samt en reference til knuden på position 
    # p som sin forælderknude. 
    # Den nye knude bliver indkapslet i en position
    # og tilføjes træet som højre barn af knuden 
    # på position p.
    # Træets størrelse øges med en.
    # Metoden returnerer den nye knudes position.
    # Hvis position p ikke kan valideres eller
    # hvis knuden på position p allerede
    # har et højre barn, returneres i
    # stedet en passende fejlmeddelelse.
    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Right child exists')
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)
    
    # Denne private metode validerer positionen p,
    # udskifter elementet i den indkapslede knude med
    # elementet e og returnerer det gamle element.
    def _replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old
    
    # Denne private metode validerer position p,
    # fjerner knuden på positionen og indsætter 
    # knudens barn på positionen.
    # Træets størrelse mindskes med en.
    # Metoden returnerer det element, 
    # som blev opbevaret i den knude,
    # som er blevet fjernet fra position p.
    # Hvis position p ikke kan valideres
    # eller hvis knuden på position p har
    # to børn, returneres i stedet en 
    # passende fejlmeddelelse.
    def _delete(self, p):
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('Position has two children')
        if node._left:
            child = node._left
        else:
            child = node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element
    
    # Denne private metode validerer position p,
    # tilknytter t1 og t2 som hhv. venstre og højre
    # barn/undertræ til knuden på position p og til sidst
    # nulstiller t1 og t2, så de begge er tomme træer.
    # Træets størrelse øges med størrelsen af hhv. t1 og t2.
    # Metoden returnerer en passende fejlmeddelelse, i de
    # tilfælde, hvor position p ikke kan valideres, 
    # eller ikke er et blad, eller hvor t1 og t2
    # ikke er den samme type som dette træ.
    def _attach(self, p, t1, t2):
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('Position must be leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0