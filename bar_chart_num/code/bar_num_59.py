
import matplotlib.pyplot as plt
import numpy as np

# Setting the category and data
category = ['Drama', 'Comedy', 'Action', 'Sci-fi']
gross_revenue = [200, 180, 150, 80]
movies_released = [10, 15, 20, 10]

# Create the figure and plot the data
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
width = 0.3
ax.bar(np.arange(len(category)) - width/2, gross_revenue, width=width, label='Gross Revenue(Million)')
ax.bar(np.arange(len(category)) + width/2, movies_released, width=width, label='Movies Released')
ax.set_title('Gross Revenue and Movies Released in four categories in 2021')
ax.set_xticks(np.arange(len(category)))
ax.set_xticklabels(category)
ax.legend()

# Adding the value labels for every variables
for x, y_1, y_2 in zip(np.arange(len(category)), gross_revenue, movies_released):
    ax.annotate('{}M\n{}'.format(y_1, y_2), xy=(x, max(y_1, y_2)), xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom', rotation=45, wrap=True)

# Adjusting the figure for better display
plt.tight_layout()

# Save the figure
plt.savefig('Bar Chart/png/301.png')

# Clear the current image state
plt.clf()