
import matplotlib.pyplot as plt 

year = [2011,2012,2013,2014,2015,2016]
twitter_users =[10,20,40,50,70,90]
instagram_users = [3,5,10,15,20,25]
facebook_users = [500,700,900,1100,1300,1500]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
ax.plot(year, twitter_users, label='Twitter Users(million)')
ax.plot(year, instagram_users, label='Instagram Users(million)')
ax.plot(year, facebook_users, label='Facebook Users(million)')
ax.set_xlabel('Year')
ax.set_ylabel('Users(million)')
ax.set_title('Trend of Social Media Users in 2011-2016')
ax.legend(loc='upper left', frameon=False)
ax.grid(linestyle='dotted')

for x,y in zip(year,twitter_users):
    label = '{}'.format(y) 
    ax.annotate(label,xy=(x,y),xytext=(-5,5),textcoords='offset points')
for x,y in zip(year,instagram_users):
    label = '{}'.format(y) 
    ax.annotate(label,xy=(x,y),xytext=(-5,5),textcoords='offset points')
for x,y in zip(year,facebook_users):
    label = '{}'.format(y) 
    ax.annotate(label,xy=(x,y),xytext=(-5,5),textcoords='offset points')

ax.set_xticks(year)
plt.tight_layout()
plt.savefig('line chart/png/391.png')
plt.clf()