
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(10, 6))

country = ['USA', 'UK', 'Germany', 'France']
Engineers = [20000, 17000, 18000, 19000]
Scientists = [30000, 25000, 27000, 28000]

ax.bar(country, Engineers, label='Engineers')
ax.bar(country, Scientists, bottom=Engineers, label='Scientists')

ax.set_title('Number of engineers and scientists in four countries in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Number')

plt.xticks(country)
for i, v in enumerate(zip(Engineers, Scientists)):
    ax.text(i-0.2, v[0]+v[1]/2, str(v[1]), color='black', rotation=90, fontsize=15)
    ax.text(i-0.2, v[0]/2, str(v[0]), color='black', rotation=90, fontsize=15)

ax.legend()
plt.tight_layout()
plt.savefig('Bar Chart/png/504.png')
plt.clf()