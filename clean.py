#Lire tous les fichiers dans le répertoire
import pandas as pd
import numpy as np

list_df = []

#On demande à l'utilisateur de choisir la période de temps à analyser
annee_debut = input('Année de début: ')
annee_fin = input('Année de fin: ')
liste_annees = []
for annee in range(int(annee_debut), int(annee_fin)+1):
    liste_annees.append(annee)

#Ouverture du fichier de référence
dict = pd.read_csv('data/comptage_velo_velo.csv')

#On enlève les colonnes inutiles
dict = dict.drop(columns=['Ancien_ID', 'Statut', 'Annee_implante'])

#On sépare les colomnes qui permettrons de cartographier les données dans un nouveau dataframe
lat_long = dict[['ID', 'Latitude', 'Longitude']]

#On crée un dictinnaire pour traduire les noms des stations en ID
dict1 = dict.drop(columns=['Latitude', 'Longitude'])
dict = dict1.set_index('Nom')
dict = dict.to_dict()
dict = dict['ID']

#On s'assure que la colonne date est de type datetime
for annee in liste_annees:
    df = pd.read_csv('data/comptage_velo_'+str(annee)+'.csv', sep=',')
    df.rename(columns=dict, inplace=True)
    for colonne in df.columns:
        if type(colonne) == str and colonne != 'Date' and colonne[:8] != 'compteur':
            df = df.drop(columns=colonne)
        elif type(colonne) == str and colonne[:8] == 'compteur':
            df.rename(columns={colonne: colonne[9:]}, inplace=True)
    #Les dates de juillet sont structurées différemment. On doit traduire juil. en Jul pour que la conversion fonctionne
    df['Date'] = df['Date'].str.replace("juil.","Jul", regex=False)
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
    df.set_index('Date')
    list_df.append(df)

#On transpose le dataframe pour avoir les dates en colonnes. Probablement une façon plus élégante de faire ça
toutes_annees = pd.concat(list_df)
toutes_annees.index = toutes_annees['Date']

toutes_annees = toutes_annees.drop(columns=['Date'])
toutes_annees = toutes_annees.resample('MS').sum()
toutes_annees = pd.DataFrame.transpose(toutes_annees)
toutes_annees = toutes_annees.reset_index()
toutes_annees = toutes_annees.rename(columns={'index': 'ID'})
toutes_annees = toutes_annees.rename_axis(None, axis=1)
toutes_annees.index = toutes_annees['ID']
toutes_annees = toutes_annees.drop(columns=['ID'])
toutes_annees = toutes_annees.reset_index()

#On ajoute les coordonnées géographiques et les noms des stations
toutes_annees['ID'] = pd.to_numeric(toutes_annees['ID'])
toutes_annees = toutes_annees.merge(lat_long, on='ID', how='left')
toutes_annees = toutes_annees.merge(dict1, on='ID', how='left')

#On s'assure que le nom des mois soit en français
import locale
locale.setlocale(locale.LC_TIME, 'fr_CA')

for col in toutes_annees.columns:
    try:
        pd.to_datetime(toutes_annees[col])
        toutes_annees = toutes_annees.rename(columns={col: pd.to_datetime(col).strftime('%B %Y')})
    except ValueError:
        pass

#On change les valeurs de 0 par des NaN pour que les mois sans données ne soient pas affichés dans les graphiques
toutes_annees = toutes_annees.replace(0, np.nan)
#print(toutes_annees)

