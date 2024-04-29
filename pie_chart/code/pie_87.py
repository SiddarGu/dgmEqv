
import matplotlib.pyplot as plt
import numpy as np

Platforms = np.array(['Facebook','YouTube','Instagram','Twitter','LinkedIn','Snapchat','Pinterest'])
Percentage = np.array([35,30,15,10,5,3,2])

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
ax.axis('equal')

wedges, texts, autotexts = ax.pie(Percentage,
                                  labels=Platforms, autopct='%1.1f%%',
                                  textprops={'rotation': 0, 'fontsize': 14},
                                  colors=['#fbb0a9', '#cce5df', '#f5cd79',
                                          '#a2c4c9', '#ffa69e', '#d2dae2', '#e2a9f3'])

for autotext in autotexts:
    autotext.set_color('black')

[t.set_va('top') for t in texts]

ax.set_title('Social Media Platform Usage in 2021')

plt.tight_layout()
plt.savefig('pie chart/png/55.png')
plt.clf()