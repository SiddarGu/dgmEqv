
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()

# Data
Country = ['USA', 'UK', 'Germany', 'France']
Sports_Venues = [50,60,70,80]
Tourists = [400,450,420,480]

# Bar chart
ax.bar(Country, Sports_Venues, label = 'Sports Venues', bottom = Tourists, color='#85C1E9')
ax.bar(Country, Tourists, color='#F1948A')

# Labels
ax.set_ylabel('Number of sports venues and tourists')
ax.set_title('Number of sports venues and tourists in four countries in 2021')
ax.legend()

# Annotate
for i,j in zip(Country,Sports_Venues):
    ax.annotate(str(j), xy=(i, j+10))
for i,j in zip(Country,Tourists):
    ax.annotate(str(j), xy=(i, j+10))

#Display
plt.xticks(Country)
plt.tight_layout()

# Save image
plt.savefig('Bar Chart/png/394.png')

# Clear figure
plt.clf()