

import matplotlib.pyplot as plt
import matplotlib.ticker as tck

month_label = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
productionA = [200,180,220,240,260]
productionB = [250,300,200,220,250]
productionC = [150,170,180,190,200]
productionD = [100,90,110,120,130]

# Create a figure
fig = plt.figure(figsize=(8,6))

# Add an axe
ax = fig.add_subplot(1,1,1)

# Plot line chart
ax.plot(month_label, productionA, label='Production A', marker='o', color='blue')
ax.plot(month_label, productionB, label='Production B', marker='s', color='red')
ax.plot(month_label, productionC, label='Production C', marker='^', color='green')
ax.plot(month_label, productionD, label='Production D', marker='*', color='black')

# Set xticks
ax.xaxis.set_major_locator(tck.FixedLocator(range(0, len(month_label))))
ax.xaxis.set_major_formatter(tck.FixedFormatter(month_label))

# Set title
ax.set_title("Monthly production of four products in 2021")

# Label each data point
for i in range(len(month_label)):
    ax.annotate(productionA[i], xy=(i, productionA[i]), rotation=45)
    ax.annotate(productionB[i], xy=(i, productionB[i]), rotation=45)
    ax.annotate(productionC[i], xy=(i, productionC[i]), rotation=45)
    ax.annotate(productionD[i], xy=(i, productionD[i]), rotation=45)

# Set legend
ax.legend(loc='best', ncol=2, fontsize='large')

# adjust figure
fig.tight_layout()

# save figure
plt.savefig('line chart/png/481.png')

# clear figure
plt.clf()