
import matplotlib.pyplot as plt
import numpy as np

Country=['USA','UK','Germany','France']
Criminal_Cases=[1500,1700,1600,1800]
Civil_Cases=[3000,3300,3200,3400]

fig, ax = plt.subplots(figsize=(10,7))

ax.bar(Country, Criminal_Cases, label='Criminal Cases',width=0.3,bottom=Civil_Cases)
ax.bar(Country, Civil_Cases, label='Civil Cases',width=0.3)

ax.set_title('Number of Criminal and Civil Cases in four countries in 2021')
ax.set_xticks(Country)
ax.set_ylabel('Number of Cases')
ax.legend()

for i, v in enumerate(Criminal_Cases):
    ax.text(i-0.15, v+50, str(v), color='black', fontsize=12, fontweight='bold')

for i, v in enumerate(Civil_Cases):
    ax.text(i+0.15, v+50, str(v), color='black', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('Bar Chart/png/508.png')
plt.clf()