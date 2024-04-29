

import matplotlib.pyplot as plt
import numpy as np

#clearing the current image state
plt.clf()

#setting data
year=[2001,2002,2003,2004]
raw_material_price=[1000,1100,1200,1300]
production_cost=[3000,2500,2700,2900]
unit_cost=[3,2.5,2.75,3.2]

#creating figure
fig = plt.figure(figsize=(20,10))

#add subplot
ax = fig.add_subplot(111)

#plot the data
ax.plot(year,raw_material_price, label="Raw Material Price (dollars per ton)", color='b')
ax.plot(year,production_cost, label="Production Cost (dollars per ton)", color='g')
ax.plot(year,unit_cost, label="Unit Cost (dollars per unit)", color='r')

#set xticks
plt.xticks(year, rotation=0)

#set title
ax.set_title("Cost of Manufacturing Products over Years")

#set legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
          ncol=3, fancybox=True, shadow=True, fontsize=20)

#tight_layout
plt.tight_layout()

#saving the figure
plt.savefig('line chart/png/472.png')