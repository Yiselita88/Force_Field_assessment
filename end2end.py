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

# Read the time (frames) and end-to-end distance data from the file
time_frames, end_to_end_distances = read_columns(
    end_to_end_file, column_indices=[1, 2])

# Divide the time (frames) by 50,000 to get the x-axis in suitable units
time_in_ps = np.array(time_frames) / 50000.0

# Create a plot of end-to-end distance versus time
plt.figure(figsize=(10, 6))
plt.plot(time_in_ps, end_to_end_distances,
         color='blue', linestyle='-', linewidth=1)
plt.xlabel("Time (μs)")
plt.ylabel("End-to-End Distance (Å)")
plt.title("End-to-End Distance of Peptide vs Time")
plt.grid(False)

plt.tight_layout()
plt.show()
