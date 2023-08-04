import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Function to read data from a file and extract a specific column


def read_column(file_path, column_index):
    with open(file_path, 'r') as file:
        data = [float(line.split()[column_index - 1])
                for line in file.readlines()]
    return np.array(data)


# Replace file paths with your actual data files
rmsd_file = 'rmsd.dat'
rg_file = 'RoG.dat'

# Read specific columns from each file
rmsd_data = read_column(rmsd_file, column_index=2)
rg_data = read_column(rg_file, column_index=2)

# Create a density map contour plot
plt.figure(figsize=(10, 6))
sns.kdeplot(x=rg_data, y=rmsd_data, cmap='magma_r',
            fill=True, levels=100, thresh=0.05)

# Customize plot labels and title
plt.xlabel("Rg (Å)")
plt.ylabel("RMSD (Å)")
plt.title("RMSD vs RoG")

plt.tight_layout()
plt.show()
