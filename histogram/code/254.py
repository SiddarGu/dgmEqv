import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Define the labels and the data
data_labels = ['Vaccination Rate (%)']
line_labels = [
    '95-100', '90-95', '85-90', '80-85', 
    '75-80', '70-75', '65-70', '60-65', '55-60'
]
data = [5.2, 10.4, 15.6, 20.5, 30.1, 22.3, 18.7, 14.2, 9.5]

# Transform data into a DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Create the plot
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))
ax = plt.subplot()

# Plot the histogram
ax = sns.barplot(x=df.index, y=df[data_labels[0]], palette="viridis")

# Set properties and layout
ax.set_title('Percentage of Vaccination Rates Across Different Population Slices')
ax.set_xlabel('Population Group (Millions)')
ax.set_ylabel('Vaccination Rate (%)')
plt.xticks(rotation=45, ha="right", rotation_mode="anchor")
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/604.png'
plt.savefig(save_path)

# Clear the current image state
plt.clf()
