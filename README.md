# M-KIS url_shortener
Ce projet est un outil de raccourcissement d'URL avec une interface web, utilisant le service Bitly via le module pyshorteners.

Fonctionnalités
Raccourcir des URL via Bitly
Gérer les exceptions pour des URL invalides ou des problèmes de réseau
Interface utilisateur web simple
Charte graphique spécifique (voir static/styles.css pour les détails)
Installation
Pour utiliser cet outil, vous devez d'abord installer les dépendances pyshorteners et flask. Vous pouvez les installer avec pip :

```pip install pyshorteners flask```
Ensuite, clonez ce dépôt sur votre machine locale :

```git clone https://github.com//m-kis/url_shortener.git```

Utilisation
Pour utiliser cet outil, naviguez dans le répertoire du projet et exécutez le script Python :

```cd url-shortener```
```python app.py```

Cela lancera le serveur Flask sur votre machine locale. Vous pouvez accéder à l'interface utilisateur web en naviguant vers http://localhost:5000 dans votre navigateur.

API Key
N'oubliez pas de remplacer "YOUR_KEY" par votre propre clé API de Bitly dans le script app.py.

Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus d'informations.
