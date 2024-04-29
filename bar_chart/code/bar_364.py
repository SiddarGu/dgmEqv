

import matplotlib.pyplot as plt
import numpy as np

#create figure
fig = plt.figure(figsize=(8,6))

#data
region = ["North America","Europe","Asia","Africa"]
beds = [2.5,3.2,1.5,0.8]
doctors = [3.8,4.2,2.3,1.2]

#plot
plt.bar(region,beds,bottom=0,width=0.4,label="Hospital Beds/1000 People")
plt.bar(region,doctors,bottom=beds,width=0.4,label="Doctors/1000 People")

#set title
plt.title('Healthcare resources in different regions in 2021')

#set xtick
plt.xticks(rotation=0, ha='center')
plt.yticks(np.arange(0, 8, 0.5))

#set legend
plt.legend(loc='upper left')

#prevent content from being displayed
plt.tight_layout()

#save
plt.savefig('bar chart/png/517.png')

#clear
plt.clf()