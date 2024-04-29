import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Data extraction
data_labels = ['Yield (million metric tons)']
line_labels = ['Cereals', 'Legumes', 'Tubers', 'Fruits', 'Vegetables', 'Oilseeds', 'Sugarcane', 'Fiber Crops']
data = [1025.3, 156.7, 785.1, 731.0, 950.5, 540.2, 1897.3, 123.8]

# Create a DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Create a figure and a single subplot
plt.figure(figsize=(12, 8))
ax = plt.subplot(111)

# Plot histogram
sns.barplot(x=df.index, y=df[data_labels[0]], palette="viridis", ax=ax)
ax.set_title('Global Agricultural Yield by Crop Type', fontsize=16)
ax.set_ylabel(data_labels[0], fontsize=12)
ax.set_xlabel('Crop Type', fontsize=12)
plt.xticks(rotation=45, ha='right', wrap=True)

# Style
sns.set_style("whitegrid")

# Adjust layout
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/635.png'
if not os.path.exists(os.path.dirname(save_path)):
    os.makedirs(os.path.dirname(save_path))
plt.savefig(save_path)

# Clear the current figure
plt.clf()
