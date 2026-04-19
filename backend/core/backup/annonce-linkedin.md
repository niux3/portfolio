Django : sécuriser vos CreateView contre les race conditions

Aujourd'hui, j'ai publié un article (suite à un commentaire sur LinkedIn) sur un bug silencieux qui touche beaucoup d'applications Django en production que j'ai constaté régulièrement : la vente de stock fantôme.

Pourquoi une CreateView parfaitement fonctionnelle en local peut-elle générer des stocks négatifs une fois en ligne ? Qu'est-ce qu'une race condition et comment Django peut-il y être vulnérable ? Comment utiliser correctement @transaction.atomic et select_for_update() ? Pourquoi models.F() est un allié précieux pour les mises à jour atomiques ? Comment transposer ces bonnes pratiques dans Django REST Framework ?

Dans cet article, je détaille :

    le scénario concret qui fait planter une gestion de stock

    les outils natifs de Django pour garantir l'intégrité des données

    une version robuste pour les vues classiques et pour les API DRF

    les erreurs à ne pas commettre quand on manipule des ressources partagées

Si vous développez une boutique en ligne, un système de réservation ou toute application où plusieurs utilisateurs peuvent modifier une même ressource, cet article vous évitera des appels clients un dimanche soir.

Django : Pourquoi votre CreateView « simple » peut vendre du stock fantôme

Bonne lecture, et vos retours d'expérience sur les bugs de concurrence sont les bienvenus !

#Django #Python #DRF #WebDevelopment #Backend #Concurrency