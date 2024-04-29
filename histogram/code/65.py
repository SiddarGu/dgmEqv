import pandas as pd
import matplotlib.pyplot as plt

# Given data
data_content = """
Donation Range ($),Number of Organizations
0-1000,18
1000-5000,24
5000-10000,30
10000-20000,25
20000-50000,22
50000-100000,15
100000-200000,10
200000-500000,5
500000+,2
"""

# Transforming data into separate variables
data_lines = data_content.strip().split('\n')
data_labels = data_lines[0].split(',')[1:]
line_labels, data = zip(*[line.split(',') for line in data_lines[1:]])
line_labels = list(line_labels)
data = list(map(int, data))

# Create a DataFrame from the data
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Set up the figure and axis
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Plotting the data as a horizontal histogram
df.plot(kind='barh', legend=None, ax=ax, color='skyblue')

# Setting the title
ax.set_title('Frequency of Donation Amounts to Charity and Nonprofit Organizations')

# Adding the labels
ax.set_xlabel('Number of Organizations')
ax.set_ylabel('Donation Range ($)')

# Enabling grid
ax.grid(True)

# Auto-sizing the layout to prevent clipping of tick-labels
plt.tight_layout()

# If the text label is too long, rotate it or display on separate lines
for label in ax.get_yticklabels():
    if len(label.get_text()) > 10:
        label.set_wrap(True)
    label.set_rotation(45)

# Save the image
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/65.png'
plt.savefig(save_path, format='png')

# Clear the current image state
plt.clf()
