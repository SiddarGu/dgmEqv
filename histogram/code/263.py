import pandas as pd
import matplotlib.pyplot as plt

# Given data
data = {
    'Revenue Growth (%)': ['1-5', '5-10', '10-15', '15-20', '20-25', '25-30', '30-35', '35-40', '40-45', '45-50'],
    'Number of Firms': [12, 18, 30, 20, 15, 9, 5, 2, 1, 1]
}

# Transforming the data into required variables
data_labels = ['Number of Firms']
line_labels = data.pop('Revenue Growth (%)')
df = pd.DataFrame(data, index=line_labels)

# Create a figure before plotting
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Visualize as a horizontal histogram using pandas
df.plot(kind='barh', ax=ax, color="skyblue", edgecolor="black", legend=False)  # Here pandas uses matplotlib under the hood

# Add grid, title and format xticks if needed
ax.grid(axis='x', which='both', linestyle='--', linewidth=0.5)
ax.set_title('Revenue Growth Percentages of Firms in the Financial Year')
ax.set_xlabel('Number of Firms')

# Set xticks rotation to prevent overlapping
plt.xticks(rotation=45)
plt.yticks(wrap=True)

# Automatically adjust subplot params to give specified padding, to prevent content from being cut off
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/613.png')

# Clear the current figure state
plt.clf()
