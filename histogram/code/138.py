import matplotlib.pyplot as plt
import pandas as pd

# Given data
data_labels = ['Graduates (Thousands)']
line_labels = ['Arts and Humanities', 'Social Sciences', 'Business', 'STEM (Science, Technology, Engineering, Mathematics)', 'Education', 'Health and Welfare', 'Law', 'Other Fields']
data = [37.2, 45.6, 68.9, 85.7, 32.8, 58.3, 25.4, 19.1]

# Convert data into a DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Create a figure
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot()

# Create horizontal bar plot
df.plot(kind='barh', ax=ax, legend=False, color='skyblue')

# Set the title
ax.set_title('Graduate Numbers by Field of Study in Higher Education')

# Set the y-axis to have the names of fields of study and wrap them if they are too long
ax.set_yticklabels(ax.get_yticklabels(), rotation=45, horizontalalignment='right', wrap=True)

# Adding background grid
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# setting the x-axis label
ax.set_xlabel('Graduates (Thousands)')

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/138.png', format='png')

# Clear the figure
plt.clf()
