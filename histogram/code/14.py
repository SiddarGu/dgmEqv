import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data_str = """Age Group (Years),Average Monthly Healthcare Costs ($)
0-18,123.50
19-25,146.75
26-35,187.30
36-45,221.85
46-55,399.90
56-65,575.40
66+,846.20"""

# Split the data string into lines and then into a list of lists
lines = data_str.strip().split('\n')
data_labels = lines[0].split(',')[1:]
line_labels, data = zip(*[line.split(',') for line in lines[1:]])

# Convert the data into the correct types
line_labels = list(line_labels)
data = [float(value) for value in data]

# Create a pandas DataFrame
df = pd.DataFrame(list(zip(line_labels, data)), columns=['Age Group', 'Average Costs'])

# Create a figure and add a subplot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Plotting the data
df.plot(kind='bar', x='Age Group', y='Average Costs', legend=False, ax=ax, color='skyblue', edgecolor='black')

# Set labels and title with a larger fontsize
ax.set_xlabel('Age Group (Years)', fontsize=12)
ax.set_ylabel('Average Monthly Healthcare Costs ($)', fontsize=12)
ax.set_title('Average Healthcare Expenses by Age Group in the U.S.', fontsize=14)

# Set the rotation of the labels on the x-axis to avoid overlapping
ax.set_xticklabels(df['Age Group'], rotation=45)

# Enabling the grid
ax.grid(True, linestyle='--', which='major', color='grey', alpha=.25)

# Automatically adjust the subplot params for the image layout
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/14.png', format='png', dpi=300)

# Clear the current figure state to avoid interference with future plots
plt.clf()
