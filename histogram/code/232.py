import pandas as pd
import matplotlib.pyplot as plt

# Given data
data_string = """0-5,1500
6-8,2400
9-11,3500
12,No data
13-15,4500
16-18,3000
19-21,1500
22-24,1000
25+,600"""

# Processing the data into the required format
data_lines = data_string.split('\n')
data_labels = ['Years of Education', 'Number of Individuals (in thousands)']
line_labels = []
data = []
for line in data_lines:
    parts = line.split(',')
    line_labels.append(parts[0])
    # Exclude 'No data' values
    if parts[1] != 'No data':
        data.append(int(parts[1]))
    else:
        data.append(None)

# Creating the DataFrame
df = pd.DataFrame(data={'Years of Education': line_labels, 
                        'Number of Individuals (in thousands)': data})

# Drop rows with 'No data'
df = df.dropna()

# Plotting the histogram
plt.figure(figsize=(10, 8))
ax = plt.subplot()
df.plot(kind='barh', x='Years of Education', y='Number of Individuals (in thousands)', 
        ax=ax, legend=False, color='skyblue')

# Setting title and labels
plt.title('Educational Attainment and the Number of Individuals in a Population')
plt.xlabel('Number of Individuals (in thousands)')

# Adjusting the text for long labels
ax.tick_params(axis='both', which='major', labelsize=10)
plt.xticks(rotation=45)
plt.yticks(wrap=True)

# Adding background grid
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Automatically adjust subplot params so the subplot(s) fits into the figure area
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/232.png', format='png')

# Clear the current image state
plt.clf()
