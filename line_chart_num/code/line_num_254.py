
import matplotlib.pyplot as plt
x = [2001, 2002, 2003, 2004, 2005, 2006]
y1 = [1000, 1200, 1100, 1300, 1400, 1500]
y2 = [100, 125, 150, 175, 200, 225]
plt.figure(figsize=(10, 5))
plt.plot(x, y1, label="Yield (tonnes)")
plt.plot(x, y2, label="Cost of production (dollars)")
plt.title('Yield and cost of production of maize in the USA from 2001 to 2006')
plt.xlabel('Year')
plt.ylabel('Yield and Cost')
plt.legend(loc ='upper right')
plt.xticks(x)
for a,b,c in zip(x,y1,y2):
    plt.annotate('Yield:{} Cost:{}'.format(b,c),xy=(a,b))
plt.grid()
plt.tight_layout()
plt.savefig('line chart/png/61.png')
plt.clf()