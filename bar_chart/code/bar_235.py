
import matplotlib.pyplot as plt
import numpy as np

country=['USA','UK','Germany','France']
sports_team=[20,15,14,13]
stadium_capacity=[150000,120000,100000,90000]

fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot()
ax.bar(country,sports_team,label='Sports Team',bottom=0)  
ax.bar(country,stadium_capacity,label='Stadium Capacity',bottom=sports_team)
ax.set_title('Number of sports teams and stadium capacity in four countries in 2021')
ax.set_xticklabels(country,rotation=30,ha='right',wrap=True)
ax.legend(loc='upper left')
plt.tight_layout()
plt.savefig('bar chart/png/321.png')
plt.clf()