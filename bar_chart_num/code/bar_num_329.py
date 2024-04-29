
import matplotlib.pyplot as plt
import numpy as np

# Setting figure size
plt.figure(figsize=(10, 6))

# Setting a title
plt.title('Number of sports teams and fans in four states in 2021', fontsize=18)

# Setting x and y axis
x = ['California', 'New York', 'Florida', 'Texas']
y1 = [10, 14, 12, 13]
y2 = [800000, 750000, 700000, 650000]

# Plotting the bars
plt.bar(x, y1, label='Sports Teams')
plt.bar(x, y2, bottom=y1, label='Fans')

# Adding legend
plt.legend(loc='upper right', fontsize=14)

# Adding x and y labels
plt.xlabel('State', fontsize=14)
plt.ylabel('Number', fontsize=14)

# Label the bars of the stacked bar chart
for i in range(len(x)):
    plt.text(x=i-0.13, y=y1[i]/2+y2[i]/2, s=y1[i], color='w', fontsize=14)
    plt.text(x=i-0.13, y=y2[i]/2, s=y2[i], color='w', fontsize=14)

# Setting the xticks
plt.xticks(np.arange(len(x)), x, rotation=0, fontsize=14)

# Automatically adjust subplots
plt.tight_layout(pad=3)

# Save the figure
plt.savefig('Bar Chart/png/101.png')

# Clear the current image state
plt.clf()