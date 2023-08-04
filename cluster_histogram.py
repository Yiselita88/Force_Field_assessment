import numpy as np
import matplotlib.pyplot as plt

# Function to read data from a file and extract a specific column


def read_column(file_path, column_index):
    with open(file_path, 'r') as file:
        data = [line.split()[column_index - 1] for line in file.readlines()]
    return np.array(data)


# Replace the file path with the actual path to your 'frame_vs_cluster.txt' file
file_path = 'frame_vs_cluster.txt'

# Read the frame numbers and cluster information from the file
frame_numbers = read_column(file_path, column_index=1)
cluster_numbers = read_column(file_path, column_index=2)

# Convert the cluster numbers to integers
cluster_numbers = np.array(cluster_numbers, dtype=int)

# Count the number of frames in each cluster using a dictionary
cluster_counts = {}
for cluster in cluster_numbers:
    cluster_counts[cluster] = cluster_counts.get(cluster, 0) + 1

# Extract cluster numbers and frame counts for plotting
clusters, frame_counts = zip(*cluster_counts.items())

# Create a histogram of frame counts per cluster
plt.figure(figsize=(8, 5))
plt.bar(clusters, frame_counts, color='orange', edgecolor='black', alpha=0.7)
plt.xlabel("Cluster")
plt.ylabel("Number of Frames")
plt.title("Histogram of Frames per Cluster")
plt.grid(False)

plt.tight_layout()
plt.show()
