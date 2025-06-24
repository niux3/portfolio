# Améliorer l'accessibilité quand on fait du routage côté client en JavaScript ?

C’est possible, mais pas sans effort. Dans cet article, je vous montre comment :

- gérer le focus correctement après un changement de page
- informer les lecteurs d’écran grâce aux régions dynamiques (role="status")
- reproduire (ou améliorer) le comportement natif du navigateur

Avec des exemples simples en HTML et JS natif, c'est de ne pas sacrifier l’expérience utilisateur au nom du "tout dynamique".

L'accessibilité est souvent la grande oubliée des SPAs. Pourtant, 97,4 % des pages web présentent encore des erreurs critiques, comme un mauvais focus ou un DOM peu clair pour les lecteurs d'écran.

- Près de 5 à 10 % des utilisateurs utilisent exclusivement le clavier pour naviguer, notamment les personnes atteintes de handicaps moteurs ou visuels. Si le focus est mal géré dans une SPA, l’utilisateur peut se retrouver perdu ou bloqué sans possibilité d’interaction.
- Google prend en compte l’accessibilité dans son score Core Web Vitals, ce qui influence directement le référencement. Une meilleure accessibilité améliore aussi le taux de rétention sur les applications web, réduisant le taux de rebond.

Et vous, comment gérez-vous ces problématiques dans vos applications React, Vue ou Svelte ? Partagez vos retours ou questions en commentaire, je vous lis avec attention !
