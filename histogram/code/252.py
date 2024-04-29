import pandas as pd
import matplotlib.pyplot as plt

# Data preprocessing
data_labels = ['Operating Income ($Billion)']
line_labels = ['Q1', 'Q2', 'Q3', 'Q4']
data = [2.3, 2.7, 3.1, 3.5]

# Create a dataframe
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Create a figure and add a subplot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)

# Plot a histogram
df.plot(kind='bar', ax=ax, legend=False, grid=True, color=['skyblue', 'orange', 'green', 'red'])

# Title and labels
ax.set_title('Quarterly Operating Income in the Tech Industry', fontsize=14)
ax.set_xlabel('Quarter', fontsize=12)
ax.set_ylabel('Operating Income ($Billion)', fontsize=12)

# Rotate x-axis labels if they are too long
for tick in ax.get_xticklabels():
    tick.set_rotation(45)
    tick.set_wrap(True)

# Resize image before saving
plt.tight_layout()

# Save image to file
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/602.png')

# Clear the current image state
plt.clf()
