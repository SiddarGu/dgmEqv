
import matplotlib.pyplot as plt
import numpy as np

#set figure size
fig = plt.figure(figsize=(12, 6))

#create  axis
ax = fig.add_subplot(111)

#set label
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Tax Rate / Unemployment Rate', fontsize=14)

#set title
ax.set_title('Changes in Tax Rate and Unemployment Rate in the US, 2008-2012', fontsize=14)

#set data
Year = [2008, 2009,2010, 2011, 2012]
Tax_Rate = [7,7.5,7.9,8.2,8.7]
Unemployment_Rate = [8.1,9.2,9.3,8.7,7.8]

#plot data
ax.plot(Year,Tax_Rate, label='Tax Rate', color='#3e719f', linewidth=3)
ax.plot(Year,Unemployment_Rate, label='Unemployment Rate', color='#3cba54', linewidth=3)

#set legend
legend = ax.legend(loc='upper center', shadow=True)

#set xticks
plt.xticks(Year)

#save figure
plt.savefig('line chart/png/41.png')

#clear current image state
plt.clf()