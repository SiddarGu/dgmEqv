
import matplotlib.pyplot as plt
plt.figure(figsize=(12,6))
plt.plot([2001,2002,2003,2004,2005],[14.5,14.6,13.7,15.2,15.7],label='GDP')
plt.plot([2001,2002,2003,2004,2005],[15,16,14,17,18],label='GNP')
plt.title('GDP and GNP from 2001 to 2005')
plt.xlabel('Year')
plt.ylabel('Value(trillion dollars)')
plt.xticks([2001,2002,2003,2004,2005])
plt.grid(True)
for x,y in zip([2001,2002,2003,2004,2005],[14.5,14.6,13.7,15.2,15.7]):
    plt.annotate('(%s, %s)' % (x,y),xy=(x,y), xytext=(x-0.1,y+0.5))
for x,y in zip([2001,2002,2003,2004,2005],[15,16,14,17,18]):
    plt.annotate('(%s, %s)' % (x,y),xy=(x,y), xytext=(x-0.1,y+0.5))
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('line chart/png/424.png')
plt.clf()