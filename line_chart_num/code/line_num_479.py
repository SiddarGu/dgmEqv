
import matplotlib.pyplot as plt 
import numpy as np 

# Set parameters 
plt.figure(figsize=(12, 8)) 
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False 

# Get data 
x = np.array([2016, 2017, 2018, 2019, 2020]) 
y1 = np.array([8, 7, 7.5, 8.5, 7.9])
y2 = np.array([2.2, 3.5, 4.5, 5.0, 6.0])
y3 = np.array([1.5, 2.2, 3.5, 4.2, 5.1])

# Draw line chart 
plt.plot(x, y1, marker='o', label='Online hours(hours/day)')
plt.plot(x, y2, marker='o', label='Facebook Likes(million)')
plt.plot(x, y3, marker='o', label='Twitter Tweets(million)')

# Label each data point 
for xy in zip(x, y1):
    plt.annotate("%.1f" % xy[1], xy=xy, xytext=(-20, 10), textcoords='offset points')
for xy in zip(x, y2):
    plt.annotate("%.1f" % xy[1], xy=xy, xytext=(-20, 10), textcoords='offset points')
for xy in zip(x, y3):
    plt.annotate("%.1f" % xy[1], xy=xy, xytext=(-20, 10), textcoords='offset points')

# Set title 
plt.title('Average Online Hours and Social Media Engagement from 2016 to 2020', fontsize=20) 

# Set legend position 
plt.legend(loc='upper left') 

# Set tick and labels 
plt.xticks(x) 
plt.xlabel('Year', fontsize=15) 
plt.ylabel('Values', fontsize=15)

# Automatically resize the image 
plt.tight_layout()

# Save picture 
plt.savefig("line chart/png/460.png", dpi=300)

# Clear current image 
plt.clf()