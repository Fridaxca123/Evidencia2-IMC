# Evidencia2-IMC: Generación y limpieza de gramática
**Frida Xcaret Vargas Trejo - A01707168**
## Descripción
EL italiano es una lengua romance procedente del latín hablado, pertenece a la familia de las lenguas Indo-Europeas. Es el idioma oficial en Italia, Vaticano y San Marino. Se calcula que, en el año 2006, unos 64 millones de ciudadanos europeos hablaban el italiano como lengua materna, y 14,7 millones como segunda o tercera lengua. 

## Estructura
Para mi modelo estare utilizando una estructura de sujeto + verbo + predicado. El italiano se distingue por como el español tener distintas conjugaciones, donde los pronombres, sustantivos y verbos deben coincidir en género (masculino o femenino) y número (singular o plural).

Ejemplo: La donna legge un libro 
Sujeto: La donna 
Verbo: legge 
Predicado: un libro
Plural: Le donne leggono un libro 

## Plural 
Para usar el plural utilizare las siguientes reglas:
* Solo tomare en cuenta los verbos regulares 
* Pronombre le para femenino
* Pronombre I para masculino si el sustantivo comienza con consontante 
* Pronombre gli para masculino si el sustantivo comienza con vocal
* Si un sustantivo termina en -e es femenino
* Si termina en -i, suele ser masculino.
* Los adverbios no tienen género.
  
## Modelo 

**Sujeto (Pronombre + Sustantivo)**
* le mani: las manos
* le sedie: las sillas
* le finestre: las ventanas
* le mele: las manzanas
* le stelle: las estrellas
* gli elefanti: los elefantes
* i bambini: los niños
* i cani: los perros
* i gatti: los gatos
* i fiori: las flores

**Verbo:**
* sono: son
* corrono: corren
* saltano: saltan

**Adverbios**
* sempre: siempre 
* presto: nunca
* spesso: a menudo

**Adjetivos**
* grandi: grandes
* veloci: rápidos
* belli: bonitos

**Conjunciones**
* o: o 
* e: y

## Gramatica
La gramática en teoría de la computación es un sistema que define cómo se forman las cadenas de un lenguaje. Sirve para verificar si las oraciones están bien construidas y es la base para analizar lenguajes de programación y naturales.
Un analizador sintáctico LL(1) es una forma de leer una cadena de izquierda a derecha, usando solo un símbolo de adelanto. Es fácil de implementar, no necesita retroceder y construye el árbol de análisis de arriba hacia abajo, lo que lo hace rápido y eficiente para verificar si una cadena cumple con una gramática.

**Gramatica Inicial**
```
Oración → Oración Conjunción Oración| Sujeto Predicado| Oración Adverbio
                
Predicado → Verbo Complemento | Verbo Adjetivo| Verbo Adverbio| Predicado Conjunción Predicado
   
Complemento → Sustantivo | Adjetivo | Complemento Conjunción Complemento

Sujeto → PronombrePlural SustantivoPlural| Sujeto Conjunción Sujeto                 

PronombrePlural → 'le' | 'gli' | 'i'

SustantivoPlural → 'mani' | 'sedie' | 'finestre' | 'mele'  | 'stelle' | 'elefanti' | 'bambini'  | 'cani' | 'gatti' | 'fiori'

Verbo → 'sono' | 'corrono' | 'saltano'

Adverbio → 'sempre' | 'presto' | 'spesso'

Adjetivo → 'grandi' | 'veloci' | 'belli'

Conjunción → 'e' | 'o'
```


## Referencias
- C. (2003, September 15). *Lengua romance*. Wikipedia.org; Wikimedia Foundation, Inc. [https://es.wikipedia.org/wiki/Idioma_italiano](https://es.wikipedia.org/wiki/Idioma_italiano)
- Introduction To Grammar in Theory of Computation. (2021, January 16). GeeksforGeeks. [https://www.geeksforgeeks.org/introduction-to-grammar-in-theory-of-computation/]
- Construction of LL(1) Parsing Table. (2019, February 27). GeeksforGeeks. [https://www.geeksforgeeks.org/construction-of-ll1-parsing-table/]
