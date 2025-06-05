# Evidencia2-IMC: Generación y limpieza de gramática
**Frida Xcaret Vargas Trejo - A01707168**
## Descripción
El lenguaje con el que estare trabajando durante esta entrega es el italiano, el cual ess una lengua romance procedente del latín hablado, pertenece a la familia de las lenguas Indo-Europeas. Es el idioma oficial en Italia, Vaticano y San Marino. Se calcula que, en el año 2006, unos 64 millones de ciudadanos europeos hablaban el italiano como lengua materna, y 14,7 millones como segunda o tercera lengua. 

## Estructura
Para mi modelo estare utilizando la estructura basica del idioma **articulo + sustantivo + verbo + predicado (adverbio, conjunción, adjetivo)**. El italiano se distingue por, al igual, español tener distintas conjugaciones, donde los pronombres, sustantivos y verbos deben coincidir en género (masculino o femenino) y número (singular o plural).Con fines de facilitar la gramatica estare usando oraciónes en plural. Para los articulos i y gli son para el masculino plural y le para el femenino plural. Los sustantivos que tienen terminacion en i son masculinos (a excepcion de mani) y aquellos que tienen terminacion en e son femenininos.

Ejemplo: Le mele sono grandi.
* Articulo: Le
* Sustantivo: mele
* Verbo: sono 
* Predicado: grandi

## Modelo 
![Gramatica Inicia](/modelo.png)

Etse modelo nos muestra el arbol 
**Articulo**
* le 
* gli
* i

**Sustantivo**
* mani: manos
* sedie: sillas
* finestre: las ventanas
* mele: las manzanas
* stelle: las estrellas
* elefanti: los elefantes
* bambini: los niños
* cani: los perros
* gatti: los gatos
* fiori: las flores

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
La gramática es un sistema formal que define un conjunto de reglas para generar cadenas válidas dentro de un lenguaje. Sirve como modelo para construir oraciones sintácticamente correctas o secuencias con significado en un lenguaje formal. El parser o analisis sintaxico es el segundo paso después del analisis lexico, checa la estractura sintactica de la entrada. Su principal objetivo es crear un arbol sintaxico, una representación del codigo que refleja la estructura gramatical. Para poder llevar a cabo un parser primero  **implementare LL1** (Left Left Look Ahead), con el proposito de eliminar la ambiguedad y la recursion a la izquierda.

