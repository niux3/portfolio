# Définir le langage naturel

Si une page ne contient pas de définition explicite du langage naturel dans lequel elle est rédigée, les logiciels risquent de ne pas pouvoir traduire correctement le contenu. Le terme &laquo;&nbsp;langue naturelle&nbsp;&raquo; fait référence à la langue utilisée pour le contenu de la page, et non au langage de programmation. Ce manque d'information peut entraîner des traductions erronées, une mauvaise mise en forme et un contenu difficile à comprendre pour les utilisateurs de lecteurs d'écran.

Vous pouvez définir la langue naturelle d'une page en utilisant l'attribut `lang` sur l'élément `<html>`.
**<span id="exemple-1">Exemple&nbsp;1</span>&nbsp;&ndash;&nbsp;Le français défini comme la langue naturelle de la page**

```html
<!DOCTYPE html>
<html lang="fr">
</html>
```

Vous pouvez également définir un dialecte spécifique de la langue de base.
<br>**<span id="exemple-2">Exemple&nbsp;2</span>&nbsp;&ndash;&nbsp;Le français de France défini comme la langue naturelle de la page**

```html
<!DOCTYPE html>
<html lang="fr-FR">
</html>
```

L'attribut lang est global, ce qui signifie que vous pouvez l'utiliser sur n'importe quel élément, bien qu'il puisse ne pas affecter certains d'entre eux. Il peut être utile si une page est rédigée dans une langue mais contient des passages de texte ou même des mots isolés dans d'autres langues.

**<span id="exemple-3">Exemple&nbsp;3</span>&nbsp;&ndash;&nbsp;Japonais translittéré en écriture latine utilisé sur une page écrite en français.**

```html
<!DOCTYPE html>
<html lang="fr">
    <head></head>
    <body>
        <p>The Wind-Up Bird Chronicle (<span lang="ja-Latn">Nejimakidori Kuronikuru </span>) is a novel published in 1994 by Japanese author Haruki Murakami.</p>
    </body>
</html>
```

Utilisez la pseudoclasse `:lang()` pour ajuster la typographie et la mise en page pour des langues spécifiques.

**<span id="exemple-4">Exemple&nbsp;4</span>&nbsp;&ndash;&nbsp;Sélection de tous les éléments en langue serbe**

```css
:lang(sr) {
    font-family: 'Cyrillic font', sans-serif;
}
```

Les technologies d'assistance et autres logiciels peuvent ne pas être en mesure de déterminer automatiquement la langue naturelle d'une page. Certaines fonctions du HTML et des feuilles de style en cascade (CSS) s'appuient sur ces informations pour aider à localiser le contenu et offrir une excellente expérience utilisateur.

