
import matplotlib.pyplot as plt
import numpy as np

# set figure
plt.figure(figsize=(7,5))

# define data
Country = ['USA','UK','Germany','France']
Ticket_Sales = [3.5,3,2.5,2.8]
Viewers = [40,35,30,38]

# plot data
plt.bar(Country, Ticket_Sales, label='Ticket Sales(million)', bottom=0)
plt.bar(Country, Viewers, label='Viewers(million)', bottom=Ticket_Sales)

# set legend
plt.legend(bbox_to_anchor=(1,1), loc='upper left')

# set xticks and title
plt.xticks(Country, rotation=45, wrap=True)
plt.title('Ticket sales and viewers of sports and entertainment in four countries in 2021')

# adjust figure
plt.tight_layout()

# save figure
plt.savefig('bar chart/png/269.png', bbox_inches='tight')

# clear figure
plt.clf()