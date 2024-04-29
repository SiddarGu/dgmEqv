
import matplotlib.pyplot as plt

# set figure
fig=plt.figure(figsize=(10,7))
ax=fig.add_subplot(111)

# set data
labels=['Primary','Secondary','Bachelor\'s','Master\'s','Doctoral']
sizes=[20,30,25,15,10]

# draw pie chart
ax.pie(sizes,labels=labels,autopct='%1.1f%%',startangle=90,textprops={'fontsize': 10},wedgeprops={"edgecolor":"k",'linewidth': 1,'linestyle': 'solid', 'antialiased': True})

# set title
ax.set_title('Education Level Distribution in the USA, 2023',fontsize=15)

# set xticks
plt.xticks(rotation=-90, fontsize=10)

# automatically resize 
plt.tight_layout()

# save figure
plt.savefig('pie chart/png/433.png')

# clear current image state
plt.clf()