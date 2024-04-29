
import matplotlib.pyplot as plt
import numpy as np

# set the size of the figure
plt.figure(figsize=(12, 8))

# create subplot
ax = plt.subplot()

# set x_data, y_data
x_data = np.array(['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80'])
y1_data = np.array([90, 120, 150, 145, 130, 120, 100, 90])
y2_data = np.array([12, 25, 40, 55, 60, 70, 80, 90])

# draw line chart
ax.plot(x_data, y1_data, label='Height(cm)', color='#1F77B4', linewidth=2.5)
ax.plot(x_data, y2_data, label='Weight(kg)', color='#FF7F0E', linewidth=2.5)

# set x,y axis label
ax.set_xlabel('Age', fontsize=14)
ax.set_ylabel('Value', fontsize=14)

# set x,y tick
ax.set_xticks(np.arange(len(x_data)), x_data)
ax.set_yticks(np.arange(min(y1_data.min(), y2_data.min()),
                    max(y1_data.max(), y2_data.max()) + 5,
                    5))

# add grid
ax.grid(linestyle='--', linewidth=1, color='#b3b3b3')

# add legend
ax.legend(loc='upper left')

# add label
for a, b, c in zip(x_data, y1_data, y2_data):
    ax.annotate(f'{b},{c}', xy=(a, b), xytext=(a, b+5))
    ax.annotate(f'{c}', xy=(a, c), xytext=(a, c+5))

# set title
ax.set_title('Height and Weight of Individuals in Different Age Groups')

# adjust figure layout
plt.tight_layout()

# save figure
plt.savefig('line chart/png/333.png')

# clear figure state
plt.clf()