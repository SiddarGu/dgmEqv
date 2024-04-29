

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

month = ['January','February','March','April','May','June','July','August']
online = [100,120,140,160,180,200,220,240]
store = [200,180,150,120,90,80,100,120]

fig = plt.figure(figsize=(15,6))
ax = fig.add_subplot(1,1,1)
ax.plot(month, online, marker='o', label="Online Sales")
ax.plot(month, store, marker='o', label="Store Sales")

ax.xaxis.set_major_locator(ticker.MaxNLocator(8))
ax.set_title("Online versus Store Sales Trend in 2021")
ax.set_xlabel('Month')
ax.set_ylabel('billion dollars')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.savefig("line chart/png/118.png")
plt.tight_layout()
plt.clf()