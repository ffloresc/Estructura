#Fernanda Flores
#HW2
#Mapas

import re
import csv
from mapas import mapa

file=open('paises.csv')
read=csv.reader(file)

# Parte 1
#a)

lista=[x for x in read if x[2]=='2013']

mapaPais=mapa()

for elemento in lista:
    pais=elemento[0]
    esperanza=float(elemento[1])
    mapaPais[pais]=esperanza

#b) & c)
print("Parte 1\n\n")
print("b) & c)")

for elemento in mapaPais:
    if elemento=='Mexico' or elemento=='Guatemala' or elemento=='Belize' or elemento=='El Salvador' or elemento=='Nicaragua':
        print(elemento, mapaPais[elemento])

#d)
print("\n")

print("d)")
for elemento in mapaPais:
    print(elemento)

#e)
print("\n")

print("e)")    
datoC=0
for elemento in mapaPais:
    if elemento[0]=='C':
        datoC+=1
        print(elemento)
    
#f)

for elemento in mapaPais:
    total=0
    total+=mapaPais[elemento]

print("\n")

print("f)")
print(total/datoC)

###############################################

#Parte 2
print("\n\n\n\n")
print("Parte 2\n\n")
words = "abcdefghijklmnopqrstuvwxyz"
mapaPower=mapa()

def extraer(elemento):
    words = "[abcdefghijklmnopqrstuvwxyz]"
    return re.findall(words, elemento)

relato= "Feeling of Power " +\
      "Isaac Asimov " +\
    "Jehan Shuman was used to dealing with the men in authority on long-embattled earth. " +\
    "He was only a civilian but he originated programming patterns that resulted " +\
    "in self-directing war computers of the highest sort. Generals, consequently " +\
    "listened to him. Heads of congressional committees too. " +\
    "There was one of each in the special lounge of New Pentagon. General Weider " +\
    "was space-burned and had a small mouth puckered almost into a cipher. " +\
    "He smoked Denebian tobacco with the air of one whose patriotism was so notorious, " +\
    "he could be allowed such liberties. " +\
    "Shuman, tall, distinguished, and Programmer-first-class, faced them fearlessly. " +\
    "He said, 'This, gentlemen, is Myron Aub.'" +\
    "'The one with the unusual gift that you discovered quite by accident, '" +\
    "said Congressman Brant placidly. 'Ah.' He inspected the little man with the " +\
    "egg-bald head with amiable curiosity. " +\
    "The little man, in return, twisted the fingers of his hands anxiously. " +\
    "He had never been near such great men before. He was only an aging low-grade " +\
    "technician who had long ago failed all tests designed to smoke out the gifted " +\
    "ones among mankind and had settled into the rut of unskilled labor. There was " +\
    "just this hobby of his that the great Programmer had found out about and was " +\
    "now making such a frightening fuss over. " +\
    "General Weider said, 'I find this atmosphere of mystery childish.' " +\
    "'You won't in a moment,' said Shuman. 'This is not something we can leak to " +\
    "'the firstcomer. Aub!' There was something imperative about his manner of " +\
    "biting off that one-syllable name, but then he was a great Programmer speaking " +\
    "to a mere technician. 'Aub! How much is nine times seven?' " +\
    "Aub hesitated a moment. His pale eyes glimmered with a feeble anxiety. "+\
    "'Sixty-three,' he said. " +\
    "Congressman Brant lifted his eyebrows. 'Is that right?' " +\
    "'Check it for yourself, Congressman.' " +\
    "The congressman took out his pocket computer, nudged the milled edges twice, " +\
    "looked at its face as it lay there in the palm of his hand, and put it back. " +\
    "He said, 'Is this the gift you brought us here to demonstrate. An illusionist?' " +\
    "'More than that, sir. Aub has memorized a few operations and with them he " +\
    "'computes on paper.' " +\
    "'A paper computer?' said the general. He looked pained. "

relato = relato.lower()
nuevoRelato = extraer(relato)
relato = ""
for elemento in range(len(nuevoRelato)):
    relato+=nuevoRelato[elemento]

#a)
for elemento in range(len(relato)):
        mapaPower[relato[elemento]]=0
for x in relato:
    for y in words:
        if x==y:
            mapaPower[x]+=1
    
#b)

print("b)") 

contador=0
for elemento in mapaPower:
    if elemento=='a' or elemento=='e' or elemento=='i' or elemento=='o' or elemento=='u':
        contador+=mapaPower[elemento]
        
        
print("Existen", contador, "vocales.")

#c)
print("\n")

print("c)") 
for elemento in mapaPower:
    print(elemento,": ", mapaPower[elemento])

#d)

print("\n")

print("d)") 
for elemento in words:
        if mapaPower.__contains__(elemento):
            contains="sí"
    
        print(elemento, ": ", contains)