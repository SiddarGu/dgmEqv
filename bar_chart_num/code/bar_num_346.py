
import matplotlib.pyplot as plt
import numpy as np

#create figure
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(1,1,1)

#data
social_media=['Facebook','Twitter','Instagram','Snapchat']
users=[2.8,392,1.2,390]
ad_revenue=[86,3.2,20,2.5]

#draw bar chart
x = np.arange(len(social_media))
ax.bar(x, users,width=0.4, label='Users(million)', color='#539caf')
ax.bar(x+0.4, ad_revenue, width=0.4, label='Ad Revenue(billion)', color='#7663b0')

#label ticks
ax.set_xticks(x+0.4/2)
ax.set_xticklabels(social_media, rotation=45, fontsize=10)
ax.set_title('Number of users and ad revenue of four social media platforms in 2021')
ax.set_xlabel('Social Media')
ax.set_ylabel('Number of Users/Ad Revenue')
ax.legend()

#annotate
for p in ax.patches:
    ax.annotate(str(round(p.get_height(),2)), 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', xytext=(0, 10), 
                textcoords='offset points')

#resize
plt.tight_layout()

#save
plt.savefig('Bar Chart/png/265.png')

#clear
plt.clf()