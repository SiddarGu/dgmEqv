
            
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot(111)

# Setting data
Year = [2010, 2011, 2012, 2013, 2014]
Facebook_Users = [500, 800, 1200, 1500, 2000]
Instagram_Users = [50, 100, 300, 500, 800]
YouTube_Users = [500, 800, 1200, 1500, 2000]
Twitter_Users = [100, 200, 300, 400, 500]

# Plotting the data
ax.plot(Year, Facebook_Users, color='r', label='Facebook Users')
ax.plot(Year, Instagram_Users, color='g', label='Instagram Users')
ax.plot(Year, YouTube_Users, color='b', label='YouTube Users')
ax.plot(Year, Twitter_Users, color='y', label='Twitter Users')

# Setting label, title, ticks, and legend
ax.set_title("Global Social Media User Growth from 2010 to 2014")
ax.set_xlabel("Year")
ax.set_ylabel("Users (million)")
ax.set_xticks(Year)
ax.legend(loc="upper left")

# Adding annotation
for a, b in zip(Year, Facebook_Users):
    ax.annotate(str(b), xy=(a, b), xytext=(a, b+10))
for a, b in zip(Year, Instagram_Users):
    ax.annotate(str(b), xy=(a, b), xytext=(a, b+10))
for a, b in zip(Year, YouTube_Users):
    ax.annotate(str(b), xy=(a, b), xytext=(a, b+10))
for a, b in zip(Year, Twitter_Users):
    ax.annotate(str(b), xy=(a, b), xytext=(a, b+10))

# Adding grids and tight_layout
ax.grid(linestyle='--')
fig.tight_layout()

# Saving the figure
plt.savefig('line chart/png/100.png')

# Clear the current image state
plt.clf()