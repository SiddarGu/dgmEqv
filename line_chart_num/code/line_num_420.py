
import matplotlib.pyplot as plt
import numpy as np

#Define data
year = np.array(['2018','2019','2020','2021','2022'])
fast_food_rev = np.array([550, 600, 650, 700, 750])
restaurant_rev = np.array([800, 900, 1000, 1100, 1200])
grocery_store_rev = np.array([1200, 1300, 1200, 1400, 1500])

#Create figure
fig=plt.figure(figsize=(14, 8))
ax=fig.add_subplot(1,1,1)

#Plot line chart
ax.plot(year, fast_food_rev, label='Fast Food Revenues', marker="o", linestyle="-")
ax.plot(year, restaurant_rev, label='Restaurant Revenues', marker="o", linestyle="-")
ax.plot(year, grocery_store_rev, label='Grocery Store Revenues', marker="o", linestyle="-")

#Label data points
for x, y in zip(year, fast_food_rev):
    ax.annotate("%.0f" % y, xy=(x, y), xytext=(-5, 5), textcoords="offset points")
for x, y in zip(year, restaurant_rev):
    ax.annotate("%.0f" % y, xy=(x, y), xytext=(-5, 5), textcoords="offset points")
for x, y in zip(year, grocery_store_rev):
    ax.annotate("%.0f" % y, xy=(x, y), xytext=(-5, 5), textcoords="offset points")

#Set x_ticks
plt.xticks(year, rotation=45)

#Add legend
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False)

#Add title
plt.title('Revenues of the Food and Beverage Industry in the US from 2018 to 2022')

#Automatic resizing image
plt.tight_layout()

#Save image
plt.savefig('line chart/png/543.png')

#Clear image state
plt.clf()