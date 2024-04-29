

import matplotlib.pyplot as plt
import numpy as np

Country = np.array(['USA', 'UK', 'Germany', 'France'])
Websites = np.array([200, 150, 180, 230])
Users = np.array([450, 400, 350, 300])

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot()

ax.bar(Country, Websites, label='Websites', color='#4f86f7', bottom=Users)
ax.bar(Country, Users, label='Users', color='#f7a35c')
ax.legend(loc='upper left')
ax.set_title('Number of websites and users in four countries in 2021')
for i, v in enumerate(Websites):
    ax.text(i-0.15, v/2+Users[i], str(v), color='#4f86f7', fontsize=12, ha='center', rotation=90)
for i, v in enumerate(Users):
    ax.text(i-0.15, v/2, str(v), color='#f7a35c', fontsize=12, ha='center', rotation=90)
plt.xticks(Country)
plt.tight_layout()
plt.savefig('Bar Chart/png/528.png')
plt.clf()