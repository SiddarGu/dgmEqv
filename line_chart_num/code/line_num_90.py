
import matplotlib.pyplot as plt
import numpy as np

#create figure
fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111)

#set data
year = np.array([2018,2019,2020,2021,2022])
num_tourist = np.array([20,23,15,25,22])
hotel_occ_rate = np.array([60,70,50,75,65])
avg_spend = np.array([1000,1200,900,1300,1100])

#plot line chart
ax.plot(year, num_tourist, 'b-', marker='o', label='Number of Tourists (million)')
ax.plot(year, hotel_occ_rate, 'r-', marker='o', label='Hotel Occupancy Rate (%)')
ax.plot(year, avg_spend, 'g-', marker='o', label='Average Spending Per Tourist (dollars)')

#label each data point
for i,j in zip(year,num_tourist):
    ax.annotate(str(j),xy=(i,j))
for i,j in zip(year,hotel_occ_rate):
    ax.annotate(str(j),xy=(i,j))
for i,j in zip(year,avg_spend):
    ax.annotate(str(j),xy=(i,j))
    
#set title and legend
ax.set_title("Tourist Trends in the United States from 2018 to 2022")
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

#set x ticks
plt.xticks(year, year)

#resize image
plt.tight_layout()

#save image
plt.savefig(r'line chart/png/563.png')

#clear current image
plt.clf()