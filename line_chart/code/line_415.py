

import matplotlib.pyplot as plt
import matplotlib

# Set the font
matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.sans-serif'] = ['Arial']

# Create the figure
fig = plt.figure(figsize=(8,5))
# Add the subplot
ax = fig.add_subplot(111)

# Plot the data
ax.plot([2015, 2016, 2017, 2018, 2019, 2020], [1.2, 1.5, 1.8, 2.1, 2.5, 2.9], color='#C24641', linewidth=3, label='Number of Users')
ax.plot([2015, 2016, 2017, 2018, 2019, 2020], [2.5, 2.7, 3.2, 3.4, 3.9, 4.2], color='#519548', linewidth=3, label='Average Hours per Day')

# Set the X-axis label
ax.set_xlabel('Year', fontsize=12, fontweight='bold')

# Set the Y-axis label
ax.set_ylabel('Number (billion)', fontsize=12, fontweight='bold')

# Set the title
ax.set_title('Social Media User Growth and Time Spent per Day', fontsize=15, fontweight='bold')

# Set the grid
ax.yaxis.grid()

# Set the xticks
xticks = [2015, 2016, 2017, 2018, 2019, 2020] 
plt.xticks(xticks)

# Add the legend
ax.legend(loc='upper left', fontsize=12)

# Set the tight layout
plt.tight_layout()

# Save the figure
plt.savefig('line chart/png/283.png')

# Clear the figure
plt.clf()