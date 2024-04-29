
import matplotlib.pyplot as plt
import numpy as np

# set figure size
plt.figure(figsize=(8,5))

# set data
Country = ['USA','India','China','Japan','UK','Canada']
Number_of_Airports = [1000,750,650,900,500,200]

# set xticks
plt.xticks(np.arange(len(Country)),Country,rotation='vertical',wrap=True)

# draw line chart
plt.plot(Country,Number_of_Airports)

# set title
plt.title('Number of Airports in Selected Countries, 2021')

# set tight_layout
plt.tight_layout()

# save the figure
plt.savefig('line chart/png/317.png')

# clear current figure
plt.clf()