
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
ax = plt.subplot()
ax.set_title('Annual Cereal Production in the United States, 2001-2004')

ax.plot([2001,2002,2003,2004], [20000,21000,22000,23000],label="Wheat Production(tonnes)", color='orange')
ax.plot([2001,2002,2003,2004], [18000,17000,16000,15000],label="Rice Production(tonnes)", color='pink')
ax.plot([2001,2002,2003,2004], [15000,14500,14000,13500],label="Corn Production(tonnes)", color='green')

ax.set_xlabel('Year')
ax.set_ylabel('Production(tonnes)')

ax.set_xticks([2001,2002,2003,2004])
ax.set_xticklabels(['2001','2002','2003','2004'], rotation = 45, ha = 'right')

ax.legend(loc = 'upper left')
plt.tight_layout()
plt.savefig('line chart/png/263.png',dpi = 600)
plt.clf()