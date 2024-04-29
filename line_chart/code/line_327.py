
import matplotlib.pyplot as plt

x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
donations = [1000, 3000, 2500, 2000, 1500, 1800, 2500, 3000]
volunteers = [50, 100, 70, 60, 50, 80, 100, 120]

# creating figure and adding subplot 
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()

# plotting line chart
ax.plot(x, donations, label='Donations', color='#1f77b4')
ax.plot(x, volunteers, label='Volunteers', color='#ff7f0e')

# setting title
ax.set_title('Annual donations and volunteers for a non-profit organization')

# setting axes labels
ax.set_xlabel('Year')
ax.set_ylabel('Quantity')

# setting x ticks
ax.set_xticks(x)

# setting legend
ax.legend(loc='best')

# automatically resize the image
plt.tight_layout()

# saving the plotted figure
plt.savefig('line chart/png/104.png')

# clearing the current image state
plt.clf()