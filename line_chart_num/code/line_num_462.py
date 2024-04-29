
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)

# Set data
Year = np.array([2012,2013,2014,2015,2016])
Twitter = np.array([10,50,150,200,250])
Facebook = np.array([20,50,100,150,200])
Instagram = np.array([1,5,20,50,100])

# Plot the data
ax.plot(Year, Twitter, label='Twitter', color='b', linewidth=2.0)
ax.plot(Year, Facebook, label='Facebook', color='r', linewidth=2.0)
ax.plot(Year, Instagram, label='Instagram', color='g', linewidth=2.0)

# Set labels,title
ax.set_title('Social Media Platform Growth from 2012-2016')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Users')

# Set xticks
ax.set_xticks(Year)

# Show legend
ax.legend(loc='upper left')

# Label the data points
ax.annotate('({}, {})'.format(Year[0],Twitter[0]), xy=(2012, 10), xytext=(2014,30), 
            arrowprops=dict(facecolor='blue', shrink=0.05))
ax.annotate('({}, {})'.format(Year[1],Twitter[1]), xy=(2013, 50), xytext=(2014,60), 
            arrowprops=dict(facecolor='blue', shrink=0.05))
ax.annotate('({}, {})'.format(Year[2],Twitter[2]), xy=(2014, 150), xytext=(2013,100), 
            arrowprops=dict(facecolor='blue', shrink=0.05))
ax.annotate('({}, {})'.format(Year[3],Twitter[3]), xy=(2015, 200), xytext=(2016,150), 
            arrowprops=dict(facecolor='blue', shrink=0.05))
ax.annotate('({}, {})'.format(Year[4],Twitter[4]), xy=(2016, 250), xytext=(2015,230), 
            arrowprops=dict(facecolor='blue', shrink=0.05))

ax.annotate('({}, {})'.format(Year[0],Facebook[0]), xy=(2012, 20), xytext=(2014,30), 
            arrowprops=dict(facecolor='red', shrink=0.05))
ax.annotate('({}, {})'.format(Year[1],Facebook[1]), xy=(2013, 50), xytext=(2014,70), 
            arrowprops=dict(facecolor='red', shrink=0.05))
ax.annotate('({}, {})'.format(Year[2],Facebook[2]), xy=(2014, 100), xytext=(2013,120), 
            arrowprops=dict(facecolor='red', shrink=0.05))
ax.annotate('({}, {})'.format(Year[3],Facebook[3]), xy=(2015, 150), xytext=(2016,150), 
            arrowprops=dict(facecolor='red', shrink=0.05))
ax.annotate('({}, {})'.format(Year[4],Facebook[4]), xy=(2016, 200), xytext=(2015,210), 
            arrowprops=dict(facecolor='red', shrink=0.05))

ax.annotate('({}, {})'.format(Year[0],Instagram[0]), xy=(2012, 1), xytext=(2014,10), 
            arrowprops=dict(facecolor='green', shrink=0.05))
ax.annotate('({}, {})'.format(Year[1],Instagram[1]), xy=(2013, 5), xytext=(2014,20), 
            arrowprops=dict(facecolor='green', shrink=0.05))
ax.annotate('({}, {})'.format(Year[2],Instagram[2]), xy=(2014, 20), xytext=(2013,30), 
            arrowprops=dict(facecolor='green', shrink=0.05))
ax.annotate('({}, {})'.format(Year[3],Instagram[3]), xy=(2015, 50), xytext=(2016,50), 
            arrowprops=dict(facecolor='green', shrink=0.05))
ax.annotate('({}, {})'.format(Year[4],Instagram[4]), xy=(2016, 100), xytext=(2015,120), 
            arrowprops=dict(facecolor='green', shrink=0.05))

# Resize the image
plt.tight_layout()

# Save figure
fig.savefig('line chart/png/365.png')

# Close the figure
plt.close()