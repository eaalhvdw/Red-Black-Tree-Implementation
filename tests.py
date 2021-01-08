from linked_queue import LinkedQueue as LinkedQueue
from red_black_tree import RedBlackTreeMap as RedBlackTreeMap

#------------------------------- LINKED QUEUE ---------------------------------

print("\nTEST LinkedQueue\n----------------\n")

# Opret ny kø.
queue = LinkedQueue()
# Test oprettelse af kø.
print("Længden af den nyoprettede kø, forventes at være 0:", queue.__len__())
print("Køen forventes at være tom og resultatet True:", queue.is_empty())
print()

# Fyld kø med elementer.
queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(12)

# Test enqueue - print alle elementer i køen.
print("Køen forventes at indeholde følgende elementer; 5, 10, 12:")
queue.print_queue()
print("\n")

# Test links mellem elementer.
print("Det første elements next forventes at være 10:", queue._head._next._element)
print("Det andet elements next forventes at være 12:", queue._head._next._next._element)
print("Det sidste elements next forventes at være None:", queue._tail._next)
print("Køens længde forventes at være 3:", queue.__len__())
print("Køen forventes ikke at være tom og resultatet False:", queue.is_empty())
print()

# Test dequeue element 5.
print("Elementet som er blevet fjernet forventes at være 5:", queue.dequeue())
print("Køen forventes at indeholde følgende elementer; 10, 12:")
queue.print_queue()
print()
print("Det første element i køen forventes at være 10:", queue.first())
print("Køens længde forventes at være 2:", queue.__len__())
print()

# Test dequeue element 10.
print("Elementet som er blevet fjernet forventes at være 10:", queue.dequeue())
print("Køen forventes at indeholde følgende elementer; 12:")
queue.print_queue()
print()
print("Det første element i køen forventes at være 12:", queue.first())
print("Køens længde forventes at være 1:", queue.__len__())
print()

# Test dequeue element 12.
print("Elementet som er blevet fjernet forventes at være 12:", queue.dequeue())
print("Køen forventes at returnere en fejlbesked ved forsøg på at printe køens indhold:")
queue.print_queue()
print("Køen forventes at være tom og resultatet True:", queue.is_empty())
print("Køens længde forventes at være 0:", queue.__len__())
print("\n-----------------------------------------------------------------------------\n")


#------------------------ NOT DONE - RED-BLACK TREE ---------------------------

print("TEST RedBlackTreeMap\n---------------------\n")

# TODO: Make more tests and adapt current tests to test all
# scenarios of  all methods, when a full tree can be build.

# Opret nyt træ.
red_black_tree = RedBlackTreeMap()
empty_root = red_black_tree.root()

print("---- TESTS PÅ ET TOMT TRÆ ----")

# Test is_empty().
print("\nis_empty()")
print("At træet er tomt, forventes at være True:", red_black_tree.is_empty())

# Test depth(p).
print("\ndepth(p)")
print("Dybden af træet forventes at være None:", red_black_tree.depth(empty_root))

# Test height(p).
print("\nheight(p)")
print("Højden af træet forventes at være None:", red_black_tree.height(empty_root))

# Test __len__().
print("\n__len__()")
print("Længden af træet forventes at være 0:", red_black_tree.__len__())

# Test root().
print("\nroot()")
print("Roden af træet forventes at være None:", empty_root)

print("\n---- FYLD ELEMENTER I TRÆET ----\n")

# Tilføj elementer til træet.
# TODO: Test __setitem__(k, v). ---- FAIL - TypeError: p must be proper Position type (from _validate(p), LinkedBinaryTree)
print("__setitem__(k, v)")
red_black_tree.__setitem__(10, 'a') # When tree is empty, the item goes in, but as a red node.
print("Roden af træet forventes at have elmentet med nøglen 10:", red_black_tree.root().element()._key)      
#red_black_tree.__setitem__(4, 'b') # The tree is not empty, throws ERROR
#red_black_tree.__setitem__(8, 'c')
#red_black_tree.__setitem__(22, 'd')
#red_black_tree.__setitem__(15, 'e')

