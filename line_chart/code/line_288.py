
import matplotlib.pyplot as plt
import numpy as np

# Set data
data = np.array([[50,60,100,80],
                [20,50,60,70],
                [60,80,90,100],
                [40,50,70,90],
                [10,20,50,60]])

# Set chart label
labels = ["North America","South America","Europe","Asia","Africa"]

# Set legend
legend_labels = ["Opera","Theater","Museum","Gallery"]

# Create figure
fig = plt.figure(figsize=(8,6))

# Set x-axis
x = np.arange(len(labels))

# Plot data
for i in range(len(legend_labels)):
    plt.plot(x, data[:,i], label=legend_labels[i])

# Add x-axis label
plt.xticks(x, labels, rotation=45, wrap=True)

# Set title
plt.title("Arts and culture attendance in four regions worldwide")

# Add legend
plt.legend(loc="best", bbox_to_anchor=(1.0,1.0))

# Adjust figure to avoid overlapping
plt.tight_layout()

# Save figure
plt.savefig("line chart/png/451.png")

# Clear the current image state
plt.clf()