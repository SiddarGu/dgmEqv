
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig=plt.figure(figsize=(8, 6))
ax=fig.add_subplot(1,1,1)

# Set data
xdata=np.array([2001,2002,2003,2004])
ydata_a=np.array([1000,1200,800,1500])
ydata_b=np.array([800,900,1100,1200])
ydata_c=np.array([1200,1100,1300,1400])
ydata_d=np.array([1500,1600,1200,800])

# Plot
ax.plot(xdata,ydata_a,label='Crop Yield A(tons)',linewidth=2,marker='o',markersize=8,color='r')
ax.plot(xdata,ydata_b,label='Crop Yield B(tons)',linewidth=2,marker='v',markersize=8,color='b')
ax.plot(xdata,ydata_c,label='Crop Yield C(tons)',linewidth=2,marker='s',markersize=8,color='g')
ax.plot(xdata,ydata_d,label='Crop Yield D(tons)',linewidth=2,marker='D',markersize=8,color='m')

# Set x ticks
plt.xticks(xdata)

# Set legend
plt.legend(loc='best')

# Set title
plt.title("Crop Yields from Four Different Crops in the USA from 2001 to 2004")

# Annotate
for a,b in zip(xdata,ydata_a):
    ax.annotate(str(b),xy=(a,b),xytext=(-20,10),textcoords='offset points')
for a,b in zip(xdata,ydata_b):
    ax.annotate(str(b),xy=(a,b),xytext=(-20,10),textcoords='offset points')
for a,b in zip(xdata,ydata_c):
    ax.annotate(str(b),xy=(a,b),xytext=(-20,10),textcoords='offset points')
for a,b in zip(xdata,ydata_d):
    ax.annotate(str(b),xy=(a,b),xytext=(-20,10),textcoords='offset points')

# Tight layout
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/311.png')

# Clear figure
plt.clf()