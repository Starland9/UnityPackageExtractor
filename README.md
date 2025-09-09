# UnityPackageExtractor

Un outil graphique simple pour extraire le contenu des fichiers `.unitypackage`.

## Capture d'écran

![Capture d'écran de l'application](screenshot.png)

## Caractéristiques

- Interface graphique simple et intuitive.
- Sélection de plusieurs fichiers `.unitypackage` à extraire.
- Choix du répertoire de destination pour les fichiers extraits.
- Option pour supprimer les archives `.unitypackage` après l'extraction.
- Messages d'erreur en cas de problème.

## Installation

1.  Clonez le dépôt du projet. Si vous l'avez téléchargé autrement, passez à l'étape 2.

2.  Installez les dépendances en utilisant `pip` :
    ```bash
    pip install -r requirements.txt
    ```

## Utilisation

Pour lancer l'application, exécutez la commande suivante à la racine du projet :

```bash
python main.py
```

Ensuite, suivez les étapes dans l'application :
1.  Cliquez sur "Choisir un fichier" pour sélectionner un ou plusieurs fichiers `.unitypackage`.
2.  (Optionnel) Cliquez sur "Choisir la destination" pour choisir où extraire les fichiers (par défaut, ce sera dans un dossier `Extracteds`).
3.  Cliquez sur "Extraire".

## Dépendances

Ce projet utilise les bibliothèques Python suivantes :

-   [PyQt6](https://pypi.org/project/PyQt6/)
-   [unitypackage_extractor](https://pypi.org/project/unitypackage-extractor/)

Toutes les dépendances sont listées dans le fichier `requirements.txt`.

## Contribuer

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une *issue* ou à soumettre une *pull request*.

## Licence

Ce projet n'a pas de licence spécifiée. Il est recommandé d'en ajouter une, comme la licence MIT.