print("\n---- TESTS PÅ ET TRÆ SOM IKKE ER TOMT ----")

root = red_black_tree.root()
root_key = root.key()
root_value = root.value()

# Test preorder() og print nøglerne i træets elementer.
print("\npreorder()")
print("Nøglerne printes i preorder rækkefølge:", end=" - ")
pre_itr = red_black_tree.preorder()
for e in pre_itr:
    print(e.key())

# Test postorder() og print nøglerne i træets elementer.
print("\npostorder()")
print("Nøglerne printes i postorder rækkefølge:", end=" - ")
post_itr = red_black_tree.postorder()
for e in post_itr:
    print(e.key())

# Test breadthfirst() og print nøglerne i træets elementer.
print("\nbreadthfirst()")
print("Nøglerne printes i bredthfirst rækkefølge:", end=" - ")
bf_itr = red_black_tree.breadthfirst()
for e in bf_itr:
    print(e.key())

# Test __iter__() og print nøglerne i træets elementer.
print("\n__iter__()")
print("Nøglerne i træet, printes i inorder rækkefølge:", end=" - ")
in_itr = red_black_tree.__iter__()
for e in in_itr:
    print(e)

# Test __reversed__() og print nøglerne i træets elementer.
print("\n__reversed__()")
print("Nøglerne printes i omvendt rækkefølge:", end=" - ")
rev_itr = red_black_tree.__reversed__()
for e in rev_itr:
    print(e)

# Test is_empty().
print("\nis_empty()")
print("At træet er tomt, forventes at være False:", red_black_tree.is_empty())

# Test depth(p).
print("\ndepth(p)")
print("Dybden af træet forventes at være None:", red_black_tree.depth(root))

# Test height(p).
print("\nheight(p)")
print("Højden af træet forventes at være 0:", red_black_tree.height(root))

# Test __len__().
print("\n__len__()")
print("Længden af træet forventes at være 1:", red_black_tree.__len__())

# Test root().
print("\nroot()")
print("Roden af træet forventes at have elementet med nøglen 10:", root_key)

# Test parent(p).
print("\nparent(p)")
print("Det forventes, at roden ikke har nogen forælder:", red_black_tree.parent(root))

# Test sibling(p).
print("\nsibling(p)")
print("Det forventes at roden ikke har nogen søskende:", red_black_tree.sibling(root))

# Test left(p)
print("\nleft(p)")
left = red_black_tree.left(root)
print("Rodens venstre barn forventes at være None:", left)

# Test right(p)
print("\nright(p)")
right = red_black_tree.right(root)
print("Rodens højre barn forventes at være None:", red_black_tree.right(root))

# Test children(p).
print("\nchildren(p)")
it = red_black_tree.children(root)
children = []
for c in it:
    children.append(c)
print("Det forventes, at roden ikke har nogen børn:", children)

# Test _get_red_child(p).
print("\n_get_red_child(p)")
print("Det forventes, at roden ikke har noget rødt barn:", red_black_tree._get_red_child(root))

# Test num_children(p)).
print("\nnum_children(p)")
print("Antallet af børn til roden forventes at være 0:", red_black_tree.num_children(root))

# Test is_leaf(p).
print("\nis_leaf(p)")
print("At roden af træet er et blad, forventes at være True:", red_black_tree.is_leaf(root))

# TODO Test _is_red(p). ---- FAIL - Root isn't colored black as root isn't identified as the root.
print("\n_is_red(p)")
print("At roden er farvet rød, forventes at være False:", red_black_tree._is_red(root))

# TODO: Test _is_red_leaf(p). ---- FAIL- Same as above ^
print("\n_is_red_leaf(p)")
print("At roden af træet er et rødt blad, forventes at være False:", red_black_tree._is_red_leaf(root))

