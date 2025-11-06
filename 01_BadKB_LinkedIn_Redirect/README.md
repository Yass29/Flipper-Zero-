## 01. Redirection LinkedIn BadKB (Payload_BadKB_LinkedIn_Redirect)

### ⚠️ Avertissement et Sensibilisation (Red Teaming) ⚠️

Ce script est un PoC qui met en lumière la menace que représentent les périphériques USB non vérifiés. Il redirige un utilisateur vers un site légitime (LinkedIn) mais montre clairement comment le point de contrôle de l'URL peut être détourné vers :
* Un site de **Phishing** (vol d'identifiants).
* Un site d'hébergement de **Malware** (téléchargement d'un virus).

**Utilisez ce code uniquement pour des tests de sécurité autorisés.**

### Détails du Code
* **Fichier :** `01_BadKB_LinkedIn_Redirect/Payload_BadKB_LinkedIn_Redirect.txt`
* **Cible :** macOS (clavier Anglais QWERTY)
* **Fonction :** Utilise `GUI SPACE` (Cmd + Espace) puis `GUI l` (Cmd + L) pour naviguer vers l'URL.

**[👉 Voir le code et la documentation détaillée du projet 01](01_BadKB_LinkedIn_Redirect/README.md)**

---

## 🔑 Installation et Prérequis

* **Appareil :** Flipper Zero.
* **Firmware :** Firmware officiel ou custom (Xtreme, Unleashed, etc.).
* **Disposition Clavier :** Assurez-vous que la disposition de votre machine cible correspond à celle du payload.