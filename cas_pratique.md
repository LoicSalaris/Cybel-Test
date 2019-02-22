# 1 - Algos Python

Write a Python 3 function/script for the three following tasks, using only the language features and standard library. No third-party library.

1. A simple string quoting system is to replace each ' in a string by \' and each \ in a string by \\. Write a function that takes a string, quotes it in this way, and returns the result.
1. Write a function that takes two strings as arguments, and returns true if they are anagrams of each other, and false otherwise.
1. A palindrome is a string that is the same forwards and backwards, disregarding non-letters and case. Eg. « A man, a plan, a canal, Panama. » is a palindrome. Write a function that takes a string as input, and returns wether it's a palindrome

# 2 - Cas pratique : l'app d'alertes

## Enoncé

Une alerte est un objet que l'on peut simplifier de la manière suivante :

```json
{
    "id": "1234",
    "category": "dark web",
    "score": 78,
    "date": "2017/11/03 15:00:56 UTC",
    "status": "new",
    "client": "Johnny",
    "summary": "This is a summary of the alert's content"
}
```

En plus de ça (l'objet json) pour chaque alerte, il y a un fichier lui correspondant stocké dans le filesystem(?) avec le contenu complet d'origine.

On souhaite créer une application web pour gérer ces alertes.

1. Avec les possibilités de tri et filtres suivantes
  - sur `client` : pouvoir sélectionner plusieurs clients (par défaut, tous)
  - sur `status` : ne pouvoir sélectionner qu'un status (valeurs possibles : `["new", "investigating", "junk"]`, par défaut : "new")
  - sur `category` : pouvoir sélectionner plusieurs categories (valeurs possibles : `["dark web", "deep web", "connected devices"]`, par défaut : tous)
  - sur `score` : pouvoir trier par score (pourcentage entier)
  - sur `date` : pouvoir trier par date (par défaut)
  - sur `summary` : pouvoir rechercher un extrait dans le summary
2. Pour chaque alerte, on permet les actions suivantes
  - changer le `status` d'une alerte.
  - click sur une alerte pour afficher ses metadatas (L'affichage de base ne permettant pas de les voir, pour gagner de la place, de plus elles ne sont pas intéressantes pour toutes les alertes)
  - download du fichier de contenu.

## Question

1. Proposer une architecture web complète (infrastructure, endpoints, schémas des objets back/front, bases de données, ...)
1. Implémenter une version très simple de l'application qui ne fait qu'afficher la liste des alertes, en chargeant les données à l'aide d'une promesse.

### Architecture Web

## Infrastructure

* Front

  => React
  => Redux
  => Axios
  => Sass

* Back

  => Node.Js / Loopback CRUD sur tous les endpoints
  => Swagger (API REST)

* Base de donnée

  => MongoDb

* Outils

  => Gitlab
  => Chaine de CI (intégration continue) + Test
  => Eslint + Rules Airbnb

## API EndPoint

=> /v1/Alerts || GET POST PUT DELETE    *Endpoint qui expose la liste des alertes
=> /v1/Files || GET POST PUT DELETE     *Endpoint qui expose les fichiers correspondant au alertes

## Schema Objet

```
{
    "id": string,
    "category": string,
    "score": boolean,
    "date": date,
    "status": string,
    "client": string,
    "summary": string
}
```