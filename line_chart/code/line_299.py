
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(10,6))
plt.subplot(1,1,1)
data = np.array([[2012,1000,800,700],
				[2013,1200,900,800],
				[2014,900,1100,900],
				[2015,1300,1200,1000],
				[2016,1100,1400,1100],
				[2017,1500,1500,1200]])
x=[2012,2013,2014,2015,2016,2017]
y1,y2,y3 = data[:,1],data[:,2],data[:,3]
plt.plot(x,y1,label="Voters in District A")
plt.plot(x,y2,label="Voters in District B")
plt.plot(x,y3,label="Voters in District C")
plt.title("Voter Turnout in Districts A, B, and C from 2012 to 2017")
plt.xlabel("Year")
plt.ylabel("Voters")
plt.xticks(x)
plt.legend(loc="upper left")
plt.tight_layout()
plt.savefig("line chart/png/180.png")
plt.clf()