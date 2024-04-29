

import matplotlib.pyplot as plt 
fig=plt.figure(figsize=(6,4))
ax=fig.add_subplot(1,1,1)
label=['Pop Music','Rock Music','Hip-Hop/Rap','Country Music','Latin Music','Jazz','Classical Music']
percentage=[35,25,14,10,8,4,4]
ax.pie(percentage, labels=label,autopct='%.1f%%', startangle=90,textprops={'fontsize': 15})
ax.set_title('Music Genre Popularity in the USA, 2023',fontsize=18,loc='center')
plt.tight_layout()
plt.savefig('pie chart/png/77.png')
plt.clf()