
import matplotlib.pyplot as plt
import numpy as np

# Set data
Country = ['USA', 'UK', 'Germany', 'France']
Galleries = [50, 60, 40, 70]
Artists = [150, 130, 140, 120]
Exhibitions = [10, 15, 18, 13]

# Create figure and plot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.bar(Country, Galleries, label='Galleries', color='#444444', width=0.4, bottom=0)
ax.bar(Country, Artists, label='Artists', color='#888888', width=0.4, bottom=Galleries)
ax.bar(Country, Exhibitions, label='Exhibitions', color='#cccccc', width=0.4, bottom=[i+j for i,j in zip(Galleries, Artists)])

# Set labels
ax.set_title('Number of galleries, artists and exhibitions in four countries in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Number')
ax.set_xticks(Country)

# Show values
for i, j in zip(Galleries, Artists):
    ax.annotate(str(i+j), xy=(Country[Galleries.index(i)], i+j/2))
for i, j, k in zip(Galleries, Artists, Exhibitions):
    ax.annotate(str(i+j+k), xy=(Country[Galleries.index(i)], i+j+k/2))

# Place legend
ax.legend(loc='upper left')

# Make chart tight
plt.tight_layout()

#Save image
plt.savefig('Bar Chart/png/606.png')

# Clear figure
plt.clf()