

import matplotlib.pyplot as plt
import numpy as np

region = np.array(['North','South','East','West'])
cases_filed = np.array([3200,4200,3600,3800])
avg_resolution = np.array([11,15,13,12])

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot()
ax.bar(region, cases_filed, color='#7CB9E8', label='Cases Filed')
ax.bar(region, avg_resolution, bottom=cases_filed, color='#FFB6C1', label='Average Resolution Time (months)')

ax.set_xticks(region)
ax.set_title('Law and Legal Affairs Cases Filed and Average Resolution Time in Four Regions in 2021')
ax.set_xlabel('Region')
ax.set_ylabel('Cases Filed/Average Resolution Time (months)')
ax.legend()
plt.tight_layout()

for x,y in zip(region, cases_filed):
        plt.annotate(y, # this is the text
                     (x,y), # this is the point to label
                     textcoords="offset points", # how to position the text
                     xytext=(0,10), # distance from text to points (x,y)
                     ha='center') # horizontal alignment can be left, right or center

for x,y1,y2 in zip(region, cases_filed, avg_resolution):
        plt.annotate(y2, # this is the text
                     (x,y1+y2/2), # this is the point to label
                     textcoords="offset points", # how to position the text
                     xytext=(0,10), # distance from text to points (x,y)
                     ha='center') # horizontal alignment can be left, right or center

plt.savefig('Bar Chart/png/62.png')  
plt.clf()