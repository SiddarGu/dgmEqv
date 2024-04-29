
import matplotlib.pyplot as plt
plt.figure(figsize=(13,7)) # Set the size of the figure
plt.title('Population in the US and its related economic indicators from 2001 to 2005') # Set the title of the figure
plt.xlabel('Year') # Set the x-axis label
plt.ylabel('Data') # Set the y-axis label
plt.grid(True, linestyle = "-.", color = "b", linewidth = "0.5") # Set the background grid
plt.plot(['2001','2002','2003','2004','2005'],[100,102,105,109,112],label = 'Population(million people)', marker = 'o', color = 'green')
plt.plot(['2001','2002','2003','2004','2005'],[2.5,3.2,4.8,5.3,4.2],label = 'Unemployment Rate', marker = 'o', color = 'red')
plt.plot(['2001','2002','2003','2004','2005'],[2.2,2.9,3.4,4.1,4.5],label = 'Inflation Rate', marker = 'o', color = 'blue')

plt.xticks(['2001','2002','2003','2004','2005']) # Set the points on the x-axis

# Add the label
plt.annotate('100',xy = ('2001',100), xytext = ('2001.2',100.2), rotation = 90, color = 'green', fontsize = 10)
plt.annotate('102',xy = ('2002',102), xytext = ('2002.2',102.2), rotation = 90, color = 'green', fontsize = 10)
plt.annotate('105',xy = ('2003',105), xytext = ('2003.2',105.2), rotation = 90, color = 'green', fontsize = 10)
plt.annotate('109',xy = ('2004',109), xytext = ('2004.2',109.2), rotation = 90, color = 'green', fontsize = 10)
plt.annotate('112',xy = ('2005',112), xytext = ('2005.2',112.2), rotation = 90, color = 'green', fontsize = 10)
plt.annotate('2.5',xy = ('2001',2.5), xytext = ('2001.2',2.7), rotation = 90, color = 'red', fontsize = 10)
plt.annotate('3.2',xy = ('2002',3.2), xytext = ('2002.2',3.4), rotation = 90, color = 'red', fontsize = 10)
plt.annotate('4.8',xy = ('2003',4.8), xytext = ('2003.2',5), rotation = 90, color = 'red', fontsize = 10)
plt.annotate('5.3',xy = ('2004',5.3), xytext = ('2004.2',5.5), rotation = 90, color = 'red', fontsize = 10)
plt.annotate('4.2',xy = ('2005',4.2), xytext = ('2005.2',4.4), rotation = 90, color = 'red', fontsize = 10)
plt.annotate('2.2',xy = ('2001',2.2), xytext = ('2001.2',2.4), rotation = 90, color = 'blue', fontsize = 10)
plt.annotate('2.9',xy = ('2002',2.9), xytext = ('2002.2',3.1), rotation = 90, color = 'blue', fontsize = 10)
plt.annotate('3.4',xy = ('2003',3.4), xytext = ('2003.2',3.6), rotation = 90, color = 'blue', fontsize = 10)
plt.annotate('4.1',xy = ('2004',4.1), xytext = ('2004.2',4.3), rotation = 90, color = 'blue', fontsize = 10)
plt.annotate('4.5',xy = ('2005',4.5), xytext = ('2005.2',4.7), rotation = 90, color = 'blue', fontsize = 10)

plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.02), ncol=1,borderaxespad=0) # Set the position of the legend
plt.tight_layout() # Automatically resize the image
plt.savefig('line chart/png/515.png') # Save the image
plt.clf() # Clear the current image state