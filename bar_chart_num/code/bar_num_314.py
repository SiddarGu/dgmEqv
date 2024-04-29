
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 5))
ax = plt.subplot()
ax.bar(['USA','UK','Germany','France'], [200, 300, 180, 230], label='Hotels', width=0.5)
ax.bar(['USA','UK','Germany','France'], [450, 500, 400, 470], label='Restaurants', width=0.5, bottom=[200, 300, 180, 230])
ax.bar(['USA','UK','Germany','France'], [5000, 4500, 4000, 4200], label='Tourists', width=0.5, bottom=[650, 800, 580, 700])
plt.title("Number of hotels, restaurants and tourists in four countries in 2021")
plt.xlabel("Country")
plt.ylabel("Number")
plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
plt.xticks(rotation=45)
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x()+0.10, p.get_height()+50))
plt.tight_layout()
plt.savefig('Bar Chart/png/89.png')
plt.clf()