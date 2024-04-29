
import matplotlib.pyplot as plt
plt.figure(figsize=(10,8))
ax = plt.subplot()
ax.plot([2001,2002,2003,2004,2005,2006,2007], [200,220,250,280,300,350,400], label='Average Price', marker='o', color='orange')
ax.plot([2001,2002,2003,2004,2005,2006,2007], [1000,1200,1300,1500,1800,2000,2500], label='Number of Transactions', marker='o', color='blue')
ax.set_xlabel('Year')
ax.set_ylabel('Value')
plt.xticks([2001,2002,2003,2004,2005,2006,2007], rotation=45)
ax.set_title('Changes in Average House Prices and Number of Transactions in the U.S. from 2001 to 2007')
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.tight_layout()
plt.savefig('line chart/png/447.png')
plt.clf()