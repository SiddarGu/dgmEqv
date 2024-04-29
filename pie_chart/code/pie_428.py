
import matplotlib.pyplot as plt
import numpy as np

labels = ['Stocks','Bonds','Mutual Funds','Options','Futures','ETFs']
sizes = [30,20,20,15,10,5]

fig = plt.figure(figsize=(10, 10))
ax1 = fig.add_subplot(111)
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.set_title('Distribution of Financial Instruments in the Global Investment Market in 2023')
ax1.axis('equal') 
plt.tight_layout()
plt.savefig('pie chart/png/384.png')
plt.clf()