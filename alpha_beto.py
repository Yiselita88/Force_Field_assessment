import numpy as np
import matplotlib.pyplot as plt

# Replace 'data_file.txt' with the path to your actual data file
data_file = 'dssp.dat.sum'

# Read the data from the file, ignoring the first row
data = np.loadtxt(data_file, usecols=(1, 2, 4), skiprows=1)

# Sum 0.01 to each value in column 4 and column 5
column1_plus_0_01 = data[:, 0] + data[:, 1] + 0.01
column4_plus_0_01 = data[:, 2] + 0.01

# Calculate the logarithm of the division of (column4 + 0.01) by (column5 + 0.01)
log_division = np.log(column4_plus_0_01 / column1_plus_0_01)

# Create an array for the row numbers (from 1 to 16)
row_numbers = np.arange(1, len(data) + 1)

# Create a scatter plot
plt.figure(figsize=(8, 4))

# Plot the logarithm of the division against the row numbers
plt.scatter(row_numbers, log_division, color='blue', marker='o', s=100)

# Set the labels for the plot
plt.xlabel('Row Number')
plt.ylabel('Logarithm of Division')

# Add a solid line at y=0 parallel to the x-axis
plt.axhline(0, color='black', linestyle='-', linewidth=1.5)


# Show the plot
plt.tight_layout()
plt.show()
