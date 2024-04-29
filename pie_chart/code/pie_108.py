

import matplotlib.pyplot as plt

#create figure
fig = plt.figure(figsize=(8,8))
ax=fig.add_subplot(111)

#data
Platforms = ['YouTube','Facebook','Twitter','Instagram','Snapchat','LinkedIn','TikTok','Other']
Percentage = [30,22,10,18,10,4,4,2]

#plot pie chart
ax.pie(Percentage, labels=Platforms,autopct='%1.1f%%',textprops={'fontsize': 10},wedgeprops={'linewidth':2,'edgecolor':"white"},radius=1)

#set title
ax.set_title('Distribution of Social Media Platform Usage in the USA, 2023',fontsize=16)

#set legend
ax.legend(Platforms,loc="best",bbox_to_anchor=(0.9, 0.5))

#set xticks
plt.xticks(rotation=45)

#resize image
plt.tight_layout()

#save image
plt.savefig('pie chart/png/106.png')
plt.clf()