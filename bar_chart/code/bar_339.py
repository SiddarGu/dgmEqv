
import matplotlib.pyplot as plt
plt.figure(figsize=(8,4))
ax = plt.subplot()
ax.bar(['Football', 'Basketball', 'Cricket', 'Hockey'], [200, 150, 220, 180], bottom=0, label='Participants')
ax.bar(['Football', 'Basketball', 'Cricket', 'Hockey'], [1500, 1800, 1700, 1400], bottom=200, label='Viewers')
ax.set_title('Number of Participants and Viewers for Four Sports in 2021')
ax.set_xlabel('Activity')
ax.set_ylabel('Number of People')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('bar chart/png/268.png')
plt.clf()