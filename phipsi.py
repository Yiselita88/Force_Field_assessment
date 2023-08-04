import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Replace 'dihedrals_data.txt' with the path to your actual data file
data_file = 'phipsi.dat'

# Read the data from the text file, skipping column 5
data = np.loadtxt(data_file, usecols=(0, 1, 2, 3))

# Get the phi and psi values for all residues
phi_values = data[:, 0]
psi_values = data[:, 1]

# Create a Ramachandran plot with density contours
plt.figure(figsize=(12, 12))
sns.kdeplot(x=phi_values, y=psi_values, cmap='YlOrRd', fill=True, levels=20)

# Use Greek letters for the x-axis and y-axis labels
plt.xlabel('φ (Phi) Angle (degrees)')
plt.ylabel('ψ (Psi) Angle (degrees)')
plt.title('Ramachandran Plot with Density Contours')
plt.grid(True)

# Set x-axis and y-axis limits as desired
# Show more of the psi angle from -180 to 0
plt.xlim(-120, -40)
# Reduce the view of 0 to 180 for phi angle
plt.ylim(-180, 180)

# Create a solid line passing through 0 angles
plt.axvline(x=0, color='black', linestyle='-', linewidth=1)
plt.axhline(y=0, color='black', linestyle='-', linewidth=1)

# Create a scatter plot of psi vs. phi dihedrals and overlay on the Ramachandran plot
plt.scatter(phi_values, psi_values, s=10, c='blue', alpha=0.7)

# Enumerate and annotate residues near data points with an offset
offset = 5  # Adjust this value to set the distance of the annotations from the data points
for i, (phi, psi) in enumerate(zip(phi_values, psi_values)):
    residue_number = i + 1
    plt.annotate(residue_number, (phi, psi), textcoords="offset points",
                 xytext=(np.random.randint(-offset, offset),
                         np.random.randint(2, 2 * offset)),
                 ha='center')

plt.tight_layout()
plt.show()
