#!/usr/bin/env python
# coding: utf-8

# In[4]:


def load_text(filepath):
    """
    Opens a txt file
    """
    with open(filepath, "r") as infile:
        text = infile.read()
    return text

filepath = './telegraaf2.txt'
artikel = load_text(filepath)

import string
def remove_punctuation(input_string):
    """
    Removes all the punctuation in a string and makes string lower case
    """
    translator = str.maketrans('', '', string.punctuation)
    clean_string = input_string.translate(translator)
    clean_string = clean_string.lower()
    cleaned_words = clean_string.split()
    return cleaned_words

cleaned_text = remove_punctuation(artikel)
print(cleaned_text)
print()

#gaat het artikel over het klimaat? 
word_list = [
    "biodiversiteit", "broeikaseffect", "broeikasgassen", "co2-uitstoot",
    "duurzaamheid", "energie", "energietransitie", "groen", "klimaat",
    "klimaatakkoord", "klimaatconferentie", "klimaatcrisis", "klimaatdoelen",
    "klimaatdoelstellingen", "klimaatmaatregel", "klimaatverandering", "milieu",
    "milieubeleid", "opwarming", "ozonlaag", "stikstof", "zeespiegelstijging"
]

def count_words(cleaned_text, word_list):
    word_count = {}
    for word in cleaned_text:
        if word in word_list:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    return word_count

result = count_words(cleaned_text, word_list)

for word, count in result.items():
    print(f"{word}: {count} keer voorkomend")
print()
    
def total_word_count(cleaned_text, word_list):
    word_count = count_words(cleaned_text, word_list)
    total_count = sum(word_count.values())
    return total_count

total_count = total_word_count(cleaned_text, word_list)
print(f"Totale woordentelling: {total_count}")    

if total_count >= 3:
    print('Dit artikel gaat over het klimaat')
else:
    print('Dit artikel gaat niet over het klimaat')

print()
 
#sensationele woorden in het artikel  
word_list = [
    "adembenemend", "alarmerend", "angstaanjagend", "bizar", "bloedstollend", "catastrofe", "chaos", 
    "dramatisch", "dreigend", "explosief", "extreem", "gruwelijk", "huiveringwekkend", "klimaatcatastrofe", 
    "klimaathysterie", "klimaatnoodtoestand", "klimaatsceptici", "ongekend", "ongelofelijk", "onthullend",
    "opwindend", "ramp", "rampzalig", "schandaal", "schokkend", "schrikbarend", "sensatie", "sensationeel", 
    "terreur", "verbijsterend", "vernietigend", "verschrikkelijk", "verwoestend", "vreselijk", "wereldschokkend"
]

result = count_words(cleaned_text, word_list)

for word, count in result.items():
    print(f"{word}: {count} keer voorkomend")
print()

total_count = total_word_count(cleaned_text, word_list)
print(f"Totaal aantal sensationele woorden: {total_count}") 

print()

#genuanceerde woorden in het artikel
word_list = [
    "aangetoond", "diepgaand", "diversiteit", "duurzaamheid", "effect", "effectief", 
    "efficiënt", "empirisch", "energie", "fundamenteel", "gedetailleerd", "geïntegreerd", "genuanceerd",
    "gepast", "informatief", "intrigerend", "klimaatfinanciering", "klimaatverandering", "klimaatwetenschap",
    "kritisch", "milieu", "nauwkeurig", "nuance", "nuanceren", "onderzoek", "pragmatisch", "probleem", 
    "problemen", "relevant", "resultaat", "significante", "suggestief", "tegenstrijdig", "verandering"

]

result = count_words(cleaned_text, word_list)

for word, count in result.items():
    print(f"{word}: {count} keer voorkomend")
print()

total_count = total_word_count(cleaned_text, word_list)
print(f"Totaal aantal genuanceerde woorden: {total_count}") 

#sentiment-analyse
get_ipython().system('pip install pattern --no-deps')
from pattern.nl import sentiment as sentiment_nl

polarity, subjectivity = sentiment_nl(cleaned_text)
print("Polariteit:", polarity, "Subjectiviteit:", subjectivity)

