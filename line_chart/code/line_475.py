
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig=plt.figure(figsize=(8,5))
ax=fig.add_subplot(111)

# Set data 
x=np.array([2001,2002,2003,2004,2005,2006])
y1=np.array([200,250,280,300,290,310])
y2=np.array([300,320,340,360,380,400])
y3=np.array([400,450,400,420,410,450])

# Plot line
ax.plot(x,y1,color='red',label='Wheat Yield(tons)')
ax.plot(x,y2,color='green',label='Rice Yield(tons)')
ax.plot(x,y3,color='blue',label='Corn Yield(tons)')

# Set Legend
ax.legend(loc='upper left',bbox_to_anchor=(1,1))

# Set x-axis label
plt.xlabel('Year')

# Set y-axis label
plt.ylabel('Yield (tons)')

# Set title
plt.title('Yield of three major crops in the United States',fontsize=14)

# Set ticks
plt.xticks(x)

# Adjust the display
plt.tight_layout()

# Save the figure
plt.savefig('line chart/png/138.png')

# Clear the current image state
plt.clf()