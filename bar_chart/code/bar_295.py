
import matplotlib.pyplot as plt
import numpy as np 

data = [['USA',20000,17000],
        ['UK',15000,18000],
        ['Germany',12000,16000],
        ['France',10000,14000]]

Country,Manufacturing_Output,Exports = zip(*data)

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1,1,1) 

bar_width = 0.35
ax.bar(Country, Manufacturing_Output, width=bar_width,label='Manufacturing Output(million)',color='green',align='center',alpha=0.8)
ax.bar(np.arange(len(Country))+bar_width, Exports, width=bar_width,label='Exports(million)',color='orange',align='center',alpha=0.8)

plt.xticks(np.arange(len(Country)),Country,rotation=30,ha='right',wrap=True)
plt.legend(loc='best')
plt.title('Manufacturing output and exports in four countries in 2021')
plt.tight_layout()
plt.savefig('bar chart/png/120.png')
plt.clf()