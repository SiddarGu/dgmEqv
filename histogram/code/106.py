import pandas as pd
import matplotlib.pyplot as plt

# Data provided
data = {
    'Art Form': ['Museums', 'Theaters', 'Concert Halls', 'Art Galleries', 'Festivals', 'Cultural Centers'],
    'Monthly Visitors (Thousands)': [150, 120, 95, 110, 135, 85]
}

# Creating DataFrame from the data
df = pd.DataFrame(data)

# Creating labels for columns and rows
data_labels = df.columns.tolist()[1:]  # Column labels without the first column
line_labels = df['Art Form']           # Row labels from the first column

# Creating the histogram
plt.figure(figsize=(10, 8))
ax = plt.subplot(111)

# Plotting the data
df.plot(kind='bar', x='Art Form', y='Monthly Visitors (Thousands)', ax=ax, legend=False, rot=45)

# Adding the grid, labels, title, and making the labels fancy
ax.set_title('Monthly Visitor Statistics Across Various Art Forms')
ax.set_xlabel('Art Form')
ax.set_ylabel('Monthly Visitors (Thousands)')
ax.grid(True)

# Handling text overlap
ax.tick_params(axis='x', which='major', labelsize=10)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', fontsize=10)

# Automatically resizing the image by tight_layout() before savefig()
plt.tight_layout()

# Save the image to an absolute path
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/106.png', dpi=300)

# Clear the current image state at the end of the code
plt.close()
