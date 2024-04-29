
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

#create figure
plt.figure(figsize=(8,8))

#create data
Devices = ('Desktop','Laptop','Smartphone','Tablet','Wearable')
Percentage = [25,20,30,15,10]

#plot pie chart
plt.pie(Percentage, labels=Devices,autopct='%1.1f%%', shadow=True, startangle=90)

#set chart title
plt.title("Device Usage Distribution Among Internet Users, 2023")

#set chart legend
plt.legend(labels=Devices, loc="best", bbox_to_anchor=(-0.1, 1.), fontsize=12)

#automatically resize the image
plt.tight_layout()

#save the figure
plt.savefig('pie chart/png/274.png')

#clear the current image state
plt.clf()