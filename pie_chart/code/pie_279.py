
import matplotlib.pyplot as plt
import numpy as np

data_name=['Voting','Contacting Elected Officials','Attending Town Hall Meetings','Signing Petitions','Donating to Political Campaigns','Other']

data_percentage=[40,20,15,10,10,5]

fig=plt.figure(figsize=(10,10))

ax=fig.add_subplot(1,1,1)

ax.pie(data_percentage,labels=data_name,autopct='%1.2f%%',textprops={'fontsize':10},shadow=True,startangle=90,rotatelabels=True,pctdistance=0.7,radius=1.2)

ax.set_title('Methods for Citizen Engagement in the US, 2023',fontsize=15)

plt.tight_layout()

plt.savefig('pie chart/png/507.png')

plt.clf()