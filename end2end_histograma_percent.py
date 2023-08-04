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

# Function to create a histogram with percentage values


def create_percentage_histogram(data, bins, title, x_label, y_label):
    total_population = len(data)
    bin_counts, bin_edges = np.histogram(data, bins=bins)
    bin_widths = np.diff(bin_edges)
    bin_percentages = (bin_counts / total_population) * 100

    sorted_bins = sorted(
        zip(bin_edges[:-1], bin_percentages), key=lambda x: x[1], reverse=True)
    top_5_bins = sorted_bins[:5]
    top_5_sum = sum(percentage for _, percentage in top_5_bins)

    plt.bar(bin_edges[:-1], bin_percentages, width=bin_widths,
            align='edge', color='blue', alpha=0.7)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(False)

    for i, (edge, percentage) in enumerate(top_5_bins):
        plt.text(edge + 0.5 * bin_widths[0], percentage,
                 f"{percentage:.2f}%", ha='center', va='bottom')

    plt.text(0.5, 95, f"Sum of Top 5: {top_5_sum:.2f}%",
             ha='left', va='bottom', fontsize=12)

    plt.tight_layout()
    plt.show()


# Replace the file path with your actual data file containing end-to-end distance
end_to_end_file = 'end2end.agr'

# Read the end-to-end distance data from the file
end_to_end_distances = read_columns(end_to_end_file, column_indices=[2])[0]

# Create a histogram of end-to-end distance populations
plt.figure(figsize=(8, 5))
create_percentage_histogram(end_to_end_distances, bins=20,
                            title="Histogram of End-to-End Distance Populations",
                            x_label="End-to-End Distance (Å)",
                            y_label="Percentage")