**Gramatica Inicial:** 
Mi gramatica inicial es capaz de producir oraciónes para sujetos en plural. Con fines de una gramatica efectiva la estuctura base sera **Articulo + Sutantivo + Predicado** (Este por lo general es un verbo + (adjetivo, adverbio) **+ Complemento**. La gramatica puede producir oraciones mas complejas debido a que también se permiten las conjunciones permitiendo oraciónes como: **i cani e i gatti e gli elefanti corrono** (contien 3 sujetos) o **i fiori corrono veloci e sono belli** (contiene dos verbos con su respectivo adjetivo). 

```
Oración → Sujeto Predicado
                
Predicado →Verbo | Verbo Complemento | Verbo Adjetivo| Verbo Adverbio| Predicado Conjunción Predicado
   
Complemento → Sustantivo | Adjetivo | Complemento Conjunción Complemento

Sujeto → Articulo Sustantivo | Sujeto Conjunción Sujeto                 

Articulo → 'le' | 'gli' | 'i'

Sustantivo → 'mani' | 'sedie' | 'finestre' | 'mele'  | 'stelle' | 'elefanti' | 'bambini'  | 'cani' | 'gatti' | 'fiori'

Verbo → 'sono' | 'corrono' | 'saltano'

Adverbio → 'sempre' | 'presto' | 'spesso'

Adjetivo → 'grandi' | 'veloci' | 'belli'

Conjunción → 'e' | 'o'
```
## Eliminar la ambiguedad
Actualmente mi gramatica cuenta con ambiguedad, esta surge cuando un string puede ser implementado por mas de un arbol **E-> E + E | E * E | id** . En mi gramatica un ejemplo de ambiguedad esta en **Sujeto → Sujeto Conjunción Sujeto**  permite agrupar los sujetos de mas de una forma (i cani e i gatti) e gli elefanti - i cani e (i gatti e gli elefanti). 

Para eliminar la ambigüedad, se deben usar  estados intermedios y producciones que indiquen una precedencia en cada línea que se llama a sí misma dos veces en la misma reglas. Basandome en la bibliografía:

E → E + T | T 

T → T * F | F

F → id	

Para **Sujeto → Sujeto Conjunción Sujeto** 

1. Creo un estado intermedio llamado Sujeto2 y lo coloco al final evitando que exita dos posibles caminos para Sujeto **Sujeto → Articulo Sustantivo | Sujeto Conjunción Sujeto2**
2. El Sujeto2 solo puede ser articulo + sustantivo **Sujeto2 → Articulo Sustantivo**

Para **Predicado → Predicado Conjunción Predicado**
1. Creo un estado intermedio llamado Predicado2 y lo coloco al final evitando que exitan dos posibles caminos Predicado **Predicado -> Verbo | Verbo Complemento | Verbo Adjetivo | Verbo Adverbio | Predicado Conjuncion Predicado2**
2. Indico precedencia **Predicado2 -> Verbo | Verbo Complemento | Verbo Adjetivo | Verbo Adverbio**


Para **Complemento → Complemento Conjunción Complemento**
1. Creo un estado intermedio llamado Complemento2 y lo coloco al final evitando que exitan dos Complemento **Complemento ->  Adjetivo | Complemento Conjuncion Complemento2**
2. Indico precedencia  **Complemento2 ->  Adjetivo**

```
Oracion -> Sujeto Predicado
                
Predicado -> Verbo | Verbo Complemento | Verbo Adjetivo | Verbo Adverbio | Predicado Conjuncion Predicado2
   
Predicado2 -> Verbo Complemento | Verbo Adjetivo | Verbo Adverbio 
                           
Complemento → Sustantivo | Adjetivo | Complemento Conjunción Complemento2
                           
Complemento2 -> Sustantivo | Adjetivo 
                           
Sujeto -> Articulo Sustantivo | Sujeto Conjuncion Sujeto2               

Sujeto2 -> Articulo Sustantivo 
```
## Eliminar la recursion izquierda
Mi gramatica tambien cuenta con recursion a la izquierda, la recursión a la izquierda se presenta cuando una regla esta seguida por el mismo no terminal:  S ⇒ S | a | b, esto no es deseable ya que puede causar un loop infinito. Por ejemplo en mi gramatica la recursion se presenta en **Predicado -> Verbo | Verbo Complemento | Verbo Adjetivo | Verbo Adverbio | Predicado Conjuncion Predicado2**, ya que esta permitiendo que un no terminal (Predicado) se derive a si mismo. Para eliminar la recursión por la izquierda, en base a la bibliografía eliminaremos los no terminales que se derivan a si mismos utilize el siguiente proceso :  

**S ⇒ S a | S b | c | d**

**S ⇒ cS' | dS'**

**S' ⇒ ε | aS' | bS'**
 
Para **Predicado -> Verbo | Verbo Complemento | Verbo Adjetivo | Verbo Adverbio | Predicado Conjuncion Predicado2**
1. Creamos una nueva regla:
PredicadoP -> 
2. Eliminamos el no terminal que se repite y agregamos PredicadoP final de cada no terminal:
**Predicado ->Verbo PredicadoP | Verbo Complemento PredicadoP | Verbo Adjetivo PredicadoP| Verbo Adverbio PredicadoP**
3. Incluimos en la nueva regla el no terminal que eliminamos de la regla anterior, renombrando el que se repetia y pansandolo al final, incluimos un nulo: 
**PredicadoP -> Conjuncion Predicado2 PredicadoP | ε**

Para **Complemento → Sustantivo | Adjetivo | Complemento Conjunción Complemento2**
1. Complemento ->
2. **Complemento → Sustantivo ComplementoP | Adjetivo ComplementoP**
3. **ComplementoP → Conjunción Complemento2  ComplementoP | ε** 
* Pare evitar ambiguedades se elimina elimino Adjetivo de Complemento → Sustantivo ComplementoP | Adjetivo ComplementoP
  Complemento → Sustantivo ComplementoP
* Pare evitar ambiguedades se elimina elimino Sustantivo de Complemento2 -> Sustantivo | Adjetivo 
  Complemento2 -> Adjetivo 

Para **Sujeto -> Articulo Sustantivo | Sujeto Conjuncion Sujeto2**
1. Separamos la recursión izquierda reescribiendo la regla con un inicio fijo seguido de un nuevo no terminal: **Sujeto -> Pronombre Sustantivo SujetoP** 
2.Creamos una nueva regla para manejar las repeticiones de la parte recursiva:  **SujetoP -> Conjuncion Sujeto2 SujetoP | ε**

```
Oracion -> Sujeto Predicado 
                           
Predicado -> Verbo PredicadoP | Verbo Complemento PredicadoP | Verbo Adjetivo PredicadoP | Verbo Adverbio PredicadoP
                           
PredicadoP -> Conjuncion Predicado2 PredicadoP | 

Predicado2 -> Verbo | Verbo Complemento | Verbo Adjetivo | Verbo Adverbio

Complemento -> Sustantivo ComplementoP
                           
ComplementoP -> Conjuncion Complemento2 ComplementoP | 

Complemento2 -> Adjetivo

Sujeto -> Articulo Sustantivo SujetoP
                           
SujetoP -> Conjuncion Sujeto2 | 

Sujeto2 -> Articulo Sustantivo
```
## Pruebas 
Para probar mi gramatica implemente python usando nltk.CFG (para definir gramaticas libres de contexto)y nltk.ChartParser(para analizar las oraciones). Para probar el programa descargue el archivo **recursion.py** y corralo. 

**Correctas**
* i cani e i gatti e gli elefanti corrono

![Gramatica Inicia](/prueba1.png)

* gli elefanti saltano spesso

![Gramatica Inicia](/prueba2.png)

* i bambini saltano

![Gramatica Inicia](/prueba3.png)

* le mele sono grandi
  
![Gramatica Inicia](/prueba4.png)

* i fiori corrono veloci e sono belli

![Gramatica Inicia](/prueba5.png)

**Incorrectas**
* corrono i cani
* i cani e corrono
* i cani grandi
* e i cani corrono
* i cani corrono veloci e
  
![Gramatica Inicia](/prueba6.png)


## Jerarquia Chomsky
La jerarquía de Chomsky fue propuesta por el lingüista y científico computacional Noam Chomsky en 1956 con el propósito de clasificar las gramáticas formales según su capacidad expresiva, es decir, según el tipo de lenguajes que pueden generar.

Esta jerarquía tiene cuatro niveles, desde los más generales (más poderosos, pero menos estructurados) hasta los más restringidos (más estructurados, pero con menor poder expresivo). 

La gramatica antes de eliminar (recursion izquierda y ambiguedad) y después  es de **tipo 2**, es decir una gramatica libre de contexto. Todos tienen un único no terminal en el lado izquierdo y no dependen del contexto en el que aparece ese símbolo para aplicarse. Cada producción tiene la forma A → α, donde A es un no terminal y α es una cadena de terminales y no terminales. 

## Complejidad 
La implementación de nuestro analizador gramatical tiene una complejidad temporal aproximada de O(n), donde n es la longitud de la entrada. Los principales factores que determinan esta complejidad son los siguientes:
* Tokenización: Este proceso implica recorrer la oración una vez para dividirla en tokens, lo que conlleva una complejidad de O(n).
* Análisis sintáctico: Utilizamos el ChartParser de NLTK, que implementa el algoritmo de Earley. Aunque en el peor de los casos este algoritmo puede tener una complejidad de O(n³), en la práctica, nuestra gramática ha sido diseñada para ser no ambigua y determinista, lo que reduce la complejidad esperada a un comportamiento cercano a O(n) en la mayoría de los casos.
* Casos de prueba: Cada oración de prueba se procesa de forma independiente, por lo que el análisis de m oraciones tiene una complejidad total de O(m), asumiendo que cada oración tiene una longitud acotada.

## Referencias
- C. (2003, September 15). *Lengua romance*. Wikipedia.org; Wikimedia Foundation, Inc. [https://es.wikipedia.org/wiki/Idioma_italiano](https://es.wikipedia.org/wiki/Idioma_italiano)
- Introduction To Grammar in Theory of Computation. (2021, January 16). GeeksforGeeks. [https://www.geeksforgeeks.org/introduction-to-grammar-in-theory-of-computation/]
- Construction of LL(1) Parsing Table. (2019, February 27). GeeksforGeeks. [https://www.geeksforgeeks.org/construction-of-ll1-parsing-table/]
- Removing Direct and Indirect Left Recursion in a Grammar. (2019, November 13). GeeksforGeeks. [https://www.geeksforgeeks.org/removing-direct-and-indirect-left-recursion-in-a-grammar/]
