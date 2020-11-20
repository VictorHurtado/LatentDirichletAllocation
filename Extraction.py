import csv
import itertools 
import pandas as pd


def format_text(strings):
    accents = ['á','é','í','ó','ú']
    vowels = ['a','e','i','o','u']
    for i, vowel in enumerate(vowels):
        strings = strings.str.replace(accents[i],vowel)
    strings = strings.str.replace('[^a-zñA-Z ]', "")
    strings = pd.Series(list(map(lambda x: x.lower(), strings)))
    return strings


def arrayStrings(strings):
    strings_array = list(map(lambda x: x.split(), strings))#lista de las palabras de cada oracion
    strings_array = list(itertools.chain.from_iterable(strings_array))  # luego juntamos cada oracion en una misma lista
    return strings_array

def extract(path):
    
    with open(path,'r') as in_file:
        stripped=  (line.strip() for line in in_file)
        lines= (line.split (",") for line in stripped if line)

        with open('files/Busquedas.csv','w') as in_file_csv:
            writer = csv.writer(in_file_csv)
            writer.writerows(lines)