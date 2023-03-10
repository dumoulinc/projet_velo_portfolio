

Projet Portfolio

**Automatisation du processus de création d’histogrammes**

Analyse de l’utilisation des pistes cyclables à Montréal



![Carte](/img/1.PNG)



**Christophe Dumoulin**


**Introduction**

Avec l'augmentation signiﬁcative du nombre de cyclistes au Québec ces dernières années,

il est important de comprendre leur répartition géographique aﬁn de mieux répondre à

leurs besoins en matière d'infrastructure et de services. Heureusement, la Ville de Montréal

met à disposition des données récoltées par les stations de comptage via le site web de

Données Québec. Cet exercice vise à trouver une solution pour automatiser le traitement

des données brutes et à produire des visualisations pour une meilleure compréhension de

ces données.


**Extraction des données**

Évidemment, la première étape de ce projet est de récupérer les données. Il est important

de s'assurer de pouvoir accéder à l'ensemble des données disponibles.

La page https://www.donneesquebec.ca/recherche/dataset/vmtl-velos-comptage contient les liens qui

permettent de télécharger les ﬁchiers CSV.

![Page Données Québec](/img/2.PNG)



Il est possible de récupérer chaque lien sur cette page et télécharger le ﬁchier CSV

correspondant. Si la structure du site reste inchangée, le même script pourra être utilisé

pour extraire les données des années suivantes sans modiﬁcation. Les données sont alors

sauvegardées et prêtes à être traitées.


**Nettoyage des données**

En examinant les données téléchargées, il est clair qu'elles sont diﬃciles à comprendre en

raison de la variabilité des fréquences d'échantillonnage et des méthodes de

référencement des stations de comptage. Certaines années présentent un compte de

cyclistes toutes les 15 minutes, tandis que d'autres ne compilent ces données que

quotidiennement. De plus, certains ﬁchiers font référence aux stations de comptage par

leur nom, tandis que d'autres utilisent un identiﬁant au format compteur\_xxxxxxxxxxxx.

Ces incohérences rendent nécessaire un nettoyage et une normalisation des données pour

en faciliter l'analyse et l'interprétation.


![Données 2015](/img/3.PNG)

Données de 2015. Elles sont quotidiennes et utilisent le nom pour faire référence aux stations de

comptage

![Données 2022](/img/4.PNG)

Données de 2022. Elles sont regroupées en sections de 15 minutes et utilisent un identiﬁant pour faire

référence aux stations de comptage.


Pour standardiser et nettoyer les données de comptage de cyclistes, il est nécessaire

d'utiliser des outils de traitement de données tels que Python. Le script clean.py peut

facilement intégrer de nouveaux compteurs ou des données compilées à diﬀérentes

fréquences. Il est également ﬂexible, permettant à l'utilisateur de spéciﬁer la période

d'étude. Le script eﬀectue un nettoyage et une normalisation des données pour en faciliter

l'analyse et l'interprétation. Enﬁn, il crée un nouveau ﬁchier incluant les données de toute

la période étudiée compilées mensuellement, avec une référence géographique pour

chaque station pour une intégration facile dans un système d'informations géographiques.


![Données traitées](/img/5.PNG)

Les données sont maintenant organisées et prêtes à être visualisées.

Cette structure permet d’intégrer facilement des statistiques descriptives, selon les besoins,

qui pourront plus facilement être cartographiées. La structure actuelle est idéale pour

produire des histogrammes pour visualiser le compte mensuel de vélos à chacune des

stations.


**Production des histogrammes**

La bibliothèque Matplotlib pour Python oﬀre un puissant outil pour produire des

histogrammes. En utilisant cette fonctionnalité, il est possible de visualiser rapidement le

nombre de cyclistes comptés par mois à chaque station de comptage. Cela permet de

mieux comprendre les tendances de circulation et de prendre des décisions éclairées en

matière de planiﬁcation des infrastructures cyclables.


![Données traitées](/img/6.PNG)

Les histogrammes sont automatiquement produits seulement pour les mois

durant lesquels la station était en opération

Pour la période de 2013 à 2022, un total de 63 histogrammes sont produits. Une telle

visualisation des données nous permet rapidement de constater la variabilité saisonnière

du nombre de passage de cyclistes


![Données traitées](/img/7.PNG)


Les histogrammes produits ont tous un style commun

**Conclusion**

En conclusion, il est clair que l'automatisation de la préparation de données est un élément

clé pour améliorer l'eﬃcacité d’organisations qui utilisent de grands jeux de données pour

guider la prise de décision. Le projet présenté dans ce rapport démontre comment

l'utilisation de technologies avancées peut faciliter la collecte et l'analyse de données,

permettant ainsi une meilleure prise de décision. Les images incluses dans ce rapport

illustrent les résultats obtenus grâce à cette automatisation, et il est évident que les

organisations qui intègrent de telles méthodes dans leur fonctionnement quotidien

bénéﬁcieront d'une amélioration signiﬁcative de leur performance. Il est donc fortement

recommandé aux employeurs de considérer ces résultats et d'envisager d'intégrer des

processus d'automatisation similaires dans leur propre organisation.



