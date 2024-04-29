
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np

#data
year = [2001,2002,2003,2004,2005]
donations = [100,150,200,180,220]
volunteers = [2000,2500,3000,2700,3500]

#plot
fig,ax = plt.subplots(figsize=(8,6))
ax.plot(year,donations,label='Donations(million dollars)',color='b', marker='o')
ax.plot(year,volunteers,label='Volunteers',color='r', marker='o')

ax.xaxis.set_major_locator(plt.MaxNLocator(5))
ax.yaxis.set_major_formatter(FuncFormatter(lambda x, p: format(int(x), ',')))

# add a legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.12),
          fancybox=True, shadow=True, ncol=5)

# add text annotation to each data point
for i,Donation in enumerate(donations):
    ax.annotate(Donation,(year[i],donations[i]), fontsize=10)
for i,Volunteer in enumerate(volunteers):
    ax.annotate(Volunteer,(year[i],volunteers[i]), fontsize=10)

# add title
ax.set_title("Growth of Donations and Volunteers for Nonprofit Organizations", fontsize=14)

plt.tight_layout()
plt.savefig('line chart/png/165.png')
plt.clf()