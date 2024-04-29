
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
region = ['East', 'West', 'North', 'South']
food_crops = [3000, 4000, 3500, 3800]
livestock = [2500, 3500, 3000, 2700]

ax.bar(region, food_crops, width=0.4, label='Food Crops')
ax.bar(region, livestock, width=0.4, bottom=food_crops, label='Livestock')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=2)
plt.title('Food crops and Livestock production in four regions in 2021')
plt.xticks(rotation=45)
fig.tight_layout()
plt.savefig('bar chart/png/65.png')
plt.clf()