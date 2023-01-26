import matplotlib.pyplot as plt
import pandas as pd
toutes_annees = pd.read_csv('data/toutes_annees.csv', sep=',')


#Création d'un histogramme pour chaque station de comptage
for station in toutes_annees['Nom']:
    plt.figure(figsize=(35,25))
    plt.style.use('ggplot')
    plt.bar(toutes_annees.columns[1:-3], toutes_annees.loc[toutes_annees['Nom'] == station].iloc[0,1:-3])
    plt.title('Station de comptage ' + station, fontsize=30)
    plt.xticks(rotation=45, fontsize=15)
    plt.ylabel('Nombre de vélos', fontsize=20)
    plt.yticks(fontsize=15)
    plt.savefig('graphs/' + station + '.png')
    plt.close()

