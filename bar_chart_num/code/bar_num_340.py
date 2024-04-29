
import matplotlib.pyplot as plt 
import numpy as np 

Country = ['USA', 'UK', 'Germany', 'France'] 
Engineers = [500, 450, 650, 550]
Scientists = [400, 350, 550, 450]

fig = plt.figure(figsize=(10, 6)) 
ax = fig.add_subplot(111) 

width = 0.3 
x = np.arange(len(Country)) 

ax.bar(x - width/2, Engineers, width, color='b', label='Engineers')
ax.bar(x + width/2, Scientists, width, color='g', label='Scientists')

ax.set_xticks(x)
ax.set_xticklabels(Country)
ax.set_title('Number of engineers and scientists in four countries in 2021')

ax.legend(bbox_to_anchor=(1.02, 0.5), loc='center left', borderaxespad=0.)

for i, v in enumerate(Engineers):
    ax.text(i - width/2, v + 0.5, str(v), color='b')

for i, v in enumerate(Scientists):
    ax.text(i + width/2, v + 0.5, str(v), color='g')

fig.tight_layout()
fig.savefig('Bar Chart/png/530.png')
plt.clf()