#correction des erreurs dûes aux accents
accents = {'Rachel / Papineau': 'Rachel - Papineau', 'Berri1': 'Berri', 'Notre-Dame': 'Notre-Dame', 'Saint-Antoine': 'Saint-Antoine', 'Saint-Urbain': 'Saint-Urbain', 'Pont Jacques-Cartier': 'Pont Jacques-Cartier', 'Saint-Laurent/Bellechasse': 'Saint-Laurent-Bellechasse', 'Eco-Display Parc Stanley': 'Eco-Display Parc Stanley', 'Edmond Valade': 'Edmond Valade', 'Gouin / Lajeunesse': 'Gouin - Lajeunesse', '16e Avenue / BÃ©langer': '16e Avenue - Bélanger', 'Bennett': 'Bennett', 'Bord-du-Lac vers est': 'Bord-du-Lac vers est', 'Bord-du-Lac vers ouest': 'Bord-du-Lac vers ouest', 'Boyer / Rosemont': 'Boyer - Rosemont', 'Boyer / Everett': 'Boyer - Everett', 'BrÃ©beuf / Rachel': 'Brébeuf - Rachel', 'Christophe-Colomb/Louvain': 'Christophe-Colomb-Louvain', 'CÃ´te Sainte-Catherine / Stuart': 'Côte Sainte-Catherine - Stuart', 'Eco-Display - MÃ©tro Laurier': 'Eco-Display - Métro Laurier', 'Estacade': 'Estacade', 'Maisonneuve / Berri': 'Maisonneuve - Berri', 'Maisonneuve / Plessis': 'Maisonneuve - Plessis', 'Maisonneuve / VendÃ´me': 'Maisonneuve - Vendôme', 'Maisonneuve / Peel': 'Maisonneuve - Peel', 'Maisonneuve / Marcil': 'Maisonneuve - Marcil', 'Maurice-Duplessis': 'Maurice-Duplessis', 'Notre-Dame Est / Bellerive': 'Notre-Dame Est - Bellerive', 'Parc / Duluth': 'Parc - Duluth', 'Parc U-Zelt Test': 'Parc U-Zelt Test', 'Pierre-Dupuy': 'Pierre-Dupuy', 'Piste Des CarriÃ¨res': 'Piste Des Carrières', 'Pont Ile Bizard': 'Pont Ile Bizard', 'Pont Le Gardeur': 'Pont Le Gardeur', 'Querbes / St-Roch': 'Querbes - St-Roch', 'Rachel / HÃ´teldeVille': 'Rachel - HôteldeVille', 'Rachel 3 (Angus)': 'Rachel 3 (Angus)', 'Rachel / Pie IX': 'Rachel - Pie IX', 'RenÃ©-LÃ©vesque / Wolfe': 'René-Lévesque - Wolfe', 'Saint-Laurent U-Zelt Test': 'Saint-Laurent U-Zelt Test', 'Sainte-Croix / Du CollÃ¨ge Sainte-Croix': 'Sainte-Croix - Du Collège Sainte-Croix', 'Souligny / Saint-Ã\x89mile': 'Souligny - Saint-Émile', 'University / Milton': 'University - Milton', 'Valois / la Fontaine': 'Valois - la Fontaine', 'Viger / Saint-Urbain': 'Viger - Saint-Urbain', 'Wellington / Charlevoix': 'Wellington - Charlevoix', 'Camillien-Houde 1': 'Camillien-Houde 1', 'McGill / William': 'McGill - William', 'Remembrance': 'Remembrance', 'REV Bellechasse / 13Ã¨me': 'REV Bellechasse - 13ème', 'REV Berri/SauvÃ© dir sud': 'REV Berri-Sauvé dir sud', 'REV Lajeunesse/SauvÃ© dir nord': 'REV Lajeunesse-Sauvé dir nord', 'REV St-Denis/CarriÃ¨res dir nord': 'REV St-Denis-Carrières dir nord', 'REV St-Denis/CarriÃ¨res dir sud': 'REV St-Denis-Carrières dir sud', 'REV St-Denis/Duluth dir nord': 'REV St-Denis-Duluth dir nord', 'REV St-Denis/Rachel dir sud': 'REV St-Denis-Rachel dir sud', 'Eco-Display - Maisonneuve and Greene': 'Eco-Display - Maisonneuve and Greene'}
toutes_annees['Nom'] = toutes_annees['Nom'].map(accents)
#print(toutes_annees)
toutes_annees.to_csv('data/toutes_annees.csv', index=False)
