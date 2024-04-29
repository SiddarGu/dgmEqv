
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111)

data = [['USA',5000,3000,7000],
['UK', 4000,2500,6000],
['Germany', 4500,3500,5500],
['France', 3500,2000,6500]]

x_pos = np.arange(len(data))
Hotels = [num[1] for num in data]
Restaurants = [num[2] for num in data]
Attractions = [num[3] for num in data]
 
ax.bar(x_pos, Hotels, label='Hotels', width=0.2)
ax.bar(x_pos + 0.2, Restaurants, label='Restaurants', width=0.2)
ax.bar(x_pos + 0.4, Attractions, label='Attractions', width=0.2)

ax.set_xticks(x_pos + 0.2)
ax.set_xticklabels([num[0] for num in data],rotation=45,ha='right')
ax.set_title('Number of hotels, restaurants and attractions in four countries in 2021')
ax.legend(loc='upper left', bbox_to_anchor=(1,1))

plt.tight_layout()
plt.savefig('bar chart/png/409.png')
plt.clf()