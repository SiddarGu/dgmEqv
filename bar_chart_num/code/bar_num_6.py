
import matplotlib.pyplot as plt
import numpy as np

Country = ['USA','UK','Germany','France']
Hotel_Stays = [100, 90, 80, 110]
Restaurants_Visits = [400, 350, 300, 450]

fig, ax = plt.subplots(figsize=(10, 8))
xtick_pos = np.arange(len(Country))

ax.bar(xtick_pos-0.2, Hotel_Stays, width=0.4, label='Hotel Stays(thousands)', color='blue')
ax.bar(xtick_pos+0.2, Restaurants_Visits, width=0.4, label='Restaurants Visits(thousands)', color='purple')

ax.set_title('Tourist visits to hotels and restaurants in four countries in 2021')
ax.set_xticks(xtick_pos)
ax.set_xticklabels(Country)
ax.legend(loc='best')
plt.tight_layout()

for i, v in enumerate(Hotel_Stays):
    ax.text(xtick_pos[i]-0.2, v+5, str(v), rotation=90, color='blue', fontsize=10)

for i, v in enumerate(Restaurants_Visits):
    ax.text(xtick_pos[i]+0.2, v+5, str(v), rotation=90, color='purple', fontsize=10)

plt.savefig('Bar Chart/png/331.png')
plt.clf()