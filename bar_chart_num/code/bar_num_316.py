
import matplotlib.pyplot as plt
import numpy as np

# Create a figure
fig = plt.figure(figsize=(8, 6))

# Create axes
ax = fig.add_subplot(111)

# Set x-axis
Country = ['USA', 'UK', 'Germany', 'France']
x_pos = np.arange(len(Country))

# Set bar width
bar_width = 0.3

# Set bar value
lawsuits_filed = [10, 9, 13, 8]
lawsuits_settled = [8, 6, 10, 7]

# Plot the bar chart
rects1 = ax.bar(x_pos, lawsuits_filed, width = bar_width, label='Lawsuits Filed')
rects2 = ax.bar(x_pos + bar_width, lawsuits_settled, width = bar_width, label='Lawsuits Settled', bottom = lawsuits_filed)

# Add x-axis labeling
ax.set_xticks(x_pos + bar_width / 2)
ax.set_xticklabels(Country)

# Add legend
ax.legend(loc='upper left')

# Add title
ax.set_title('Number of Lawsuits Filed and Settled in four countries in 2021')

# Annotate the value of each data point
for rects in rects1 + rects2:
    height = rects.get_height()
    ax.annotate('{}'.format(height),
                xy=(rects.get_x() + rects.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

# Automatically adjust the subplot parameters to give specified padding
plt.tight_layout()

# Save image
plt.savefig('Bar Chart/png/388.png')

# Clear the current image state
plt.clf()