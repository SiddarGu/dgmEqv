
import matplotlib.pyplot as plt
import numpy as np

# set data
Country = ['USA', 'UK', 'Germany', 'France']
Wind_Energy = [20, 25, 15, 18]
Solar_Energy = [30, 35, 40, 38]
Geothermal_Energy = [5, 10, 15, 20]

# Create figure and set figure size
fig=plt.figure(figsize=(10,6))

# Plot bar chart
x=np.arange(len(Country))
rect1=plt.bar(x,Wind_Energy,width=0.3,label='Wind Energy',align='center')
rect2=plt.bar(x+0.3,Solar_Energy,width=0.3,label='Solar Energy',align='center')
rect3=plt.bar(x+0.6,Geothermal_Energy,width=0.3,label='Geothermal Energy',align='center')

# Set x-axis
plt.xticks(x+0.3,Country,rotation=45,wrap=True)

# Set legend
plt.legend(bbox_to_anchor=(1, 1))

# Set title
plt.title('Energy production from wind, solar and geothermal sources in four countries in 2021')

# Automatically resize the image by tight_layout
plt.tight_layout()

# Save the figure
plt.savefig('bar chart/png/196.png')

# Clear the current image state
plt.clf()