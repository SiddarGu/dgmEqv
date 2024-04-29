import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

# Create the data variables
data_labels = ["Monthly Sales ($ million)"]
line_labels = ["Electronics", "Apparel", "Home & Furniture", "Health & Personal Care", "Groceries",
               "Sports & Outdoors", "Toys & Games", "Books & Media"]
data = [145.5, 200.3, 135.4, 165.2, 190.1, 155.7, 120.6, 87.9]

# Transform data into a DataFrame
df = pd.DataFrame(data=np.array(data).reshape(-1, 1), index=line_labels, columns=data_labels)

# Create the figure and axis for the histogram
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Plotting the data using seaborn
sns.barplot(x=data_labels[0], y=df.index, data=df, orient="h", palette="viridis", ax=ax)

# Setting title, labels, and grid
ax.set_title('Monthly Sales Distribution Across Various E-commerce Categories', fontsize=16)
ax.set_xlabel(data_labels[0], fontsize=13)
ax.set_ylabel("Category", fontsize=13)

# Customize ticks and labels for better visualization
plt.xticks(fontsize=12)
plt.yticks(fontsize=12, rotation=0, wrap=True)

# Adding background grids
plt.grid(True, axis='x', linestyle='--', alpha=0.7)

# Automatically adjust subplot params for the figure to fit into the image
plt.tight_layout()

# Save the figure
save_path = "/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/83.png"
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path)

# Clear the current figure to free memory after saving the image
plt.clf()
