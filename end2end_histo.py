import numpy as np
import matplotlib.pyplot as plt

# Function to read data from a file and extract specific columns


def read_columns(file_path, column_indices):
    with open(file_path, 'r') as file:
        data = [line.split() for line in file.readlines()]
    columns = [[] for _ in range(len(column_indices))]
    for row in data:
        for idx, col_idx in enumerate(column_indices):
            columns[idx].append(float(row[col_idx - 1]))
    return columns


# Replace the file path with your actual data file containing end-to-end distance
end_to_end_file = 'end2end.agr'

# Read the end-to-end distance data from the file
end_to_end_distances = read_columns(end_to_end_file, column_indices=[2])[0]

# Create a histogram of end-to-end distance populations
plt.figure(figsize=(8, 5))
plt.hist(end_to_end_distances, bins=20,
         color='blue', edgecolor='black', alpha=0.7)
plt.xlabel("End-to-End Distance (Å)")
plt.ylabel("Population")
plt.title("Histogram of End-to-End Distance Populations")
plt.grid(False)

plt.tight_layout()
plt.show()
