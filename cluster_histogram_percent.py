import numpy as np
import matplotlib.pyplot as plt

# Function to read data from a file and extract a specific column


def read_column(file_path, column_index, skip_rows=0):
    with open(file_path, 'r') as file:
        lines = file.readlines()[skip_rows:]
        data = [line.split()[column_index - 1] for line in lines]
    return np.array(data)


# Replace the file path with the actual path to your 'frame_vs_cluster.txt' file
file_path = 'frame_vs_cluster.txt'

# Read the frame numbers and cluster information from the file (skip the first row)
frame_numbers = read_column(file_path, column_index=1, skip_rows=1)
cluster_numbers = read_column(file_path, column_index=2, skip_rows=1)

# Convert the cluster numbers to integers
cluster_numbers = np.array(cluster_numbers, dtype=int)

# Count the number of frames in each cluster using a dictionary
total_frames = len(frame_numbers)
cluster_counts = {}
for cluster in cluster_numbers:
    cluster_counts[cluster] = cluster_counts.get(cluster, 0) + 1

# Calculate the percentage of frames in each cluster
cluster_percentages = {cluster: (
    count / total_frames) * 100 for cluster, count in cluster_counts.items()}

# Extract cluster numbers and frame percentages for plotting
clusters, frame_percentages = zip(*cluster_percentages.items())

# Create a histogram of frame percentages per cluster
plt.figure(figsize=(8, 5))
plt.bar(clusters, frame_percentages, color='orange',
        edgecolor='black', alpha=0.7)
plt.xlabel("Cluster")
plt.ylabel("Percentage of Frames")
plt.title("Histogram of Frame Percentage per Cluster")
plt.grid(False)

# Calculate the cumulative percentage
cumulative_percentages = np.cumsum(frame_percentages)

# Find the index where the cumulative percentage becomes higher than 50%
index_50_percent = np.argmax(cumulative_percentages > 50)

# Add a vertical line at the boundary between bin 5 and bin 6
plt.axvline(x=5.5, color='red', linestyle='--')

plt.annotate('50% threshold', xy=(5.5, 50),
             xytext=(5.5 + 0.5, 60),
             arrowprops=dict(arrowstyle='->', color='red'))

plt.tight_layout()
plt.show()
