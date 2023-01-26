#Extraction des données de comptage de vélos de la ville de Montréal

import requests
import pandas as pd
from io import StringIO
#Requête pour obtenir les url des fichiers csv de comptage de vélos disponibles
url_list = []
url = requests.get('https://www.donneesquebec.ca/recherche/api/3/action/package_show?id=f170fecc-18db-44bc-b4fe-5b0b6d2c7297').json()
url = url['result']['resources']
for i in range(len(url)):
    url_list.append(url[i]['url'])

#Il y a des erreurs dans l'url des fichiers csv de 2015 et 2016, on les corrige
for url in url_list:
    if url[-8:-4] == '0152':
        url = url.replace(url[-9:], '2015.csv')
    if url[-8:-4] == '0162':
        url = url.replace(url[-9:], '2016.csv')

    #On télécharge les fichiers csv et on les nommes selon l'année
    try:
        io_velo = StringIO(requests.get(url).text)
        pd_velo = pd.read_csv(io_velo, sep=',')
        pd_velo.to_csv('comptage_velo_'+url[-8:], index=False)
    except Exception:
        pass








