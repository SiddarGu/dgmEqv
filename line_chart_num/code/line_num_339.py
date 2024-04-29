
import matplotlib.pyplot as plt
import numpy as np

# Set data
Month = np.array(['January','February','March','April','May','June','July','August'])
Production_A = np.array([1000,1200,1400,1500,1700,1800,2000,2100])
Production_B = np.array([500,600,700,800,900,1000,1100,1200])
Production_C = np.array([800,900,1000,1100,1200,1300,1400,1500])

# Create figure
fig = plt.figure(figsize=(15,7))

# Plot line chart
plt.plot(Month,Production_A,label='Production A',marker='o',linestyle='-',markersize=10)
plt.plot(Month,Production_B,label='Production B',marker='v',linestyle='--',markersize=10)
plt.plot(Month,Production_C,label='Production C',marker='s',linestyle='-.',markersize=10)

# Add title and axis names
plt.title('Monthly Production of Three Different Products in 2021')
plt.xlabel('Month')
plt.ylabel('Production')

# Set xticks
xticks = np.arange(len(Month))
plt.xticks(xticks, Month, rotation=45)

# Add legend
plt.legend(loc='best')

# Add annotation
for x, y in zip(xticks, Production_A):
	plt.annotate(f'{y}', xy=(x, y))
for x, y in zip(xticks, Production_B):
	plt.annotate(f'{y}', xy=(x, y))
for x, y in zip(xticks, Production_C):
	plt.annotate(f'{y}', xy=(x, y))

# Automatically resize the image
plt.tight_layout()

# Save and show figure
plt.savefig('line chart/png/268.png')
plt.show()

# Clear the current image state
plt.cla()
plt.clf()
plt.close()