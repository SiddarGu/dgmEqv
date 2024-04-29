
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

data=[(2015,500,600,400,300),(2016,550,620,450,320),(2017,600,630,420,340),(2018,625,650,425,360),(2019,650,670,450,380),(2020,675,690,475,400)]
year=[x[0] for x in data]
research_a=[x[1] for x in data]
research_b=[x[2] for x in data]
research_c=[x[3] for x in data]
research_d=[x[4] for x in data]

# Create figure
fig=plt.figure(figsize=(15,7))

# Plot data
plt.plot(year, research_a, label='Research A(million dollars)', marker='o')
plt.plot(year, research_b, label='Research B(million dollars)', marker='+')
plt.plot(year, research_c, label='Research C(million dollars)', marker='*')
plt.plot(year, research_d, label='Research D(million dollars)', marker='^')

# set the x axis
plt.xticks(year, rotation=45)

# Add annotations
for i,j in zip(year,research_a):
    plt.annotate(str(j),xy=(i,j), fontsize=12)

for i,j in zip(year,research_b):
    plt.annotate(str(j),xy=(i,j), fontsize=12)

for i,j in zip(year,research_c):
    plt.annotate(str(j),xy=(i,j), fontsize=12)

for i,j in zip(year,research_d):
    plt.annotate(str(j),xy=(i,j), fontsize=12)

# Add legend and title
plt.legend(loc='best')
plt.title("Investment in four research fields from 2015 to 2020")

# Resize the figure
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/273.png')

# Clear the current figure state
plt.clf()