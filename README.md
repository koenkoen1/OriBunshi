# Mijn Project

Bij het probleem "Protein Pow(d)er" van de minor programmeren van de UvA is de opdracht om een eiwit zo te vouwen dat het maximale stabiliteit krijgt. Het eiwit kan drie typen aminozuren bevatten: 'H' voor hydrofoob, 'P' voor polair en 'C' voor het aminozuur cysteïne. Als twee H's naast elkaar liggen in het (2D of 3D) grid zonder direct verbonden te zijn, krijgt het eiwit -1 stabiliteit. Voor twee C's naast elkaar krijgt het eiwit -5 stabiliteit. Voor een C en H naast elkaar krijgt het molecuul -1 stabiliteit. Hoe lager het getal voor stabiliteit wordt, hoe stabieler het eiwit.

## Aan de slag (Getting Started)

### Analyse Toestandsruimte en Doelfunctie
__Toestandsruimte__

Een bovengrens van de toeststandsruimte van dit probleem is:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src="https://latex.codecogs.com/gif.latex?\left\begin{Bmatrix}&space;1&space;&&space;\text{~~voor&space;}&space;0&space;\leq&space;n&space;\leq&space;2,&space;\\&space;3&space;^&space;{n-2}&space;&&space;\text{~~~~~~~~voor&space;}&space;n&space;>&space;2,&space;\end{matrix}\right." title="\left\begin{Bmatrix} 1 & \text{~~voor } 0 \leq n \leq 2, \\ 3 ^ {n-2} & \text{~~~~~~~~voor } n > 2, \end{matrix}\right." />

waarin <img src="https://latex.codecogs.com/gif.latex?n" title="n" /> het aantal aminozuren in het eiwit is en <img src="https://latex.codecogs.com/gif.latex?x" title="x" /> het aantal duplicaten ontstaan door spiegelvlakken.

Deze bovengrenzen zijn bepaald vanuit een beginsituatie met een eiwit van 1 aminozuur, die een toeststandsruimte van 1 geeft, waaraan een voor een aminozuren toegevoegd kunnen worden. Het eerste aminozuur dat wordt toegevoegd kan op 4 plaatsen worden toegevoegd, namelijk links van, rechts van, onder of boven het aminozuur dat er al ligt. Om rotatieduplicaten te voorkomen, kunnen we direct concluderen dat deze vier situaties in wezen één en dezelfde zijn, wat een toeststandsruimte van 1 oplevert voor het twee-aminozurige eiwit. Ieder aminozuur dat vanaf nu wordt toegevoegd kan op maximaal drie plaatsen worden gelegd, namelijk de drie plaatsen waar het voorgaande aminozuur nog geen verbinding heeft, mits daar nog geen aminozuur ligt. Dat geeft ons de hierboven getoonde bovengrenzen van de toestandsruimte.

Deze bovengrens kan aangescherpt worden, bijvoorbeeld door de duplicaten ontstaan door spiegelvlakken weg te filteren.

__Doelfunctie__

De doelfunctie van dit probleem is gedefinieerd als de stabiliteit van het eiwit, zoals beschreven in de inleiding. Hoe lager deze stabiliteit, hoe beter de oplossing. De ondergrens van de doelfunctie ligt dus aan de kant van de beste oplossing, terwijl de bovengrens de slechts mogelijke oplossing representeert. De gevonden onder- en bovengrens van onze doelfunctie zijn:

* ondergrens: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img src="https://latex.codecogs.com/gif.latex?-(H&space;&plus;&space;5C&space;&plus;&space;5)" title="-(H + 5C + 5)" />,
* bovengrens: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img src="https://latex.codecogs.com/gif.latex?0" title="0" />,

waarin <img src="https://latex.codecogs.com/gif.latex?H" title="H" /> en <img src="https://latex.codecogs.com/gif.latex?C" title="C" /> het aantal aminozuren van type H respectievelijk C zijn.

De bovengrens komt voor in situaties waarbij geen enkele H en/of C aan elkaar grenzen. De ondergrens is bepaald vanuit het gegeven dat elk H en C aminozuur maximaal twee ongebonden buren kan hebben, behalve de aminozuren aan de uiteinden, die er drie hebben. Voor een niet-uiteinde H levert dit een minimale stabiliteit van -2 op, als de H aan twee H's of C's grenst, en voor een niet-uiteinde C een minimum van -10, als de C aan twee C's grenst. Aangezien elke stabiliserende verbinding twee aminozuren betreft, moet de minimale stabiliteit per aminozuur nog gehalveerd worden. Dus een H levert maximaal -1 op en een C maximaal -5. Omdat de uiteinden nog een extra buur hebben, kan daar maximaal nog een winst van (-5 + -5) / 2 behaald worden, in het geval dat de uiteinden twee C aminozuren zijn. Dat alles tezamen levert de hierboven getoonde ondergrens.


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

Eerst moet gekozen worden of een standaard eiwit of zelfgemaakt eiwit gebruikt zal worden. Kies dan het gewenste standaard eiwit of voer de aminozuur sequentie in.  
Daarna moet het laadproces gekozen worden: 'direct' voor een rechte lijn, 'acids' voor eigen toekenning van coördinaten of 'depth' om een depthfirst algoritme toe te passen. 'greedyadd' werkt nog niet.

Zodra het eiwit geladen is, kan gebruik gemaakt worden van 'draw' om het te tekenen en 'turn' + id + richting om vanaf het zoveelste aminozuur de opvolgende keten te draaien in de bepaalde richting.  
Verder kan gebruik gemaakt worden van 'spiral' om het eiwit zoveel mogelijk in spiraalvorm te krijgen en 'random' + nummer om over zoveel keer het eiwit op willekeurige manieren te draaien en het eiwit met de beste gevonden stabiliteit te nemen.

## Auteurs (Authors)

* Maud van Boven
* Koen Dielhoff
* Koen van der Kamp

## Dankwoord (Acknowledgments)

* StackOverflow
* minor programmeren van de UvA
