
import matplotlib.pyplot as plt
import numpy as np

# Data to plot
Country = ['USA', 'UK', 'Germany', 'France']
Renewable = [25, 30, 35, 40]
Fossil = [75, 70, 65, 60]

# create figure
fig = plt.figure(figsize=(16,8))
ax = fig.add_subplot(111)

# plot bars
ax.bar(Country, Renewable, color='tab:green', label='Renewable Energy Usage(%)')
ax.bar(Country, Fossil, bottom=Renewable, color='tab:red', label='Fossil Fuels Usage(%)')

# set ticks
ax.set_xticks(np.arange(len(Country)))
ax.set_xticklabels(Country)

# label data points
for x, y, z in zip(Country, Renewable, Fossil):
    ax.text(x, y/2, '{}%'.format(y), ha='center', va='center')
    ax.text(x, y+z/2, '{}%'.format(z), ha='center', va='center')

# set labels
ax.set_title('Usage of Renewable and Fossil Fuels in four countries in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Usage(%)')

# show legend
ax.legend(loc=(1.04,0.5)) 

# adjust layout
plt.tight_layout()

# save figure
plt.savefig('Bar Chart/png/65.png', bbox_inches="tight")

# clear current image
plt.clf()