import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import subprocess

def git_commit(message, chemin_repo):
    """
    Effectue un commit avec un message donné dans un dépôt Git.

    Args:
        message (str): Le message de commit.
        chemin_repo (str): Le chemin local du dépôt Git.
    """
    try:
        subprocess.run(["git", "add", "."], cwd=chemin_repo, check=True)
        subprocess.run(["git", "commit", "-m", message], cwd=chemin_repo, check=True)
        print(f"Commit effectué avec le message : {message}")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'ajout et du commit : {e}")

def create_arborescence(arborescence, chemin_repo):
    """
    Crée une arborescence de fichiers et de dossiers dans le dépôt Git.

    Args:
        arborescence (dict): Une structure d'arborescence spécifiée comme un dictionnaire.
        chemin_repo (str): Le chemin local du dépôt Git.
    """
    
    def parcourir_arborescence(arbo, chemin_actuel):
        for element, contenu in arbo.items():
            chemin_element = os.path.join(chemin_actuel, element)

            if isinstance(contenu, dict): 
                os.makedirs(chemin_element, exist_ok=True)
                parcourir_arborescence(contenu, chemin_element)
            elif contenu:  
                os.makedirs(os.path.dirname(chemin_element), exist_ok=True)
                with open(chemin_element, "w") as fichier:
                    fichier.write(contenu)

    # Création arborescence locale
    parcourir_arborescence(arborescence, chemin_repo)


if __name__ == '__main__' :
#arborescence
    arborescence = {
        "data": {
            "cleaned": {},
            "processed": {},
            "raw": {}
            
        },
        "docs": {},
        "LICENCE" : "",
        "Makefile": "",
        "github":{
            "workflows":{
                "build.yaml" : '''name: Auto Data Process

on:
  push:
    branches:
      - main

jobs:
  process_data:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9

    - name: Install dependencies
      run: pip install -r requirements.txt

    - name: Run data process script
      run: python main.py
'''
            }
        },
        "models": {},
        "notebooks": {
            "main.py": '''import pandas as pd

def load(path) :

    data = pd.read_csv(path)
    print(data.info())
    print('Street',data['Street'].unique())
    print('LotShape',data['LotShape'].unique())
    print('Alley',data['Alley'].unique())
    print('Foundation',data['Foundation'].unique())
    print('CentralAir',data['CentralAir'].unique())
    print('PoolArea',data['PoolArea'].unique())
    return data

def red(data) :
    x = data[['MSSubClass', 'LotArea', 'Street', 'LotShape', 'LandContour', 'HouseStyle', 'OverallQual', 'OverallCond', 'YearBuilt', 'Foundation', 'CentralAir', 'GrLivArea', 'BedroomAbvGr', 'KitchenAbvGr', 'TotRmsAbvGrd', 'GarageCars', 'PoolArea', 'YrSold']]
    return x

def clean(x) :
    street = {'Pave': 0,'Grvl': 1}
    x.Street = [street[item] for item in x.Street]

    lot = {'Reg' : 0, 'IR1' : 1, 'IR2' : 2, 'IR3' : 3}
    x.LotShape = [lot[item] for item in x.LotShape]

    land = {'Lvl' : 0, 'Bnk' : 1, 'Low' : 2, 'HLS' : 3}
    x.LandContour = [land[item] for item in x.LandContour]

    house = {'2Story' : 0, '1Story' : 1, '1.5Fin' : 2, '1.5Unf' : 3, 'SFoyer' : 4, 'SLvl' : 5, '2.5Unf' : 6, '2.5Fin' : 7}
    x.HouseStyle = [house[item] for item in x.HouseStyle]

    fond = {'PConc' : 0, 'CBlock' : 1, 'BrkTil' : 2, 'Wood' : 3, 'Slab' : 4, 'Stone' : 5}
    x.Foundation = [fond[item] for item in x.Foundation]

    air = {'N': 0,'Y': 1}
    x.CentralAir = [air[item] for item in x.CentralAir]

    return x

def summary_stats(data):
    
    summary = data.describe()
    
    print("Statistiques sommaires des données :")
    return summary

if __name__ == '__main__' :

    data = load('train.csv')
    data_reduce = red(data)
    cleaned = clean(data)
    stats = summary_stats(cleaned)
    print(stats)
'''
        },
        "README.md": """Ce programme Python a pour objectif de créer une structure d'arborescence de fichiers et de dossiers spécifique dans un dépôt Git\nPour exécuter l'application, suivez ces étapes :
    1. [Étape 1 : Prérequis, par exemple, installer Python 3.7+]
    2. [Étape 2 : Cloner le dépôt Git : `git clone https://github.com/votre-utilisateur/mon-projet.git`]
    3. [Étape 3 : Naviguer vers le répertoire du projet : `cd mon-projet`]
    4. [Étape 4 : Installer les dépendances : `pip install -r requirements.txt`]
    5. [Étape 5 : Lancer l'application : `python main.py`]
    """,
        "reports": {},
        "requirements.txt": "os\nsubprocess\nnumpy\npandas",
        "src": {
            "utils.py": "",
            "process.py": "",
            "train.py": ""
        }
    }

    chemin_repo_git = r"C:\Users\baaymatar\Desktop\COURS\examVers_DIT"
    subprocess.run(["git", "init"], cwd=chemin_repo_git, check=True)

    create_arborescence(arborescence, chemin_repo_git)

    git_commit("Création de l'arborescence", chemin_repo_git)

    subprocess.run(["git", "init"], cwd=chemin_repo_git, check=True)



