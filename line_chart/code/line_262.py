
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
ax = plt.subplot()

year=[2010,2011,2012,2013,2014,2015,2016,2017]
num_users=[450,550,800,1000,1200,1600,2000,2500]
num_posts=[2300,3200,4500,6000,7200,9000,11000,13000]

plt.plot(year, num_users, label='Number of Users (million)', color='#e67e22', marker='o', linestyle='dashed', linewidth=2, markersize=7)
plt.plot(year, num_posts, label='Number of Posts (million)', color='#16a085', marker='o', linestyle='dashed', linewidth=2, markersize=7)
plt.title('Global Social Media Use and Posting Statistics from 2010 to 2017')
plt.xlabel('Year')
plt.ylabel('Number')
plt.xticks(year)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True, ncol=2)
plt.tight_layout()
plt.savefig('line chart/png/137.png', dpi=300)
plt.show()
plt.clf()