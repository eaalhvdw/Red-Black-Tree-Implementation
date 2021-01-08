from collections.abc import MutableMapping

# Abstrakt basal klasse, som beskriver et map, 
# og nedarver fra klassen MutableMapping.
class MapBase(MutableMapping):
    
    # Denne private klasse beskriver et item, 
    # der indeholder et nøgle-værdi par.
    class _Item:
        __slots__ = '_key', '_value'
        
        # Konstruktør til at oprette et item 
        # med en nøgle og en værdi.
        def __init__(self, k, v):
            self._key = k
            self._value = v
        
        # Metoden sammenligner to items baseret på deres nøgler.
        # Metoden returnerer True, hvis nøglerne er ens.
        def __equals__(self, other):
            return self._key == other._key
    
        # Metoden sammenligner to items baseret på deres nøgler.
        # Metoden returnerer True, hvis nøglerne ikke er ens.
        def __ne__(self, other):
            return not (self == other)
    
        # Metoden sammenligner to items baseret på deres nøgler.
        # Metoden returnerer True, hvis nøglen for dette item er 
        # mindre, end det andet items nøgle.
        def __lt__(self, other):
            return self._key < other._key
