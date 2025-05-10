import nltk
from nltk import CFG

gramatica = CFG.fromstring("""
Oracion -> Sujeto Predicado OracionP| Adverbio OracionP
                           
OracionP -> Conjuncion Oracion2 OracionP| 

Oracion2 -> Sujeto Predicado | Oracion Adverbio

Predicado -> Verbo PredicadoP | Verbo Complemento PredicadoP | Verbo Adjetivo PredicadoP | Verbo Adverbio PredicadoP
                           
PredicadoP -> Conjuncion Predicado2 PredicadoP | 

Predicado2 -> Verbo | Verbo Complemento | Verbo Adjetivo | Verbo Adverbio

Complemento -> Sustantivo ComplementoP
                           
ComplementoP -> Conjuncion Complemento2 ComplementoP | 

Complemento2 -> Adjetivo

Sujeto -> Articulo Sustantivo SujetoP
                           
SujetoP -> Conjuncion Sujeto2 SujetoP | 

Sujeto2 -> Articulo Sustantivo

Articulo -> 'le' | 'gli' | 'i'

Sustantivo -> 'mani' | 'sedie' | 'finestre' | 'mele' | 'stelle' | 'elefanti' | 'bambini' | 'cani' | 'gatti' | 'fiori'

Verbo -> 'sono' | 'corrono' | 'saltano'

Adverbio -> 'sempre' | 'presto' | 'spesso'

Adjetivo -> 'grandi' | 'veloci' | 'belli'

Conjuncion -> 'e' | 'o'
""")

parser = nltk.ChartParser(gramatica)

def marcar_epsilon(tree):
    if isinstance(tree, nltk.Tree):
        if len(tree) == 0:
            tree.append('(ε)')
        else:
            for child in tree:
                marcar_epsilon(child)

oraciones = [
    # Correctas
    "i cani e i gatti e gli elefanti corrono",
    "gli elefanti saltano spesso",
    "i bambini saltano",
    "le mele sono grandi",
    "i fiori corrono veloci e sono belli",
    # Incorrectas
    "corrono i cani",
    "i cani e corrono",
    "i cani grandi",
    "e i cani corrono",
    "i cani corrono veloci e"
]

for oracion in oraciones:
    print(f"\nProbando: \"{oracion}\"")
    tokens = oracion.split()
    trees = list(parser.parse(tokens))
    if trees:
        print(f" Árboles generados: {len(trees)}")
        for i, tree in enumerate(trees, 1):
            marcar_epsilon(tree)  # Agrega (ε) en nodos vacíos
            print(f"\nÁrbol {i}:")
            tree.pretty_print()
    else:
        print(" No se generaron árboles.")


