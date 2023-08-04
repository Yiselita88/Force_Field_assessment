import numpy as np

# Replace 'data_file.txt' with the path to your actual data file
data_file = 'dssp.dat.sum'

# Read the data from the file, ignoring the first row
data = np.loadtxt(data_file, usecols=(3, 4), skiprows=1)

# Extract columns 4 and 5
column4 = data[:, 0]
column5 = data[:, 1]

# Save columns 4 and 5 as a new CSV file
output_file = 'extracted_columns.csv'
np.savetxt(output_file, np.column_stack((column4, column5)), delimiter=',', header='Column 4,Column 5', comments='')

print(f"Columns 4 and 5 extracted and saved to '{output_file}'.")
