
import matplotlib.pyplot as plt
import numpy as np

#Creating figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)

#Setting data
labels = ['USA', 'UK', 'Germany', 'France']
data = np.array([[300, 420, 360], [280, 420, 400], [320, 380, 440], [320, 400, 380]])

# Setting bar width and color 
bar_width = 0.2
colors = ['r', 'g', 'b', 'y']

# Plotting the bars
for i, label in enumerate(labels):
    x_pos = np.arange(3) + (i - 2) * bar_width
    ax.bar(x_pos, data[i], width=bar_width, color=colors[i], label=label, edgecolor='black')

ax.tick_params(axis='x', rotation=45)
ax.set_ylabel('Manufacturing output(million)')
ax.set_xlabel('Categories')
ax.set_title('Manufacturing output in three categories in four countries in 2021')
ax.set_xticks(np.arange(3) + bar_width)
ax.set_xticklabels(['Manufacturing A', 'Manufacturing B', 'Manufacturing C'])
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=4)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('bar chart/png/544.png', dpi=300)

# Clear the current image state
plt.clf()