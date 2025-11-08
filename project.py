import matplotlib.pyplot as plt
import numpy as np

# Données de la cellule PV
V = np.array([0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30])
I = np.array([5.0, 4.8, 4.5, 4.0, 3.5, 2.5, 0.0])

# Création du graphique
plt.figure(figsize=(8,6))
plt.plot(V, I, 'b-o', linewidth=2, markersize=6)
plt.xlabel('Tension (V)')
plt.ylabel('Courant (A)')
plt.title('Caractéristique I-V')
plt.grid(True, alpha=0.3)
plt.xlim(0, 0.35)
plt.ylim(0, 5.5)

# Affichage
plt.show()