#Extraction des données de comptage de vélos de la ville de Montréal

import requests
import pandas as pd
from io import StringIO


annee_debut = input("Année de début: ")
annee_fin = input("Année de fin: ")
liste_annees = []
liste_str = []
for annee in range(int(annee_debut), int(annee_fin)+1): liste_annees.append(annee)
for annee in liste_annees: liste_str.append(str(annee))


for annee in liste_str:
    io_velo = StringIO(requests.get('https://data.montreal.ca/dataset/f170fecc-18db-44bc-b4fe-5b0b6d2c7297/resource/c7d0546a-a218-479e-bc9f-ce8f13ca972c/download/comptage_velo_'+annee+'.csv').text)
    pd_velo = pd.read_csv(io_velo, sep=',')
    pd_velo.to_csv('comptage_velo_'+annee+'.csv', index=False)