# Test first().
print("\nfirst()")
print("Den første position i træet forventes at være roden, som har elementet med nøglen 10:", red_black_tree.first().key())

# Test last().
print("\nlast()")
print("Den sidste position i træet forventes at være roden, som har elementet med nøglen 10:", red_black_tree.last().key())

# Test before(p)
print("\nbefore(p)")
print("Den position der ligger lige før roden i en inorder traversal af træet, forventes at være None:", red_black_tree.before(root))

# Test after(p) - cannot do until errors thrown from _validate(p) are fixed
print("\nafter(p)")
print("Den position der ligger lige efter roden i en inorder travrsal af træet, forventes at være None:", red_black_tree.after(root))

# Test find_position(k).
print("\nfind_position(k) & __equals__(other)")
print("Det forventes at positionen der indeholder nøglen er rodens position:", red_black_tree.find_position(root_key).__equals__(root))

# Test find_min().
print("\nfind_min()")
print("Det item som har den mindste nøgle i træet forventes at være (10, 'a'):", red_black_tree.find_min())

# Test find_max().
print("\nfind_max()")
print("Det item som har den største nøgle i træet forventes at være (10, 'a'):", red_black_tree.find_max())

# Test find_le(k).
print("\nfind_le(k)")
print("Det item som har en nøgle der er mindre end, eller lig med rodens nøgle, forventes at være (10, 'a'):", red_black_tree.find_le(root_key))

# Test find_lt(k).
print("\nfind_lt(k)")
print("Det forventes, at der ikke er noget item med en nøgle, der er mindre, end rodens nøgle:", red_black_tree.find_lt(root_key))

# Test find_ge(k).
print("\nfind_ge(k)")
print("Det item, som har en nøgle, der er større end, eller lig med rodens nøgle, forventes at være (10, 'a'):", red_black_tree.find_ge(root_key))

# Test find_gt(k).
print("\nfind_gt(k)")
print("Det forventes, at der ikke er noget item med en nøgle, der er større, end rodens nøgle:", red_black_tree.find_gt(root_key))

# Test _replace(p, v).
print("\n_replace(p, v)")
new_item = red_black_tree._Item(20, 'ø')
old_item = red_black_tree._replace(root, new_item)
print("Det forventes at det gamle element indeholdt nøgle-værdi parret (10, a):", old_item._key, old_item._value)

new_root = red_black_tree.root()
new_root_key = new_root.key()
new_root_value = new_root.value()

# Test __getitem__(k).
print("\n__getitem__(k)")
print("Det forventede resultat er værdien 'ø':", red_black_tree.__getitem__(new_root_key))

# Test positions().
print("\npositions()")
keys = []
for p in red_black_tree.positions():
    keys.append(p.element()._key)
print("Test positions som bruger inorder til at iterere over nøglerne i træet:", keys)

# Test __delitem__(k).
print("\n__delitem__(k)")
red_black_tree.__delitem__(new_root_key)
print("Det forventes, at træet efter sletning af item, er tomt:", red_black_tree.is_empty())

# Indsæt et nyt item i træet med __setitem__(k, v).
print("\n__setitem__(k, v)")
red_black_tree.__setitem__(125, 'f')
print("Roden af træet forventes at have elmentet med nøglen 125:", red_black_tree.root().element()._key)

# Kør positions().
print("\npositions()")
keys = []
for p in red_black_tree.positions():
    keys.append(p.element()._key)
print("Test positions som bruger inorder til at iterere over nøglerne i træet:", keys)

# Test delete(p).
print("\ndelete(p)")
latest_root = red_black_tree.root()
red_black_tree.delete(latest_root)
print("Det forventes, at træet efter sletning af den eneste position i træet, er tomt:", red_black_tree.is_empty())

# TODO: Test find_range(start_k, stop_k) - cannot do until tree has more items (Empty error)
# TODO: Test _attach(p, t1, t2) - cannot do until errors thrown from _validate(p) are fixed

print("\n-----------------------------------------------------------------------------------------")