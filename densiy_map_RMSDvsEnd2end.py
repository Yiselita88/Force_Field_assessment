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
termini_file = 'end2end_sieved.dat'

# Read specific columns from each file
rmsd_data = read_column(rmsd_file, column_index=2)
termini_data = read_column(termini_file, column_index=2)

# Create a density map contour plot
plt.figure(figsize=(10, 6))
sns.kdeplot(x=termini_data, y=rmsd_data, cmap='coolwarm',
            fill=True, levels=100, thresh=0.05)

# Customize plot labels and title
plt.xlabel("End 2 end distance (Å)")
plt.ylabel("RMSD (Å)")
plt.title("Density Map of RMSD vs end 2 end distance")

plt.tight_layout()
plt.show()
