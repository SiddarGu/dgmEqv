import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = {
    'Degree Level': ["High School", "Associate's", "Bachelor's", "Master's", "Professional", "Doctorate"],
    'Holders (in millions)': [85.3, 35.7, 68.1, 30.4, 5.6, 4.1]
}

# Transforming the given data into three variables: data_labels, data, line_labels
data_labels = ['Holders (in millions)']
line_labels = data.pop('Degree Level')
data_array = data['Holders (in millions)']

# Creating a DataFrame
df = pd.DataFrame(data, index=line_labels)

# Create figure and add a subplot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Plotting the data as a vertical histogram
df.plot(kind='bar', ax=ax, rot=0, legend=False)

# Adding the title
ax.set_title('Educational Attainment in the United States: Degree Holders Distribution')

# Adding gridlines
ax.grid(axis='y')

# Setting up x-axis
ax.set_xticklabels(line_labels, rotation=45, ha='right', fontsize=10)

# Automatically resize the image
plt.tight_layout()

# Save the figure to the specified path
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/207.png', format='png', dpi=300)

# Clear the current image state
plt.clf()
