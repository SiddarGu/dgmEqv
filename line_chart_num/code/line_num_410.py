
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Main
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Plot
ax.plot(['2015', '2016', '2017', '2018'], [10000, 12000, 15000, 18000], 'bo-', label='Soccer attendance')
ax.plot(['2015', '2016', '2017', '2018'], [15000, 17000, 20000, 22000], 'r^-', label='Basketball attendance')
ax.plot(['2015', '2016', '2017', '2018'], [20000, 25000, 30000, 35000], 'gs-', label='Football attendance')

# Setting
ax.set_title('Sports attendance in North America from 2015 to 2018', fontsize=16)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Attendance', fontsize=14)
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.set_xlim(left=2014.8, right=2018.2)
ax.set_ylim(bottom=8000, top=40000)
ax.legend(loc='upper left', fontsize=12)

# Data Point Label
ax.annotate('Soccer 10K', xy=(2015, 10000), xytext=(2015, 11000), fontsize=10, arrowprops=dict(facecolor='blue', shrink=0.05)) 
ax.annotate('Basketball 15K', xy=(2015, 15000), xytext=(2015, 16500), fontsize=10, arrowprops=dict(facecolor='red', shrink=0.05)) 
ax.annotate('Football 20K', xy=(2015, 20000), xytext=(2015, 21000), fontsize=10, arrowprops=dict(facecolor='green', shrink=0.05)) 
ax.annotate('Soccer 18K', xy=(2018, 18000), xytext=(2018, 17000), fontsize=10, arrowprops=dict(facecolor='blue', shrink=0.05)) 
ax.annotate('Basketball 22K', xy=(2018, 22000), xytext=(2018, 23000), fontsize=10, arrowprops=dict(facecolor='red', shrink=0.05)) 
ax.annotate('Football 35K', xy=(2018, 35000), xytext=(2018, 34000), fontsize=10, arrowprops=dict(facecolor='green', shrink=0.05)) 

# Resize
fig.tight_layout()

# Save
plt.savefig('line chart/png/442.png')

# Clear
plt.clf()