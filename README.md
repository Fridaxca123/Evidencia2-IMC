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

Sujeto → Pronombre Sustantivo | Sujeto Conjunción Sujeto                 

Pronombre → 'le' | 'gli' | 'i'

Sustantivo → 'mani' | 'sedie' | 'finestre' | 'mele'  | 'stelle' | 'elefanti' | 'bambini'  | 'cani' | 'gatti' | 'fiori'

Verbo → 'sono' | 'corrono' | 'saltano'

Adverbio → 'sempre' | 'presto' | 'spesso'

Adjetivo → 'grandi' | 'veloci' | 'belli'

Conjunción → 'e' | 'o'
```

Esta gramatica cuenta con ambiguedad y recursion a la izquierda, lo que hace que exista mas de un arbol como para la oración "i cani e i gatti e gli elefanti corrono" (el elefante, el gato y el perro corren). En este caso la recursión a la izquierda estan en Oracion -> Oracion Conjuncion Oracion, y que esta permitiendo que un no terminal (Oracion) se derive a si mismo. Por otro lado la ambiguedad se demuestra ya que existe mas de un arbol para una misma oración. 

![Gramatica Inicia](/gramaticaInicial.png)

**Eliminar la ambiguedad**

Para eliminar la ambigüedad, necesitamos usar estados intermedios en cada línea que se llama a sí misma dos veces en la misma opción, por ejemplo, en Oración → Oración Conjunción Oración| Sujeto Predicado | *otros estados*, que se resolvería con el estado intermedio Oracion -> S S -> *otros estados*. También añadí estos estados en  VP y NP.

```
S -> S Conjuncion NP VP | NP VP
NP -> Pronombre Sustantivo | NP Conjuncion NP
VP -> Verbo | Verbo Adjetivo | Verbo Adverbio
```
**Eliminar la recursion izquierda**
Para eliminar la recursión por la izquierda, necesitamos deshacernos de las aquellos no terminales que se derivan a si mismos:
```
S -> NPLista VP
NPLista -> NP NPListaRest
NPListaRest -> Conjuncion NP NPListaRest | 
NP -> Pronombre Sustantivo
VP -> Verbo VPmod
VPmod -> Adjetivo | Adverbio |

```
## Pruebas 
**Correctas**
* i cani e i gatti e gli elefanti corrono
* gli elefanti saltano spesso
* i bambini saltano"
* le mele sono grandi
* i cani corrono

**Incorrectas**
* corrono i cani
* i cani e corrono
* i cani grandi
* e i cani corrono
* i cani corrono veloci e

## Jerarquia Chomsky
La jerarquía de Chomsky fue propuesta por el lingüista y científico computacional Noam Chomsky en 1956 con el propósito de clasificar las gramáticas formales según su capacidad expresiva, es decir, según el tipo de lenguajes que pueden generar.

Esta jerarquía tiene cuatro niveles, desde los más generales (más poderosos, pero menos estructurados) hasta los más restringidos (más estructurados, pero con menor poder expresivo). 

La gramatica antes de eliminar (recursion izquierda y ambiguedad) y después  es de **tipo 2**, es decir una gramatica libre de contexto. Todos tienen un único no terminal en el lado izquierdo y no dependen del contexto en el que aparece ese símbolo para aplicarse. Cada producción tiene la forma A → α, donde A es un no terminal y α es una cadena de terminales y no terminales. 

## Complejidad 
La complejidad de 

## Referencias
- C. (2003, September 15). *Lengua romance*. Wikipedia.org; Wikimedia Foundation, Inc. [https://es.wikipedia.org/wiki/Idioma_italiano](https://es.wikipedia.org/wiki/Idioma_italiano)
- Introduction To Grammar in Theory of Computation. (2021, January 16). GeeksforGeeks. [https://www.geeksforgeeks.org/introduction-to-grammar-in-theory-of-computation/]
- Construction of LL(1) Parsing Table. (2019, February 27). GeeksforGeeks. [https://www.geeksforgeeks.org/construction-of-ll1-parsing-table/]
