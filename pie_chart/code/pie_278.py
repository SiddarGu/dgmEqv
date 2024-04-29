

import matplotlib.pyplot as plt
import pandas as pd

data = {'Art Forms':['Music','Visual Arts','Performance Arts','Literature','Theatre','Design'],
        'Percentage':[20,25,15,20,15,5]}

df = pd.DataFrame(data)

plt.figure(figsize=(6,6))
ax = plt.subplot()
ax.axis('equal') 

labels = df['Art Forms']
sizes = df['Percentage']
explode=(0.1,0.1,0,0,0,0)

ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90, textprops={'wrap':True, 'rotation':90})

ax.set_title('Distribution of Popular Art Forms in 2023')

plt.tight_layout()
plt.savefig('pie chart/png/298.png')
plt.clf()