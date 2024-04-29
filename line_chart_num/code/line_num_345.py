
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot(111)

year = [2011,2012,2013,2014]
restaurants = [1000,1200,1500,1700]
fast_food_chains = [400,500,400,450]
cafes = [200,250,300,350]
bakeries = [50,60,70,80]

ax.plot(year, restaurants, label="Restaurants")
ax.plot(year, fast_food_chains, label="Fast Food Chains")
ax.plot(year, cafes, label="Cafes")
ax.plot(year, bakeries, label="Bakeries")

ax.set_title('Growth of Food and Beverage Establishments in the United States from 2011 to 2014', fontsize=15)
ax.set_xlabel('Year', fontsize=13)
ax.set_ylabel('Number of Establishments', fontsize=13)
ax.set_xticks(year)
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0., fontsize=13)

for i,j in zip(year,restaurants):
    ax.annotate(str(j),xy=(i,j))
for i,j in zip(year,fast_food_chains):
    ax.annotate(str(j),xy=(i,j))
for i,j in zip(year,cafes):
    ax.annotate(str(j),xy=(i,j))
for i,j in zip(year,bakeries):
    ax.annotate(str(j),xy=(i,j))

plt.tight_layout()
plt.savefig("line chart/png/371.png")
plt.clf()