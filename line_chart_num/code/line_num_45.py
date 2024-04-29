
import matplotlib.pyplot as plt
import numpy as np
 
# Generate figure
plt.figure(figsize=(10,6))
 
# Generate subplot
ax = plt.subplot()
 
# Set plot data
day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
num_users = [40000, 45000, 50000, 55000, 60000, 65000, 70000]
num_tweets = [20000, 24000, 30000, 35000, 40000, 45000, 50000]
 
# Generate chart
ax.plot(day, num_users, label="Number of Online Users")
ax.plot(day, num_tweets, label="Number of Tweets")
 
# Generate label
for i,j in zip(day,num_users):
    ax.annotate(str(j),xy=(i,j))
for i,j in zip(day,num_tweets):
    ax.annotate(str(j),xy=(i,j))
 
# Generate other features
ax.set_title("Social Media Usage Trend in a Week")
ax.set_xlabel("Day")
ax.set_ylabel("Number of Users/Tweets")
ax.legend()
ax.grid()
 
# Save the figure
plt.savefig("line chart/png/375.png")
 
# Clear the image state
plt.clf()