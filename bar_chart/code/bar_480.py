
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(7,4))
ax = fig.add_subplot()

Country = ('USA', 'UK', 'Germany', 'France')
Internet_Users = np.array([350, 60, 82, 70])
Internet_Penetration = np.array([85, 90, 98, 92])

ax.bar(Country, Internet_Users, label='Internet Users(million)', bottom=0, width=0.3, color='#9EC0F7', edgecolor='#0A3059')
ax.bar(Country, Internet_Penetration, label='Internet Penetration(%)', bottom=0, width=0.3, color='#F1AA7E', edgecolor='#0A3059')

ax.set_xticks(Country)
ax.set_xticklabels(Country, rotation=0, wrap=True)

ax.set_title('Internet users and penetration rate in four countries in 2021')
ax.legend(loc='lower right', bbox_to_anchor=(1.25, 0.5), ncol=1)

plt.tight_layout()
plt.savefig('bar chart/png/460.png')
plt.clf()