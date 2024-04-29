import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Given Data
data_labels = ["Average Lifespan (Years)", "Number of Countries"]
line_labels = ["40-50", "50-60", "60-70", "70-80", "80-90", "90-100"]
data = [2, 5, 20, 30, 25, 10]

# Create a DataFrame
df = pd.DataFrame(data, index=line_labels, columns=[data_labels[1]])

# Plotting
plt.figure(figsize=(10, 8))
ax = plt.subplot()
sns.barplot(x=data_labels[1], y=df.index, data=df, orient='h', palette='viridis')
ax.set_title('Global Distribution of Average National Lifespan')
ax.set_xlabel(data_labels[0])
ax.set_ylabel('')
ax.grid(True)

# Adjust layout to prevent content from being cut off
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/78.png'
plt.savefig(save_path, format='png')

# Clear the current image state
plt.clf()
