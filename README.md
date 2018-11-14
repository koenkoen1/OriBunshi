![equation](http://latex.codecogs.com/gif.latex?Concentration%3D%5Cfrac%7BTotalTemplate%7D%7BTotalVolume%7D)  

# Mijn Project

Bij het probleem "Protein Pow(d)er" van de minor programmeren van de UvA is de opdracht om een eiwit zo te vouwen dat het maximale stabiliteit krijgt. Het eiwit kan drie typen aminozuren bevatten: 'H' voor hydrofoob, 'P' voor polair en 'C' voor het aminozuur cysteïne. Als twee H's naast elkaar liggen in het (2D of 3D) grid zonder direct verbonden te zijn, krijgt het eiwit -1 stabiliteit. Voor twee C's naast elkaar krijgt het eiwit -5 stabiliteit. Voor een C en H naast elkaar krijgt het molecuul -1 stabiliteit. hoe lager het getal voor stabiliteit wordt, hoe stabieler het eiwit.
^Hier staat een korte beschrijving van het probleem evt. met plaatje.^

## Aan de slag (Getting Started)

### Analyse Toestandsruimte en Doelfunctie
__Toestandsruimte__

Bovengrens: $2 * 3^(n-3) - x$, voor $n > 2$, waarin $x$ duplicaten ontstaan door spiegelingen
en rotaties zijn.

__Doelfunctie__

### Vereisten (Prerequisites)

Deze codebase is volledig geschreven in [Python3.7.1](https://www.python.org/downloads/). In requirements.txt staan alle benodigde packages om de code succesvol te draaien. Deze zijn gemakkelijk te installeren via pip dmv. de volgende instructie:

```
pip install -r requirements.txt
```

### Structuur (Structure)

Alle Python scripts staan in de folder Code. In de map Data zitten alle input waardes en in de map resultaten worden alle resultaten opgeslagen door de code.

### Test (Testing)

Om de code te draaien gebruik de instructie:

```
python main.py
```

Eerst moet gekozen worden of een standaard eiwit of zelfgemaakt eiwit gebruikt zal worden. Kies dan het gewenste standaard eiwit of voer de aminozuur sequentie in. Daarna moet het laadproces gekozen worden: 'direct' voor een rechte lijn, 'acids' voor eigen toekenning van coördinaten of 'depth' om een depthfirst algoritme toe te passen. 'greedyadd' werkt nog niet.
Zodra het eiwit geladen is, kan gebruik gemaakt worden van 'draw' om het te tekenen en 'turn' + id + richting om vanaf het zoveelste aminozuur de opvolgende keten te draaien in de bepaalde richting. Verder kan gebruik gemaakt worden van 'spiral' om het eiwit zoveel mogelijk in spiraalvorm te krijgen en 'random' + nummer om over zoveel keer het eiwit op willekeurige manieren te draaien en de het eiwit met de beste gevonden stabiliteit te nemen.

## Auteurs (Authors)

* Maud van Boven
* Koen Dielhoff
* Koen van der Kamp

## Dankwoord (Acknowledgments)

* StackOverflow
* minor programmeren van de UvA
