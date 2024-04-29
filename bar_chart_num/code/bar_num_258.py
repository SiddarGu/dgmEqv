
import matplotlib.pyplot as plt
import numpy as np

Country = ['USA', 'UK', 'Germany', 'France']
Internet_Users = [250, 90, 70, 50]
Smartphone_Users = [220, 80, 60, 40]

fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(Country, Internet_Users, label="Internet Users", color='#FFC0CB')
ax.bar(Country, Smartphone_Users, label="Smartphone Users", bottom=Internet_Users, color='#FFB6C1')

for i in range(len(Country)):
    ax.text(x=i, y=Internet_Users[i]/2, s=Internet_Users[i], size=12, ha='center', va='center')
    ax.text(x=i, y=Internet_Users[i]+Smartphone_Users[i]/2, s=Smartphone_Users[i], size=12, ha='center', va='center')

ax.set_title("Number of internet and smartphone users in four countries in 2021")
ax.set_ylabel("Number of users (million)")
ax.set_xticks(np.arange(len(Country)))
ax.set_xticklabels(Country)
ax.legend(loc='upper right')

plt.tight_layout()
plt.savefig('Bar Chart/png/258.png')
plt.clf()