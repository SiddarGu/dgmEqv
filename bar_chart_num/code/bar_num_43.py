
import matplotlib.pyplot as plt
import numpy as np

# Set the figure size
plt.figure(figsize=(9,6))

# Create an axis
ax = plt.subplot()

# Set the labels of the x-axis
country = ['USA', 'UK', 'Germany', 'France']

# Set the position of the x-axis
ind = np.arange(len(country))

# Set the data of the y-axis
nuclear = [20, 10, 30, 25]
solar = [50, 35, 60, 55]
wind = [60, 25, 45, 40]

# Create the bar chart
p1 = ax.bar(ind, nuclear, color='#006699', edgecolor='white', width=0.5)
p2 = ax.bar(ind, solar, bottom=nuclear, color='#5EF1F2', edgecolor='white', width=0.5)
p3 = ax.bar(ind, wind, bottom=np.array(nuclear)+np.array(solar), color='#FFCC66', edgecolor='white', width=0.5)

# Set the title and labels
ax.set_title('Energy production from nuclear, solar, and wind sources in four countries in 2021', fontsize=14)
ax.set_ylabel('Energy Production (GW)', fontsize=12)
ax.set_xticks(ind)
ax.set_xticklabels(country, fontsize=12)

# Create the legend
ax.legend((p1[0], p2[0], p3[0]), ('Nuclear', 'Solar', 'Wind'), fontsize=12)

# Automatically resize the image
plt.tight_layout()

# Label the value of each data point for every variables directly on the figure
for p1, p2, p3 in zip(p1, p2, p3):
    ax.annotate('{:.0f}'.format(p1.get_height()), xy=(p1.get_x()+p1.get_width()/2, p1.get_height()), 
                ha='center', va='center', fontsize=10, color='black')
    ax.annotate('{:.0f}'.format(p2.get_height()), xy=(p2.get_x()+p2.get_width()/2, p2.get_height()+p1.get_height()), 
                ha='center', va='center', fontsize=10, color='black')
    ax.annotate('{:.0f}'.format(p3.get_height()), xy=(p3.get_x()+p3.get_width()/2, p3.get_height()+p1.get_height()+p2.get_height()), 
                ha='center', va='center', fontsize=10, color='black')

# Save the figure
plt.savefig('Bar Chart/png/153.png', dpi=300)

# Clear the current figure
plt.clf()