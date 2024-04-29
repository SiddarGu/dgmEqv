
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8,5))
ax = fig.add_subplot()
ax.bar(['USA','UK','Germany','France'], [4000,3500,3700,3900], label='Criminal Cases', color='#ff6600', bottom=0)
ax.bar(['USA','UK','Germany','France'], [6000,5500,4500,4800], label='Civil Cases', color='#00cc99', bottom=4000)
ax.set_xlabel('Country')
ax.set_ylabel('Number')
ax.set_title('Number of criminal and civil cases in four countries in 2021')
ax.legend()

plt.xticks(['USA','UK','Germany','France'])
plt.tight_layout()
plt.savefig('bar_92.png')
plt.clf()