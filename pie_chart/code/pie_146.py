
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# Set the parameters of the figure
mpl.rcParams['figure.figsize'] = (10,10) 

# Data to be represented
Renewables = ['Solar', 'Wind', 'Geothermal', 'Hydroelectric', 'Biomass']
Percentage = np.array([20, 35, 20, 20, 5])

# Create a figure
fig = plt.figure() 

# Create a pie chart
ax = fig.add_subplot()
ax.pie(Percentage, labels=Renewables, autopct='%1.1f%%',
       textprops={'fontsize': 14}, startangle=90,
       wedgeprops={'linewidth':2, 'edgecolor':'white'})

# Title of the figure
ax.set_title('Percentage of Renewable Energy Sources in the USA, 2023', fontsize=14)

# Set the axis of x and y to zero
ax.set_xticks(())
ax.set_yticks(())

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the figure
plt.savefig('pie chart/png/20.png')

# Clear the current image state
plt.clf()