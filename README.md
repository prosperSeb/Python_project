# Python_project
## Dataset et réflexion
YearPredictionMSD est un dataset comportant la description de 515345 musiques en 91 varaible différentes. On divise 3 type de variables :
  - l'anné de sortie de la musique
  - 12 Timbre moyen 
  - 78 covariance de Timbre 

Le but de ce dataset est d'être utilisé pour prédire l'année de sorite d'une musique en fonction de ses 90 caractéristiques.Le dataset comporte des musiques sorties entre 1922 et 2011. Cette plage étant importante et afin d'obtenir des résultats plus concluants nous avons décidé de diviser cette plage en intervalles.
```sh
1: "1922 1983",
2: "1983 1992",
3: "1992 1996",
4: "1996 1999",
5: "1999 2002",
6: "2002 2004",
7: "2004 2005",
8: "2005 2007",
9: "2007 2008",
10: "2008 2011"
```

Vous trouverez dans le fichier code_python.ypnb l'ensemble de la data visualisation ainsi que de la modélisation.

## API django
L'api possède trois urls afin d'y faire des requêtes.
```sh
./songs/$
```
Permets d'afficher l'ensemble des musiques dans la bdd à l'aide d'une requête GETAvec une requête POST on pourra enregistrer une musique sans prédire l'intervalle de sortie.

```sh
./songs/pk/$
```
Permets des selectionner/supprimer/modifier une musique en fonction de son index à l'aide des requêtes respective GET/DELETE/PUT.

```sh
./predict/$
```
Permets d'ajouter une musique à la bdd tout en prédisant l'intervalle de sortie de cette musique à l'aide d'une requête POST.

L'ensemble du code ainsi que des exemples d'utilisation est disponibles dans la présentation.