Vous devez définir la langue de chaque page de manière programmatique et explicite en utilisant l'attribut lang sur l'élément `<html>`, comme le montre [l'exemple 1](#exemple-1). Pour les passages de texte écrits dans une langue différente de la langue principale de la page, vous pouvez également utiliser l'attribut, comme le montre [l'exemple 3](#exemple-3). Cela permet aux lecteurs d'écran d'améliorer la prononciation en modifiant les profils vocaux en fonction de certains mots ou phrases.

Utilisez cette fonctionnalité avec parcimonie car le changement de profil vocal peut être gênant en interrompant le flux de lecture. Pour les mots étrangers bien établis, ce n'est pas forcément nécessaire. Des exemples en allemand sont des mots anglais comme &laquo;&nbsp;Download&nbsp;&raquo;, &laquo;&nbsp;Workshop&nbsp;&raquo; ou &laquo;&nbsp;Link&nbsp;&raquo;.

La valeur de l'attribut `lang` doit être une <a href="https://datatracker.ietf.org/doc/html/rfc5646" target="_blank">balise de langue BCP 47</a> valide, composée d'une ou plusieurs balises secondaires. Un *subtag* est une séquence de caractères alphanumériques distingués et séparés des autres subtags par un trait d'union.

La *sous-étiquette* de langue est un code de 2 ou 3 caractères qui définit la langue principale : par exemple, `en` pour l'anglais, `de` pour l'allemand ou `fr` pour le français, comme le montre [l'exemple 5](#exemple-5).

**<span id="exemple-5">Exemple 5</span>&nbsp;&ndash;&nbsp;L'espagnol défini comme la langue naturelle de la page**

```html
<html lang="es"></html>
```

## Sous-étiquettes d'écriture
La sous-étiquette d'écriture facultative est un code de 4 caractères qui définit le système d'écriture utilisé pour la langue, comme le montre [l'exemple 6](#exemple-6).

**<span id="exemple-6">Exemple 6</span>&nbsp;&ndash;&nbsp;Un nom en écriture cyrillique à côté du même nom en écriture latine marqué comme tel**

```html
Никола Јокић (<span lang="sr-Latn">Nikola Jokić</span>).
```

La *sous-étiquette* facultative de région est généralement un code de pays à 2 caractères écrit en majuscules et définit un dialecte de la langue de base, comme le montre [l'exemple 7](#exemple-7).

**<span id="exemple-7">Exemple 7</span>&nbsp;&ndash;&nbsp;L'allemand autrichien défini comme la langue naturelle de la page**

```html
<!DOCTYPE html>
<html lang="de-AT">
</html>
```
Vous devez utiliser le code de langue primaire à deux caractères et n'ajouter des balises secondaires de région que lorsqu'il est nécessaire de différencier le contenu dans différents dialectes qui peuvent ne pas être mutuellement compréhensibles. Pour les utilisateurs de lecteurs d'écran, le fait de ne pas ajouter de sous-tags de région ne devrait pas faire de différence car ils sont généralement ignorés par le logiciel.

Vous pouvez trouver une liste de toutes les étiquettes et sous-étiquettes dans la <a href="https://r12a.github.io/app-subtags/" target="_blank">liste des sous-étiquettes de la langue BCP 47</a>.

## Les avantages
L'attribut `lang` est puissant et affecte de nombreux aspects de l'accessibilité du web et de l'expérience utilisateur en général. Voici ses principaux avantages :

### La technologie d'assistance
Les synthétiseurs vocaux qui prennent en charge plusieurs langues adaptent leur prononciation et leur syntaxe à la langue de la page, prononçant le texte avec l'accent et la prononciation appropriés.

Pour une page au contenu allemand dont la langue est réglée sur l'anglais (`lang="en"`), le logiciel de lecture d'écran peut choisir un profil de voix synthétique anglais et lire le texte allemand avec une prononciation anglaise. Si vous ne définissez aucune langue, les lecteurs d'écran risquent de se rabattre sur les paramètres par défaut du système de l'utilisateur, ce qui peut ne pas être approprié. Le résultat peut être difficile à comprendre, confus ou même complètement erroné.

Tous les lecteurs d'écran ne prennent pas en charge de nombreuses langues. Certains logiciels changent de langue automatiquement, tandis que pour d'autres, les utilisateurs doivent installer et configurer manuellement des voix ou des packs de langues.

La définition de l'attribut permet également au logiciel de traduction en braille d'optimiser la sortie et de l'empêcher de créer par erreur des <a href="https://www.rnib.org.uk/living-with-sight-loss/education-and-learning/braille-tactile-codes/contracted-grade-2-braille-explained/" target="_blank">contractions en braille de grade 2</a>.

### La traduction
Les outils de traduction comme Google Translate utilisent les informations de l'attribut `lang` pour traduire le contenu de la page. Bien que ce type de logiciel soit généralement bon pour détecter automatiquement la langue de la page, un décalage entre la langue réelle et la langue définie peut donner lieu à des <a href="https://www.matuzo.at/blog/lang-attribute/" target="_blank">traductions inattendues et non souhaitées</a>.

### Les citations
Les guillemets peuvent changer en fonction de la langue naturelle de la page. Par exemple, l'anglais utilise des guillemets différents de ceux de l'allemand ou du français, et la bonne définition de lang aide les navigateurs à choisir les glyphes appropriés, comme l'illustrent les exemples [8](#exemple-8), [9](#exemple-9) et [10](#exemple-10).

**<span id="exemple-8">Exemple&nbsp;8</span>&nbsp;&ndash;&nbsp;Guillemets automatiques à l'aide de l'élément `<q>` en anglais**

```html
<p lang="en">
    <q>A quote in English.</q>
</p>
<!-- Résultat : "A quote in English." -->
```
**<span id="exemple-9">Exemple&nbsp;9</span>&nbsp;&ndash;&nbsp;Guillemets automatiques à l'aide de l'élément `<q>` en allemand**

```html
<p lang="de">
<q>Ein Zitat auf Deutsch.</q>
</p>
<!-- Résultat : „Ein Zitat auf Deutsch." -->
```
**<span id="exemple-10">Exemple&nbsp;10</span>&nbsp;&ndash;&nbsp;Guillemets automatiques utilisant l'élément `<q>` en français**

```html
<p lang="fr">
<q>Une citation en français.</q>
</p>
<!-- Résultat : « Une citation en français. » -->
```
### La césure
L'attribut `lang` peut affecter <a href="https://developer.mozilla.org/fr/docs/Web/CSS/hyphens" target="_blank">la césure</a> dans les CSS. Voir l'[exemple&nbsp;11](#exemple-11).

**<span id="exemple-11">Exemple&nbsp;11</span>&nbsp;&ndash;&nbsp;Un paragraphe avec une largeur maximale de 28 caractères et une césure activée**

```css
p {
    max-width: 28ch;
    hyphens: auto;
}
```
Dans les exemples&nbsp;[12](#exemple-12), [13](#exemple-13) et [14](#exemple-14), vous pouvez voir comment le même paragraphe écrit en allemand, avec une valeur d'attribut lang différente, est rendu différemment dans Google Chrome. Les mots ne s'interrompent pas du tout ou s'interrompent à des positions différentes. Seuls le premier et le deuxième exemples sont corrects. Il convient de noter que les navigateurs se comportent différemment.

**<span id="exemple-12">Exemple&nbsp;12</span>&nbsp;&ndash;&nbsp;Texte allemand correctement coupé par un trait d'union dans un paragraphe défini comme allemand**

```html
<p lang="de">
Weit hinten, hinter den Wortbergen, fern der Länder Vokalien und Konsonantien
leben die Blindtexte. Abgeschieden wohnen sie in Buchstabhausen an der Küste
des Semantik, eines großen Sprachozeans. Ein kleines Bächlein namens Duden
fließt durch ihren Ort und versorgt sie mit den nötigen Regelialien.
</p>
<!-- Résultat :
Weit hinten, hinter den Wortbergen,
     fern der Länder Vokalien und Konso-
     nantien leben die Blindtexte. Abge-
     schieden wohnen sie in Buchstab-
     hausen an der Küste des Semantik,
     eines großen Sprachozeans.
     -->
```
**<span id="exemple-13">Exemple&nbsp;13</span>&nbsp;&ndash;&nbsp;Pas de césure du texte allemand dans un paragraphe défini comme anglais**

```html
     <p lang="en">
     Weit hinten,…
     </p>
     <!-- Résultat :
     Weit hinten, hinter den Wortbergen,
     fern der Länder Vokalien und
     Konsonantien leben die Blindtexte.
     Abgeschieden wohnen sie in
     Buchstabhausen an der Küste des
     Semantik, eines großen
     Sprachozeans.
     -->
```
**<span id="exemple-14">Exemple&nbsp;14</span>&nbsp;&ndash;&nbsp;Trait d'union incorrect du texte allemand dans un paragraphe défini comme français**

```html
     <p lang="fr">
     Weit hinten,…
     </p>
     <!-- Résultat :
     Weit hinten, hinter den Wortbergen,
     fern der Länder Vokalien und Konso-
     nantien leben die Blindtexte. Abges-
     chieden wohnen sie in Buchstabhau-
     sen an der Küste des Semantik, eines
     großen Sprachozeans.
     -->
```
### Sélection des polices

Les navigateurs peuvent sélectionner <a href="https://www.w3.org/International/questions/qa-lang-why#fonts" target="_blank">des polices adaptées</a> à la langue pour afficher les détails des caractères idéographiques qui varient d'une langue à l'autre, tels que le chinois, le japonais et le coréen (connus sous le nom de "langues CJK").

### Optimisation des moteurs de recherche (SEO)

Une bonne définition du langage naturel peut améliorer la qualité des résultats de recherche en aidant les moteurs de recherche à la localisation.

### Contrôles de formulaires

Dans certains navigateurs, l'attribut `lang` affecte également la mise en forme des contrôles de formulaire. Par exemple, <a href="https://www.mozilla.org/fr/firefox/new/" target="_blank">Firefox</a> affiche les bons caractères décimaux dans les champs de saisie des nombres en fonction de la langue.
