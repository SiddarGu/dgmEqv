

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(15,7))
ax = fig.add_subplot(1,1,1)
ax.bar(['USA','UK','Germany','France'], [1000, 900, 1100, 800], label='Manufacturing Output(million)', color='#449ad1')
ax.bar(['USA','UK','Germany','France'], [1200, 1300, 1400, 1500], label='Export Output(million)', bottom=[1000, 900, 1100, 800], color='#5eb8b5')
ax.set_ylabel('Output(million)', fontsize=15)
ax.set_title('Manufacturing and Export Output from Four Countries in 2021', fontsize=20)
ax.legend(loc='upper right', fontsize=15)
ax.set_xticks(['USA','UK','Germany','France'])
for i,v in enumerate([1000, 900, 1100, 800]):
    ax.text(i-0.2, v/2, str(v), fontsize=15, color='black')
for i,v in enumerate([1200, 1300, 1400, 1500]):
    ax.text(i-0.2, v/2 + (1000, 900, 1100, 800)[i], str(v), fontsize=15, color='black')
plt.tight_layout()
plt.savefig('Bar Chart/png/114.png')
plt.clf()