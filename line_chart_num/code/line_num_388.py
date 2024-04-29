
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(13,8))

year=[2015,2016,2017,2018,2019]
facebook_user=[500,550,650,750,850]
instagram_user=[100,150,200,250,300]
twitter_user=[250,300,350,400,450]
youtube_user=[350,400,500,550,600]

plt.plot(year,facebook_user,label='Facebook Users',marker='o',markersize=7,color='b')
plt.plot(year,instagram_user,label='Instagram Users',marker='x',markersize=7,color='g')
plt.plot(year,twitter_user,label='Twitter Users',marker='s',markersize=7,color='r')
plt.plot(year,youtube_user,label='Youtube Users',marker='d',markersize=7,color='m')

plt.xlabel('Year')
plt.ylabel('Users (million)')
plt.title('Growth of Social Media Users from 2015 to 2019')
plt.legend(loc='upper left')

plt.xticks(year)
plt.grid(axis='both',linestyle='--')

for i,j in zip(year,facebook_user):
    plt.annotate(str(j),xy=(i,j+15),rotation=45,ha='center',va='bottom')
for i,j in zip(year,instagram_user):
    plt.annotate(str(j),xy=(i,j+15),rotation=45,ha='center',va='bottom')
for i,j in zip(year,twitter_user):
    plt.annotate(str(j),xy=(i,j+15),rotation=45,ha='center',va='bottom')
for i,j in zip(year,youtube_user):
    plt.annotate(str(j),xy=(i,j+15),rotation=45,ha='center',va='bottom')

plt.tight_layout()
plt.savefig('line chart/png/459.png',dpi=200)
plt.clf()