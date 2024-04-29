import pandas as pd
import matplotlib.pyplot as plt
import os

# Data preparation
data_labels = ['Annual Budget Allocation ($ Billion)']
line_labels = ['Education', 'Healthcare', 'Defense', 'Welfare', 'Transportation', 'Environment', 'Science and Technology', 'Agriculture', 'Energy']
data = [58.7, 110.4, 601.2, 380.5, 87.3, 71.6, 29.4, 46.8, 64.9]

# Create a DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Create a figure and a subplot
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Plotting the data
df.plot(kind='bar', ax=ax, rot=0)

# Improve formatting and layout
plt.title('Annual Budget Allocation Across Various Public Policy Areas')
plt.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)
ax.tick_params(axis='x', labelrotation=45)
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/34.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path)

# Clear the current figure state to prevent interference with other plots
plt.clf()
