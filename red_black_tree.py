from tree_map import TreeMap as TreeMap

# Denne konkrete underklasse implementerer
# et sorteret map med et rød-sort træ, som
# nedarver fra TreeMap klassen.
class RedBlackTreeMap(TreeMap):
    
    # Denne private klasse, som er nedarvet 
    # fra TreeMap klassen, beskriver en 
    # enkelt linket knude, som har referencer 
    # til et element og hhv. sin forælder,
    # sit venstre og sit højre barn. 
    # Klassens variabel __slots__ 
    # bliver udviddet med en boolean, 
    # som indikerer hvorvidt en knude 
    # er rød eller ej. I sidste tilfælde,
    # vil det sige, at knuden er sort.
    class _Node(TreeMap._Node):
        __slots__ = '_red'
        
        # Konstruktør til oprettelse af en knude.
        # Knuden bliver by default farvet rød.
        def __init__(self, element, parent = None, left = None, right = None):
            super().__init__(element, parent, left, right)
            self._red = True
    
    # Denne private metode farver
    # knuden på positionen p rød.
    def _set_red(self, p):
        p._node._red = True
    
    # Denne private metode farver
    # knuden på position p sort.
    def _set_black(self, p):
        p._node._red = False
    
    # Denne private metode farver
    # knuden på position p enten 
    # rød eller sort, alt efter 
    # hvilken værdi den boolske 
    # variabel make_red har.
    def _set_color(self, p, make_red):
        p._node._red = make_red
    
    # Denne private metode 
    # returnerer True, hvis 
    # knuden på position p 
    # ikke er None samt har
    # farven rød.
    def _is_red(self, p):
        return p is not None and p._node._red
        
    # Denne private metode
    # returnerer True, hvis
    # knuden på position p
    # er farvet rød og tilmed
    # er en bladknude.
    def _is_red_leaf(self, p):
        return self._is_red(p) and self.is_leaf(p)
    
    # Denne private metode søger i 
    # position p's undertræer efter 
    # et rødt barn og returnerer det
    # først fundne røde barns position.
    # Hvis p ikke har noget rødt barn
    # returneres None.
    def _get_red_child(self, p):
        for child in (self.left(p), self.right(p)):
            if self._is_red(child):
                return child
        return None
    
    # Denne private metode balancerer 
    # træet efter indsættelse af en 
    # ny knude på position p.
    def _rebalance_insert(self, p):
        self._resolve_red(p)
    
    # Denne private metode løser evt. konflikter i forbindelse
    # med indsættelse af en ny knude på position p i træet.
    # Hvis p er roden af træet, er der ingen konflikter,
    # og knuden på position p farves sort.
    # Hvis p's forælder er sort, er der ingen konflikter 
    # og man behøver ikke at foretage sig mere.
    # Hvis p's forælder er rød, er der en dobbelt rød konflikt 
    # og her ser man nærmere på p's onkel for at finde den rette løsning.
    # Hvis p's onkel er sort, restruktureres træet.
    # Hvis p's onkel er rød, omfarves knuderne således, 
    # at p's bedsteforælder farves rød, p's forælder og
    # onkel farves sorte og til sidst løses evt. endnu en
    # dobbelt rød konflikt, som kan være propageret op til 
    # bedsteforælderen, hvis dennes forælder også er rød.
    def _resolve_red(self, p):
        if self.is_root(p):
            # TODO: SOLVE - NOT ENTERED (=> ROOT BECOMES RED)
            self._set_black(p)
        else:
            parent = self.parent(p)
            if self._is_red(parent):
                uncle = self.sibling(parent)
                if not self._is_red(uncle): # Case 1
                    middle = self._restructure(p)
                    self._set_black(middle)
                    self._set_red(self.left(middle))
                    self._set_red(self.right(middle))
                else: # Case 2
                    grand = self.parent(parent)
                    self._set_red(grand)
                    self._set_black(self.left(grand))
                    self._set_black(self.right(grand))
                    self._resolve_red(grand)
    
    # Denne private metode balancerer 
    # træet efter fjernelse af en
    # knude på position p.
    # Hvis træet er blevet reduceret 
    # til kun at indeholde én knude, 
    # som dermed er roden, farves 
    # denne sort.
    # Hvis p ikke er None, og p har ét
    # barn, som ikke er et rødt blad,
    # er der opstået en dobbelt sort 
    # konflikt, som skal håndteres.
    # Hvis p ikke er None, og p har to
    # børn, bliver børnene farvet sorte,
    # såfremt de er røde.
    def _rebalance_delete(self, p):
        if len(self) == 1:
            self._set_black(self.root())
        elif p is not None:
            n = self.num_children(p)
            if n == 1:
                child = next(self.children(p))
                if not self._is_red_leaf(child):
                    self._fix_deficit(p, child)
            elif n == 2:
                if self._is_red_leaf(self.left(p)):
                    self._set_black(self.left(p))
                else:
                    self._set_black(self.right(p))

    # Denne private metode løser evt. konflikter i forbindelse
    # med fjernelse af en knude i træet.
    # Metoden tager to argumenter, en position x og en position y, 
    # som er x's barn og søskende til den dobbelt sorte knude.
    # Hvis knuden på position y ikke er rød, men har et rødt barn, z,
    # er det Case 1, som skal løses. Her udføres en restrukturering,
    # hvor z roteres op over sin forælder y. Knuderne farves derefter,
    # således, at knuden på position x får samme farve som knuden på
    # position z havde til at starte med, mens knuderne på positionerne
    # x og y farves sorte.
    # Hvis knuden på position y ikke er rød, og begge dens børn er sorte,
    # er det Case 2, som skal løses. Her udføres en omfarvning, hvor knuden
    # på position y farves rød og knuden på position x farves sort. Hvis
    # knuden på position x var rød, er konflikten løst. Var knuden sort,
    # opstår en ny dobbelt sort konflikt, da x farves dobbelt sort.
    # Hvis knuden på position y er rød, er det Case 3, som skal løses.
    # Her udføres først en justering, hvor y roteres op over sin forælder,
    # x, derefter farves y sort og x rød og til sidst kan enten Case 1 eller
    # Case 2 benyttes til at afslutte konflikten. 
    def _fix_deficit(self, x, y):
        if not self._is_red(y): # Case 1 or case 2
            z = self._get_red_child(y)
            if z is not None: # Case 1
                old_color = self._is_red(x)
                middle = self._restructure(z)
                self._set_color(middle, old_color)
                self._set_black(self.left(middle))
                self._set_black(self.right(middle))
            else: # Case 2
                self._set_red(y)
                if self._is_red(x):
                    self._set_black(x)
                elif not self.is_root(x):
                    self._fix_deficit(self.parent(x), self.sibling(x))
        else: # Case 3
            self._rotate(y)
            self._set_black(y)
            self._set_red(x)
            if x == self.right(y):
                self._fix_deficit(x, self.left(x))
            else:
                self._fix_deficit(x, self.right(x))
