# from radis import *

# s = calculated_spectrum(
#     molecule = "CO2",
#     # isotope = 
#     wavenum_min = 2300,
#     wavenum_max = 2400,
#     step = 0.1,
#     pression = 1,
#     temperature = 453.15,
#     Fraction_molaire = 0.001,
#     L_optique = 50,
#     data_base = "hitran"
# )

# s.plot("abscoeff")



# from radis import calc_spectrum

# s = calc_spectrum(
#     molecule="CO2",
#     wavenum_min=2300,
#     wavenum_max=2400,
#     pressure=1,               # en atm
#     Tgas=453.15,              # température en Kelvin
#     mole_fraction=0.001,      # fraction molaire
#     path_length=50,           # en cm
#     databank="hitran"         # base de données
# )

# s.plot("abscoeff")


from radis import calc_spectrum
import pandas as pd
import numpy as np

# Calcul du spectre
s = calc_spectrum(
    molecule="CO2",
    wavenum_min=2300,
    wavenum_max=2400,
    pressure=1,
    Tgas=453.15,
    mole_fraction=0.001,
    path_length=50,
    databank="hitran"
)

# Rééchantillonnage avec un pas de 0.1 cm^-1
wavenumbers = np.arange(2300, 2400.1, 0.1)
s_resampled = s.resample(wavenum=wavenumbers)

# Extraction des données
df = pd.DataFrame({
    "Wavenumber (cm^-1)": s_resampled.get_grid(),
    "Absorption Coefficient": s_resampled.get("abscoeff")
})

# Sauvegarde dans un fichier Excel
df.to_excel("absorption_coefficients.xlsx", index=False)

print("Fichier 'absorption_coefficients.xlsx' sauvegardé avec succès.")

