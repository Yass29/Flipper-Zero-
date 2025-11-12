# 02. Sub-GHz Rolling Code Brute Force PoC 📡

## 🎯 Aperçu du Projet : Sensibilisation aux Codes Roulants

Ce projet est une **Proof of Concept (PoC)** avancée visant à démontrer la vulnérabilité de certains systèmes d'accès utilisant des **codes roulants (Rolling Codes)** simples. Au lieu de se limiter au Rejeu (Replay Attack), nous utilisons un outil Python personnalisé pour automatiser une **attaque par force brute ciblée**.

L'objectif est de montrer qu'en capturant un seul code valide, il est possible de calculer une "fenêtre" de codes potentiellement acceptables par le récepteur, puis de les essayer en rafale.

| Outil | Rôle dans l'Attaque |
| :--- | :--- |
| **Python** | **Générateur de Payload.** Crée le fichier `.sub` contenant 1000 tentatives de code calculées. |
| **Flipper Zero** | **Transmetteur RF.** Exécute le fichier `.sub` et émet les 1000 tentatives radio successives. |

---

## ⚠️ Avertissement Éthique et Portée du Test

Ce PoC est réalisé sur des **systèmes de test autorisés** et vise à des fins de **sensibilisation et d'éducation en cybersécurité (Red Teaming)**.

* **Rappel :** Ce type d'attaque est généralement inefficace contre les systèmes modernes de voiture ou d'alarme qui utilisent un chiffrement robuste (ex: KeeLoq avancé). Ce PoC est efficace contre les implémentations plus anciennes ou les protocoles simples.
* **Rigueur Professionnelle :** N'utilisez ce code que sur des équipements vous appartenant ou avec une autorisation explicite.

---

## ⚙️ Méthodologie et Préparation

### 1. Reconnaissance et Capture

Utiliser le Flipper Zero pour capturer un signal de la télécommande de test afin d'obtenir les paramètres nécessaires pour le script Python.

| Paramètre | Source | Exemple (pour le script) |
| :--- | :--- | :--- |
| **Fréquence** | Flipper Sub-GHz Read | `315.000` MHz (Amérique du Nord) |
| **Longueur de bit** | Flipper Sub-GHz Read | `24` |
| **Code Capturé** | Flipper Sub-GHz Read (Data) | `0xAAFF10` |

### 2. Ingénierie du Payload (Script Python)

Le script **`generator_script.py`** calcule la plage de codes. Nous utilisons un code capturé (`0xAAFF10`) pour dériver un point de départ `BASE_CODE_START` et créer 1000 tentatives consécutives.

**Paramètres Critiques dans `generator_script.py` :**

```python
# FRÉQUENCE (Norme Am. du Nord)
frequency_mhz = 315.000 

# CODE DE DÉPART (Décalé de 1000 positions avant le code capturé 0xAAFF10)
# Remplacer cette valeur par une valeur proche du code capturé au début 
# de l'exercice pour déterminer la plage à attaquer.
BASE_CODE_START = 0xAAFB28 

# NOMBRE DE CODES À GÉNÉRER
NUMBER_OF_CODES = 1000