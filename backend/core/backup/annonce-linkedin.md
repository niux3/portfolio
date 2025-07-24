# Savez-vous comment conserver efficacement les N derniers éléments dans une boucle Python ?

Beaucoup utilisent des listes, mais il existe une solution bien plus élégante et rapide : collections.deque.
J’ai rédigé un petit article technique pour partager ce pattern que j’utilise souvent, notamment dans les traitements de logs ou l'analyse de fichiers.

Au programme : deque, yield, et des exemples concrets.

l'article est ici : [lien]

# Vous avez besoin de trouver les N plus petits ou plus grands éléments d’une liste en Python ?

Oubliez les tris complets quand N est petit : heapq.nlargest() et heapq.nsmallest() sont là pour ça.
Ce module vous permet d’accéder efficacement aux extrêmes d’une collection, avec des performances adaptées aux gros volumes.

Dans mon nouvel article, je vous explique :

- Pourquoi et quand utiliser un tas (heap)
- Comment cela fonctionne en coulisses
- Et comment appliquer cela à des objets complexes

Bonus : visualisation ASCII de la structure du heapq

l'article est ici : [lien]
