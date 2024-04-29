
import matplotlib.pyplot as plt
import numpy as np

Month = ['January','February','March','April','May','June']
WebsiteA = [1000,1200,1400,1800,1600,1200]
WebsiteB = [2000,1800,1600,2000,2200,1800]
WebsiteC = [3000,2500,3000,3500,4000,3500]

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)

ax.plot(Month, WebsiteA, label='Website A', color='green', linewidth=2)
ax.plot(Month, WebsiteB, label='Website B', color='orange', linewidth=2)
ax.plot(Month, WebsiteC, label='Website C', color='blue', linewidth=2)

plt.legend(loc='best')
plt.title("Monthly Website Hits in Three Categories in 2021")
plt.xlabel("Month")
plt.ylabel("Hits per million")

for x,y in zip(Month,WebsiteA):
    ax.annotate('{}'.format(y), xy=(x,y),  xycoords='data',
            xytext=(-10, 10), textcoords='offset points')
for x,y in zip(Month,WebsiteB):
    ax.annotate('{}'.format(y), xy=(x,y),  xycoords='data',
            xytext=(-10, 10), textcoords='offset points')
for x,y in zip(Month,WebsiteC):
    ax.annotate('{}'.format(y), xy=(x,y),  xycoords='data',
            xytext=(-10, 10), textcoords='offset points')

plt.xticks(Month)

plt.tight_layout()
plt.savefig('line chart/png/602.png')
plt.clf()