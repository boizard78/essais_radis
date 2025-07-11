"# essais_radis" 
from radis import calc_spectrum

# Calcul d'un spectre d'absorption à partir de HITRAN online
s = calc_spectrum(
    wavenum_min=2300,     # cm⁻¹
    wavenum_max=2400,     # plage spectrale
    molecule="CO2",       # molécule
    isotope="1",          # isotope (1 = principal)
    pressure=1.0,         # en atm
    Tgas=296.0,           # température en Kelvin
    mole_fraction=0.1,    # fraction molaire de CO2
    path_length=1.0,      # en cm
    databank="hitran",    # base de données
)

# Affichage du spectre
s.plot("abscoeff")   # ou "transmittance", "radiance" selon ce que tu veux
