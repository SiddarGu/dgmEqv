
import matplotlib.pyplot as plt
from matplotlib.pyplot import pie, axis, title, legend

#Creating figure
fig = plt.figure(figsize=(10,8))

#Data
labels = ['Solar Energy','Wind Energy','Hydropower','Geothermal Energy','Biomass']
sizes = [25,25,20,15,15]

#Plotting Pie Chart
ax = fig.add_subplot()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', textprops={'fontsize':14},startangle=90)
ax.axis('equal')
title('Distribution of Renewable Energy Sources in the USA, 2023')
legend(labels, loc='upper left', bbox_to_anchor=(-0.1, 1.), fontsize=14)

#Saving Figure
plt.tight_layout()
plt.savefig('pie chart/png/228.png')
plt.clf()