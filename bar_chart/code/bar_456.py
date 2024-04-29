
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(8,6))
ax=fig.add_subplot(111)
ax.set_title('Average house prices and sales volumes in four regions in 2021')
ax.bar(['North','East','South','West'],[400000,450000,500000,550000],width=0.4,label='Average House Price ($)',color='b')
ax.bar(['North','East','South','West'],[500,600,700,800],width=0.4,bottom=[400000,450000,500000,550000],label='Sales Volume (number)',color='g')
ax.set_xticks(['North','East','South','West'])
ax.set_ylabel('Price and Volume')
ax.legend(loc='upper left')
plt.tight_layout()
plt.savefig('bar chart/png/524.png')
plt.clf()