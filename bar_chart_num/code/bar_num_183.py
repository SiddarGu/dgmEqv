
import matplotlib.pyplot as plt
import numpy as np

# Create the figure and set its size
fig = plt.figure(figsize=(15,5))
ax = fig.add_subplot(1,1,1)

# Data to be ploted 
Month = ['January','February','March','April']
Electricity_Usage = [1000,900,1100,1200]
Gas_Usage = [800,900,1000,1100]
Water_Usage = [400,450,500,550]

# Plot the bar chart
x = np.arange(len(Month))
width = 0.25
ax.bar(x-width, Electricity_Usage, width, label='Electricity Usage')
ax.bar(x, Gas_Usage, width, label='Gas Usage')
ax.bar(x+width, Water_Usage, width, label='Water Usage')

# Set the title and labels
ax.set_title('Utility usage in three categories from January to April 2021')
ax.set_xlabel('Month')
ax.set_ylabel('kWh')

# Label the value of each data point for every variables directly on the figure
ax.annotate('{}'.format(Electricity_Usage[0]), (x[0]-width, Electricity_Usage[0]), xytext=(0, 5), textcoords='offset points', ha='center', va='bottom')
ax.annotate('{}'.format(Electricity_Usage[1]), (x[1]-width, Electricity_Usage[1]), xytext=(0, 5), textcoords='offset points', ha='center', va='bottom')
ax.annotate('{}'.format(Electricity_Usage[2]), (x[2]-width, Electricity_Usage[2]), xytext=(0, 5), textcoords='offset points', ha='center', va='bottom')
ax.annotate('{}'.format(Electricity_Usage[3]), (x[3]-width, Electricity_Usage[3]), xytext=(0, 5), textcoords='offset points', ha='center', va='bottom')
ax.annotate('{}'.format(Gas_Usage[0]), (x[0], Gas_Usage[0]), xytext=(0, 5), textcoords='offset points', ha='center', va='bottom')
ax.annotate('{}'.format(Gas_Usage[1]), (x[1], Gas_Usage[1]), xytext=(0, 5), textcoords='offset points', ha='center', va='bottom')
ax.annotate('{}'.format(Gas_Usage[2]), (x[2], Gas_Usage[2]), xytext=(0, 5), textcoords='offset points', ha='center', va='bottom')
ax.annotate('{}'.format(Gas_Usage[3]), (x[3], Gas_Usage[3]), xytext=(0, 5), textcoords='offset points', ha='center', va='bottom')
ax.annotate('{}'.format(Water_Usage[0]), (x[0]+width, Water_Usage[0]), xytext=(0, 5), textcoords='offset points', ha='center', va='bottom')
ax.annotate('{}'.format(Water_Usage[1]), (x[1]+width, Water_Usage[1]), xytext=(0, 5), textcoords='offset points', ha='center', va='bottom')
ax.annotate('{}'.format(Water_Usage[2]), (x[2]+width, Water_Usage[2]), xytext=(0, 5), textcoords='offset points', ha='center', va='bottom')
ax.annotate('{}'.format(Water_Usage[3]), (x[3]+width, Water_Usage[3]), xytext=(0, 5), textcoords='offset points', ha='center', va='bottom')

# Set the x ticks
ax.set_xticks(x)
ax.set_xticklabels(Month)

# Place the legend
ax.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0.)

# Adjust the figure
plt.tight_layout()

# Save and clear
plt.savefig('Bar Chart/png/570.png')
plt.clf()