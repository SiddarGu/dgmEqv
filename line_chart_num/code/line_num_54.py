

import matplotlib.pyplot as plt
import numpy as np

# set the figure size
plt.figure(figsize=(12,8))

# set the data
Year = np.array([2017, 2018, 2019, 2020, 2021])
InternationalVisitor = np.array([3000, 3500, 4000, 4500, 5000])
DomesticVisitor = np.array([2500, 2700, 3000, 3300, 3700])

# plotting the line chart
plt.plot(Year, InternationalVisitor, color="red", label="International Visitor")
plt.plot(Year, DomesticVisitor, color="blue", label="Domestic Visitor")

# set the x ticks
plt.xticks(Year, Year, rotation='vertical')

# set the title
plt.title("Tourist Visitor in the USA from 2017 to 2021")

# set the legend
plt.legend(loc="upper right")

# add the labels
for a, b in zip(Year, InternationalVisitor):
    plt.annotate('{}'.format(b), xy=(a, b), xytext=(a-0.1, b+100))
for a, b in zip(Year, DomesticVisitor):
    plt.annotate('{}'.format(b), xy=(a, b), xytext=(a-0.1, b+100))

# set the tight layout
plt.tight_layout()

# save the image
plt.savefig('line chart/png/254.png')

# clear the current image state
plt.clf()