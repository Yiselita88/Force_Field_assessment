import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Function to read data from a file and extract specific columns


def read_columns(file_path, column1_index, column2_index):
    with open(file_path, 'r') as file:
        data = np.loadtxt(file_path)
    column1_data = data[:, column1_index - 1]
    column2_data = data[:, column2_index - 1]
    return column1_data, column2_data


# Replace the file path with the actual path to your 'rmsf.dat' file
file_path = 'rmsf.dat'

# Read data from columns 1 and 2 in the file
residue_numbers, rms_fluctuations = read_columns(
    file_path, column1_index=1, column2_index=2)

# Interpolate the data for a smooth line plot
interpolation_function = interp1d(
    residue_numbers, rms_fluctuations, kind='cubic')
smooth_residue_numbers = np.linspace(
    min(residue_numbers), max(residue_numbers), num=1000)
smooth_rms_fluctuations = interpolation_function(smooth_residue_numbers)

# Create a line plot with a smooth curve
plt.figure(figsize=(10, 6))
plt.plot(smooth_residue_numbers, smooth_rms_fluctuations,
         color='blue', linewidth=2.0, label='ff14IDPs')
plt.scatter(residue_numbers, rms_fluctuations,
            color='red', s=10)
plt.xlabel("Residue Number")
plt.ylabel("RMS Fluctuations (Å)")
plt.title("Smooth Line Plot of RMS Fluctuations vs. Residue Number")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
