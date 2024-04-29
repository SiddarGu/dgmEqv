
import matplotlib.pyplot as plt
import numpy as np

data=[[20, 3.1], [19, 2.5], [22, 3.2], [21, 2.8]]
Country = ['USA', 'UK', 'Germany', 'France']

fig, ax = plt.subplots(figsize=(7,5))
ax.bar(Country, [i[0] for i in data], label='Tax Rate', bottom=[i[1] for i in data])
ax.bar(Country, [i[1] for i in data], label='Government Spending')

ax.set_title('Tax rate and government spending of four countries in 2021')
ax.set_ylabel('Trillion')
ax.legend()

for i, v in enumerate(data):
    ax.text(i-0.2, v[0]+v[1]/2, str(v[0])+'%', fontsize=12, color='black')
    ax.text(i-0.2, v[1]/2, str(v[1])+'T', fontsize=12, color='black')

plt.xticks(np.arange(len(Country)), Country)
plt.tight_layout()
plt.savefig('Bar Chart/png/126.png',dpi=100)
plt.clf()