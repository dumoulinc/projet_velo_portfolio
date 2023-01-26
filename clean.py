#Lire tous les fichiers dans le répertoire
import pandas as pd
import datetime

liste_str = ['2019', '2020','2021', '2022']
toutes_annees = pd.concat([pd.read_csv('comptage_velo_'+annee+'.csv') for annee in liste_str])

#Groupe par mois
# normalisation de la date dans le format YYYY-MM-DD HH:MM
toutes_annees['Date'] = toutes_annees['Date'].str.replace("juil.","Jul", regex=False)
toutes_annees['Date'] = pd.to_datetime(toutes_annees['Date'])
toutes_annees.set_index('Date')

#group data by month resample('M') and sum the values

#toutes_annees = toutes_annees.resample('D', on='Date').sum()


#Transforme la date en mois et année seulement
print(toutes_annees)
