
import matplotlib.pyplot as plt
import numpy as np

data = [['USA', 8.5, 20, 21.4],
        ['UK', 7.5, 25, 2.9],
        ['Germany', 9.0, 30, 4.2],
        ['France', 8.0, 35, 2.9]]

# Create figure
fig = plt.figure(figsize=(8,5))

# Plot bar chart
ax = fig.add_subplot()

# Define labels
labels = ['Public Services','Tax Rate','GDP']

# Get data
data_x = np.arange(len(data))
data_y0 = [i[1] for i in data]
data_y1 = [i[2] for i in data]
data_y2 = [i[3] for i in data]
data_y = [data_y0, data_y1, data_y2]

# Create bar chart
ax.bar(data_x, data_y0, label=labels[0], color='#539caf')
ax.bar(data_x, data_y1, bottom=data_y0, label=labels[1], color='#7663b0')
ax.bar(data_x, data_y2, bottom=[sum(x) for x in zip(data_y1,data_y0)], label=labels[2], color='#e45756')

# Set x-axis
ax.set_xticks(data_x)
ax.set_xticklabels([i[0] for i in data])

# Add title and legend
ax.set_title('Public services, tax rate and GDP of four countries in 2021')
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

# Add value annotation
for x, y0, y1, y2 in zip(data_x, data_y0, data_y1, data_y2):
    ax.annotate(f'{y0}', xy=(x, y0/2), ha='center')
    ax.annotate(f'{y1}', xy=(x, y0+y1/2), ha='center')
    ax.annotate(f'{y2}', xy=(x, y0+y1+y2/2), ha='center', rotation=90, wrap=True)

# Resize the image
fig.tight_layout()

# Save figure
plt.savefig('bar_118.png')

# Clear figure
plt.clf()