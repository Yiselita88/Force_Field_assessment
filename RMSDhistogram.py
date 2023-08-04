import numpy as np
import matplotlib.pyplot as plt

# Function to read data from a file and extract a specific column


def read_column(file_path, column_index):
    with open(file_path, 'r') as file:
        data = [float(line.split()[column_index - 1])
                for line in file.readlines()]
    return np.array(data)


# Replace the file path with your actual data file for RMSD
rmsd_file = 'rmsd_2first.dat'

# Read the RMSD data from the file
rmsd_data = read_column(rmsd_file, column_index=2)

# Create a histogram of RMSD populations
plt.figure(figsize=(8, 5))
n, bins, patches = plt.hist(
    rmsd_data, bins=20, color='orange', edgecolor='black', alpha=0.7)

# Calculate the percentage of frames in each bin
total_frames = len(rmsd_data)
percentages = (n / total_frames) * 100

# Set the y-axis to show the percentage of frames
plt.gca().set_yticklabels(['{:.1f}%'.format(x)
                           for x in plt.gca().get_yticks()])

plt.xlabel("RMSD (Å)")
plt.ylabel("Percentage of Frames")
plt.title("Histogram of RMSD Populations")
plt.grid(False)

plt.tight_layout()
plt.show()
