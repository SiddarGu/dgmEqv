
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[2001,200,1000], [2002,225,1100], [2003,250,1200], [2004,275,1500], [2005,300,1700], [2006,325,2000]])

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

ax.plot(data[:,0], data[:,1], label = 'Average House Price(thousands of dollars)', color='blue', marker='o')
ax.plot(data[:,0], data[:,2], label = 'Number of Houses Sold', color='red', marker='o')

ax.set_title('Average House Prices and Sales in the US Housing Market from 2001-2006')
ax.set_xlabel('Year')
ax.set_ylabel('Price/Number')

for x,y,z in data:
    label = "({}k, {})".format(y,z)
    ax.annotate(label, (x,y), textcoords="offset points", xytext=(0,10), ha='center')

ax.legend()
plt.xticks(data[:,0])
plt.tight_layout()
plt.savefig("line chart/png/553.png")
plt.clf()