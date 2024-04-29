
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(15, 7))
ax = fig.add_subplot(111)

plt.bar(['YouTube','Instagram','Twitter','Facebook'], [2.5, 1.8, 0.9, 2.2], color='#6699FF', width=0.5, label='Active Users(million)')
plt.bar(['YouTube','Instagram','Twitter','Facebook'], [120, 90, 60, 100], color='#FFCC66', bottom=[2.5, 1.8, 0.9, 2.2], width=0.5, label='Advertisers')

plt.title('Social Media Platforms and their active users and advertisers in 2021', fontsize=15)
plt.xlabel('Platform', fontsize=12)
plt.ylabel('Number', fontsize=12)
plt.legend(loc='upper left', fontsize=12)
ax.tick_params(axis='x', rotation=45, labelsize=12)
plt.xticks(fontsize=12)

plt.tight_layout()
plt.savefig('bar chart/png/305.png')

plt.clf()