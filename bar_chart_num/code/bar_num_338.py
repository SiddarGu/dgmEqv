
import numpy as np
import matplotlib.pyplot as plt

sports = ['Basketball','Football','Volleyball','Badminton']
tournaments = [20,30,25,15]
participants = [3000,3500,4000,2500]

x = np.arange(len(sports)) 
width = 0.35 

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

ax.bar(x - width/2, tournaments, width, label='Tournaments')
ax.bar(x + width/2, participants, width, label='Participants')

ax.set_ylabel('Number')
ax.set_title('Number of tournaments and participants in four sports in 2021')
ax.set_xticks(x)
ax.set_xticklabels(sports)
ax.legend()

for i, v in enumerate(tournaments):
    ax.text(i - 0.3, v + 50, str(v))
    
for i, v in enumerate(participants):
    ax.text(i + 0.1, v + 50, str(v))

plt.tight_layout()
plt.savefig('Bar Chart/png/596.png')
plt.clf()