
import matplotlib.pyplot as plt
import numpy as np 

fig=plt.figure(figsize=(8,8))
ax=fig.add_subplot(111)

sports=['Football','Basketball','Ice Hockey','Golf','Motorsport']
share=[45,20,15,10,10]

explode=[0.2,0,0,0,0]
ax.pie(share,explode=explode,labels=sports,autopct='%1.1f%%',shadow=True,startangle=90,textprops={'fontsize': 10})
ax.set_title("Global Market Share of Popular Sports in 2023")

plt.tight_layout()
plt.savefig('pie chart/png/176.png')
plt.show()
plt.clf()