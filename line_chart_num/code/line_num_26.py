
import matplotlib.pyplot as plt
import numpy as np

Month = np.array(['January','February','March','April','May','June','July'])
Online_Shopping = np.array([100,90,80,110,120,130,140])
Retail_Shopping = np.array([120,150,170,140,150,130,120])
Total_Shopping = np.array([220,240,250,250,270,260,260])

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
ax.set_title('Comparison of Online and Retail Shopping Revenue in 2021', fontsize=15)
ax.plot(Month,Online_Shopping,label="Online Shopping(million dollars)", marker='o', markersize=7)
ax.plot(Month,Retail_Shopping,label="Retail Shopping(million dollars)", marker='o', markersize=7)
ax.plot(Month,Total_Shopping,label="Total Shopping(million dollars)", marker='o', markersize=7)
ax.set_xticks(Month)
ax.legend(loc="upper right")
ax.grid()
ax.set_xlabel('Month', fontsize=13)
ax.set_ylabel('Revenue(million dollars)', fontsize=13)

for i, txt in enumerate(Online_Shopping):
    ax.annotate(txt, (Month[i],Online_Shopping[i]), rotation=45, fontsize=10)
for i, txt in enumerate(Retail_Shopping):
    ax.annotate(txt, (Month[i],Retail_Shopping[i]), rotation=45, fontsize=10)
for i, txt in enumerate(Total_Shopping):
    ax.annotate(txt, (Month[i],Total_Shopping[i]), rotation=45, fontsize=10)

plt.tight_layout()
plt.savefig('line chart/png/542.png')
plt.clf()