import nltk
from nltk import CFG

gramatica = CFG.fromstring("""
S -> NPLista VP
NPLista -> NP NPListaRest
NPListaRest -> Conjuncion NP NPListaRest | 
NP -> Pronombre Sustantivo
VP -> Verbo VPmod
VPmod -> Adjetivo | Adverbio | 

Pronombre -> 'le' | 'gli' | 'i'
Sustantivo -> 'mani' | 'sedie' | 'finestre' | 'mele' | 'stelle' | 'elefanti' | 'bambini' | 'cani' | 'gatti' | 'fiori'
Verbo -> 'sono' | 'corrono' | 'saltano'
Adverbio -> 'sempre' | 'presto' | 'spesso'
Adjetivo -> 'grandi' | 'veloci' | 'belli'
Conjuncion -> 'e' | 'o'
""")

parser = nltk.ChartParser(gramatica)

oraciones = [
    # Correctas
    "i cani e i gatti e gli elefanti corrono",
    "gli elefanti saltano spesso",
    "i bambini saltano",
    "le mele sono grandi",
    "i cani corrono",
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
            print(f"\nÁrbol {i}:")
            tree.pretty_print()
    else:
        print(" No se generaron árboles.")

