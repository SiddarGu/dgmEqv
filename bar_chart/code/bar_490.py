
import matplotlib.pyplot as plt
import numpy as np

#Create figure
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(1, 1, 1)

#Data
Region = ['East Coast','West Coast','Midwest','South']
Average_Property_Price = [300000, 400000, 250000, 350000]
Average_Rental_Cost = [2500, 3000, 2000, 2700]

#Plot
bar_width = 0.3
ax.bar(np.arange(len(Region)), Average_Property_Price, bar_width, label = 'Average Property Price')
ax.bar(np.arange(len(Region)) + bar_width, Average_Rental_Cost, bar_width, label = 'Average Rental Cost')

#Label
ax.set_xticks(np.arange(len(Region)))
ax.set_xticklabels(Region, rotation = 'vertical')
ax.set_xlabel('Region')
ax.set_ylabel('Price ($)')
ax.set_title('Average property prices and rental costs in four regions in 2021')

#Legend
ax.legend(loc = 'upper left', bbox_to_anchor = (1, 1))

#Save
fig.tight_layout()
plt.savefig('bar chart/png/455.png')

#Clear
plt.clf()