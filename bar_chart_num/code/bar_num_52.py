
import matplotlib.pyplot as plt 
import numpy as np

# Set data 
Country = ['USA','UK','Germany','France']
Food_Consumption = [200,300,180,230]
Beverage_Consumption = [500,550,400,450]

# Plot figure
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot()
barWidth = 0.3

# Plot bars
r1 = np.arange(len(Country))
r2 = [x + barWidth for x in r1]
ax.bar(r1, Food_Consumption, width=barWidth, bottom=0, label='Food Consumption')
ax.bar(r2, Beverage_Consumption, width=barWidth, bottom=0, label='Beverage Consumption')

# Set labels, title
ax.set_xticks([r + barWidth for r in range(len(Country))])
ax.set_xticklabels(Country)
ax.set_title('Food and Beverage Consumption in four countries in 2021')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
          fancybox=True, shadow=True, ncol=2)

# Label annotations
for x, y in enumerate(Food_Consumption):
    ax.annotate(str(y), xy=(x - 0.1, y + 0.5), color='black')
for x, y in enumerate(Beverage_Consumption):
    ax.annotate(str(y), xy=(x + 0.2, y + 0.5), color='black')
plt.tight_layout()

# Save figure
plt.savefig('Bar Chart/png/254.png')
plt.clf()