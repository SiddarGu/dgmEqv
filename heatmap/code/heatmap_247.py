
# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define data as a dictionary
data = {'Product': ['Coca-Cola', 'PepsiCo', 'Nestle', 'Kraft Heinz', 'Unilever'],
        'Revenue (in millions)': [500, 400, 300, 200, 100],
        'Market Share (%)': [15, 10, 8, 5, 2],
        'Distribution (%)': [35, 30, 25, 20, 10],
        'Customer Satisfaction (%)': [85, 80, 75, 70, 65],
        'Advertising Cost (in millions)': [50, 45, 40, 35, 30]}

# Create a dataframe from the data
df = pd.DataFrame(data)

# Set the figure size
plt.figure(figsize=(10, 6))

# Plot the heatmap using seaborn
import seaborn as sns
ax = sns.heatmap(df.iloc[:, 1:], annot=True, fmt=".0f", cmap="YlGnBu")

# Set the tick labels and rotation for x and y axis
ax.set_xticklabels(df.columns[1:], rotation=45, ha="right", rotation_mode="anchor")
ax.set_yticklabels(df["Product"], rotation=0)

# Set the ticks to be in the center of each cell
ax.set_xticks(np.arange(0.5, len(df.columns)-1, 1))
ax.set_yticks(np.arange(0.5, len(df), 1))

# Set the title of the figure
plt.title("Key Metrics in Food and Beverage Industry")

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig("output/final/heatmap/png/20231228-155147_45.png", bbox_inches="tight")

# Clear the current image state
plt.clf()