

import matplotlib.pyplot as plt
import numpy as np

Country = ['USA','UK','Germany','France']
FoodDonations = [200, 150, 130, 180]
ClothingDonations = [80, 60, 50, 70]
VolunteerHours = [50, 40, 30, 20]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1,1,1)

width = 0.25
x = np.arange(4)
ax.bar(x - width, FoodDonations, width, label='Food Donations', color='tab:green')
ax.bar(x, ClothingDonations, width, label='Clothing Donations', color='tab:blue')
ax.bar(x + width, VolunteerHours, width, label='Volunteer Hours', color='tab:orange')
ax.set_title('Tonnage and volunteer hours of donations in four countries in 2021')
ax.set_xticks(x)
ax.set_xticklabels(Country)
ax.set_ylim(0, 250)
ax.legend()

for i in range(len(Country)):
    ax.annotate(str(FoodDonations[i]), xy=(x[i] - width, FoodDonations[i] + 10),va='bottom', rotation=90)
    ax.annotate(str(ClothingDonations[i]), xy=(x[i], ClothingDonations[i] + 10),va='bottom', rotation=90)
    ax.annotate(str(VolunteerHours[i]), xy=(x[i] + width, VolunteerHours[i] + 10),va='bottom', rotation=90)
    
fig.tight_layout()
plt.savefig('Bar Chart/png/136.png')
plt.clf()