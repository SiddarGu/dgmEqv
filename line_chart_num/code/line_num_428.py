
import matplotlib.pyplot as plt
import numpy as np

# setting the figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)

# setting the data 
months = np.array(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August'])
cars = np.array([500, 600, 550, 575, 625, 650, 700, 725])
trucks = np.array([200, 250, 300, 275, 325, 350, 400, 425])
buses = np.array([100, 125, 150, 175, 200, 225, 250, 275])

# plotting the line chart
ax.plot(months, cars, label="Cars", color='#6495ED', marker='o', linestyle = '--')
ax.plot(months, trucks, label="Trucks", color='#B22222', marker='o', linestyle = '--')
ax.plot(months, buses, label="Buses/Vans", color='#228B22', marker='o', linestyle = '--')

# setting the label of x axis
ax.set_xticks(months)

# setting the title of the figure
ax.set_title('Vehicle Usage in the United States during 2020')

# setting the legend
ax.legend()

# setting the label of y axis
ax.set_ylabel('Number of vehicles')

# setting the value of each data point directly on the figure
for i, txt in enumerate(cars):
    ax.annotate(txt, (months[i],cars[i]))
for i, txt in enumerate(trucks):
    ax.annotate(txt, (months[i],trucks[i]))
for i, txt in enumerate(buses):
    ax.annotate(txt, (months[i],buses[i]))

# resizing the image
fig.tight_layout()

# saving the figure
plt.savefig('line chart/png/431.png')

# clearing the current image state
plt.clf()