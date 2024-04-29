

import matplotlib.pyplot as plt 

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111)

x = ['North East','South East','West Coast','Midwest']
y1 = [250,270,280,260]
y2 = [500,520,540,530]

ax.bar(x,y1,width=0.4,label='Average House Price (thousand dollars)')
ax.bar(x,y2,width=0.4,bottom=y1,label='Homes Sold')

ax.set_title('Average house prices and number of homes sold in four regions in 2021', fontsize=20)
ax.set_ylabel('Price/Sold', fontsize=15)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=15)
ax.set_xticklabels(x, rotation=45, fontsize=15)
ax.tick_params(axis='both', which='major', labelsize=13)

plt.tight_layout()
plt.savefig('bar chart/png/277.png')

plt.clf()