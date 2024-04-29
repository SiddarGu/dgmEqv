
import matplotlib.pyplot as plt
import numpy as np

#Prepare data
month = ['January','February','March','April','May','June','July','August','September','October','November','December']
cafe,restaurant,catering = [20,25,30,35,40,45,50,55,60,65,70,75],[50,55,60,65,70,75,80,85,90,95,100,105],[30,35,40,45,50,55,60,65,70,75,80,85]

#Draw chart
fig,ax = plt.subplots(figsize=(12, 8))
ax.plot(month, cafe, label='Cafe sales', marker='o', linestyle='--', color='b', alpha=0.8)
ax.plot(month, restaurant, label='Restaurant sales', marker='*', linestyle='-.', color='r', alpha=0.8)
ax.plot(month, catering, label='Catering sales', marker='d', linestyle='-', color='g', alpha=0.8)

#Set xticks
x_pos = np.arange(len(month))
ax.set_xticks(x_pos)
ax.set_xticklabels(month, rotation=30, wrap=True)

#Set legend
plt.legend(loc='best', fontsize=12)

#Set title
plt.title('Annual sales of food and beverage industry in the USA', fontsize=16)

#Set labels
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Sales(million dollars)', fontsize=14)

#Set grid
ax.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.5)

#Set annotation
for a, b, c in zip(month, cafe, restaurant):
    ax.annotate('({}, {})'.format(a, b), xy=(a, b), xytext=(a, b+2), fontsize=10)
    ax.annotate('({}, {})'.format(a, c), xy=(a, c), xytext=(a, c+2), fontsize=10)

#Resize
plt.tight_layout()

#Save
plt.savefig('line chart/png/187.png')

#Clear
plt.clf()