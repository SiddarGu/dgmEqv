
import matplotlib.pyplot as plt
import numpy as np

data=[["USA",200,2000],["UK",150,1800],["Germany",180,1500],["France",130,1600]]

x=np.arange(len(data))
universities=[num[1] for num in data]
schools=[num[2] for num in data]

fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot()

ax.bar(x-0.2, universities, width=0.4, label='Universities',color='b')
ax.bar(x+0.2, schools, width=0.4, label='Schools',color='#FF7F50')

ax.set_xticks(x)
ax.set_xticklabels([num[0] for num in data], rotation=0, fontsize='large')
ax.set_title("Number of universities and schools in four countries in 2021")
ax.legend(fontsize='large')
plt.tight_layout()
plt.savefig('bar chart/png/159.png', dpi=300)
plt.clf()