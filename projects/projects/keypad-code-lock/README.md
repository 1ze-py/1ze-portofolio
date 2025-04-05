# 🔢 Digicode avec Clavier Matriciel sur Raspberry Pi

Un projet permettant de saisir un code secret à l'aide d'un clavier matriciel 3x4 connecté à un Raspberry Pi.

🔎 **Pourquoi ce projet ?**
Ce projet a été réalisé en suivant un [tutoriel](https://raspberrypi-tutorials.fr/connecter-un-clavier-raspberry-pi-code-lock/) pour comprendre comment interfacer un clavier matriciel avec le Raspberry Pi et gérer la saisie d'un code secret.

## 🛠️ Matériel Utilisé
- Raspberry Pi 
- Clavier matriciel 3x4
- Câbles de connexion 

## 🔌 Connexions
Les broches du clavier sont connectées aux GPIO du Raspberry Pi comme suit :

| Broche Clavier | GPIO Raspberry Pi | Numéro de Broche Physique |
|----------------|-------------------|---------------------------|
| Ligne 1        | GPIO 7            | Broche 26                 |
| Ligne 2        | GPIO 8            | Broche 24                 |
| Ligne 3        | GPIO 11           | Broche 23                 |
| Ligne 4        | GPIO 25           | Broche 22                 |
| Colonne 1      | GPIO 9            | Broche 21                 |
| Colonne 2      | GPIO 10           | Broche 19                 |
| Colonne 3      | GPIO 15           | Broche 10                 |

## 🚀 Utilisation
1. **Installation des dépendances** :
   Assurez-vous que la bibliothèque RPi.GPIO est installée :
   ```bash
   pip install RPi.GPIO
