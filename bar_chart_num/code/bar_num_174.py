
import matplotlib.pyplot as plt
import numpy as np

# set up data 
data = np.array([[500, 4000, 8000], [600, 4500, 9000], [550, 5000, 9500], [650, 4800, 8700]])

# set up labels
Country = ["USA", "UK", "Germany", "France"]
Professionals = ["Hospitals", "Doctors", "Nurses"]

# create figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()

# set up bottom of the bar
bottom = np.zeros(len(Country))

# draw bars
for i in range(len(Professionals)):
    ax.bar(Country, data[:,i], label=Professionals[i], bottom=bottom)
    bottom += data[:,i]

# annotate values
for i in range(len(Country)):
    ax.annotate(str(data[i][0]), xy=(Country[i], data[i][0]/2), ha='center')
    ax.annotate(str(data[i][1]), xy=(Country[i], bottom[i]-data[i][1]/2), ha='center')
    ax.annotate(str(data[i][2]), xy=(Country[i], bottom[i]-data[i][2]/2), ha='center')

# rotate xticks
plt.xticks(rotation=45)

# add legend
plt.legend()

# add title
plt.title('Number of healthcare facilities and professionals in four countries in 2021')

# adjust the layout
plt.tight_layout()

# save the figure
plt.savefig('Bar Chart/png/407.png')

# clear the current image state
plt.clf()