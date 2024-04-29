
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)
ax.bar(['USA','UK','Germany','France'],[1400,1200,1000,900],label='Website Visits(million)',width=0.4,bottom=0)
ax.bar(['USA','UK','Germany','France'],[750,650,550,500],label='Ads Viewed(million)',width=0.4,bottom=0)
ax.set_title('Number of website visits and ads viewed in four countries in 2021')
ax.set_ylabel('Number of visits(million)')
plt.xticks(rotation=45,ha='right',wrap=True)
plt.grid(True)
ax.legend()
plt.tight_layout()
plt.savefig('bar chart/png/513.png')
plt.clf()