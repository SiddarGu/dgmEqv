
import matplotlib.pyplot as plt
import numpy as np

data = {'Country': ['USA', 'UK', 'Germany', 'France'], 
        'Criminal Cases': [20000,15000,17000,18000], 
        'Civil Cases': [25000,19000,24000,22000]
       }

x = np.arange(len(data['Country']))
width = 0.35

fig,ax = plt.subplots(figsize=(10,7))

ax.bar(x - width/2, data['Criminal Cases'], width, label='Criminal Cases',color='#349adf')
ax.bar(x + width/2, data['Civil Cases'], width, label='Civil Cases',color='#f06b6f')

ax.set_xticks(x)
ax.set_xticklabels(data['Country'])

for i, v in enumerate(data['Criminal Cases']):
    ax.text(i - width/2, v + 1000, str(v), color='black', fontweight='bold')
for i, v in enumerate(data['Civil Cases']):
    ax.text(i + width/2, v + 1000, str(v), color='black', fontweight='bold')

ax.set_title('Number of criminal and civil cases in four countries in 2021')
ax.legend()

plt.tight_layout()
plt.savefig('Bar Chart/png/574.png')
plt.clf()