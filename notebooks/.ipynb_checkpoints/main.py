# import pandas as pd
 
# # Remplace par le chemin réel de ton fichier Excel

# fichier_excel = "Combinaisons_Spectrapot_Radis_1.xlsm"
 
# # # Lire la première feuille du fichier Excel

# df = pd.read_excel(fichier_excel)
 
# # # Affiche les premières lignes pour voir ce que contient le fichier

# # print("Aperçu des données :")

# print(df)
 

from hapi import *
import matplotlib.pyplot as plt
from hapi import *

# 1. Initialiser la base de données locale
db_begin('data')

# 2. Télécharger les données HITRAN pour le CO2 (ID HITRAN = 2)
#    Plage spectrale : 600 à 800 cm⁻¹
fetch('CO2', 2, 600.0, 800.0)

# 3. Définir les conditions expérimentales
T = 296.0         # Température en Kelvin
P = 1.0           # Pression en atm
L = 10.0          # Longueur optique en cm
x_CO2 = 0.01      # Fraction molaire de CO2

# 4. Calculer le coefficient d'absorption
nu, coef = absorptionCoefficient_Voigt(
    SourceTables='CO2',
    Environment={'T': T, 'p': P},
    WavenumberStep=0.01,
    HITRAN_units=True
)

# 5. Calculer l'absorbance
nu, absorbance = absorbanceSpectrum(
    nu, coef,
    Environment={'l': L, 'T': T, 'p': P, 'x_CO2': x_CO2}
)

# 6. Tracer le spectre
plt.figure(figsize=(10, 5))
plt.plot(nu, absorbance, label='Absorbance CO₂')
plt.xlabel('Nombre d\'onde (cm⁻¹)')
plt.ylabel('Absorbance')
plt.title('Spectre d\'absorption du CO₂')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
