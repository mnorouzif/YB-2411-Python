# import seaborn as sns
# import matplotlib.pyplot as plt
# import numpy as np

# # Example confusion matrix
# conf_matrix = np.array([[64, 1],
#                         [10, 32]])

# # Normalize by total predictions
# total = np.sum(conf_matrix)
# percent_matrix = conf_matrix

# # Plot heatmap
# sns.heatmap(percent_matrix, annot=True, fmt=".1f", cmap="Blues", cbar=True)
# plt.xlabel("Predicted Label")
# plt.ylabel("Actual Label")
# plt.title("Confusion Matrix (% of Total Predictions)")
# plt.show()

import csv
import os

# Define the RGB colormap list
colormap = [
  [0, 0, 128], [4, 4, 132], [8, 8, 136], [12, 12, 140], [16, 16, 144], [20, 20, 148], [24, 24, 152], [28, 28, 156],
  [32, 32, 160], [36, 36, 164], [40, 40, 168], [44, 44, 172], [48, 48, 176], [52, 52, 180], [56, 56, 184], [60, 60, 188],
  [64, 64, 192], [68, 68, 196], [72, 72, 200], [76, 76, 204], [80, 80, 208], [84, 84, 212], [88, 88, 216], [92, 92, 220],
  [96, 96, 224], [100, 100, 228], [104, 104, 232], [108, 108, 236], [112, 112, 240], [116, 116, 244], [120, 120, 248], [124, 124, 252],
  [128, 128, 255], [132, 132, 255], [136, 136, 255], [140, 140, 255], [144, 144, 255], [148, 148, 255], [152, 152, 255], [156, 156, 255],
  [160, 160, 255], [164, 164, 255], [168, 168, 255], [172, 172, 255], [176, 176, 255], [180, 180, 255], [184, 184, 255], [188, 188, 255],
  [192, 192, 255], [196, 196, 255], [200, 200, 255], [204, 204, 255], [208, 208, 255], [212, 212, 255], [216, 216, 255], [220, 220, 255],
  [224, 224, 255], [228, 228, 255], [232, 232, 255], [236, 236, 255], [240, 240, 255], [244, 244, 255], [248, 248, 255], [255, 255, 255]
]

# Sort by brightness (sum of RGB values)
sorted_colormap = sorted(colormap, key=lambda rgb: sum(rgb))

# Define output path
output_path = "./sorted_colormap.csv"

# Ensure directory exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Write to CSV
with open(output_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["R", "G", "B"])
    writer.writerows(sorted_colormap)

print(f"CSV file saved to {output_path}")
